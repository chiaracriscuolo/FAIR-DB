import express from 'express'
import multer from 'multer'
// const fs = require('fs')

const app = express()
const storage = multer.diskStorage({
  destination (req, file, cb) {
    cb(null, './static')
  },
  filename (req, file, cb) {
    // const uniqueSuffix = Date.now() + '-' + Math.round(Math.random() * 1e9)
    // cb(null, file.fieldname + '-' + uniqueSuffix + '.csv')
    cb(null, file.fieldname + '.csv')
  }
})

const upload = multer({ storage })
// const upload = multer({ dest: './static/' })
// We need this one if we send data inside the body as JSON
app.use(express.json())

// Function to call python script
function pythonDiscoveryScript (body, dataToSend, res) {
  let dataToSend2
  const { spawn } = require('child_process')
  // spawn new child process to call the python script
  // const subprocess = spawn('python', ['nodePythonApp/script1.py'])
  // const subprocess1 = spawn('./CFDD', ['./datasets/preprocessedTitanic.csv', 80, params.confidence, params.maxAntSize], { cwd: 'cdfAlgorithm/cfddiscovery' })
  const subprocess2 = spawn('pipenv', ['run', 'python', 'discoveryScript.py', JSON.stringify(body), dataToSend], { cwd: 'nodePythonApp' })
  // collect data from script
  subprocess2.stdout.on('data', function (data) {
    console.log('Pipe data from python script...')
    dataToSend2 = data.toString()
  })
  subprocess2.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`)
  })
  // in close event we are sure that stream from child process is closed
  subprocess2.on('close', (code) => {
    console.log(`child python process close all stdio with code ${code}`)
    // send data to browser
    console.log('Dati:' + dataToSend2)
    // dataToSend = 'static/ACFDsTitanic.json'
    res.json(dataToSend2)
    // return dataToSend2
  })
}

function init () {
  // This one is just an example
  app.get('/api/preprocessingUNUSED', (req, res) => {
    return res.json({
      url:
        'https://wordstream-files-prod.s3.amazonaws.com/s3fs-public/styles/simple_image/public/images/media/images/google-display-ads-example-2-final.png?oV7qevVB2XtFyF_O64TG6L27AFM3M2oL&itok=TBfuuTM_'
    })
  })

  // POST TO SAVE THE CUSTOM DATASET
  app.post('/import/postDataset', upload.single('dataset'), (req, res) => {
    let dataToSend = null
    const dataset = req.file
    console.log('DATASET: ')
    console.log(dataset)

    // CHIAMATA A SCRIPT IMPORT DATASET.PY PER CONVERTIRE .CSV IN .JSON
    const { spawn } = require('child_process')
    const subprocess = spawn('pipenv', ['run', 'python', 'importDataset.py', '../static/dataset.csv'], { cwd: 'nodePythonApp' })
    // collect data from script
    subprocess.stdout.on('data', function (data) {
      console.log('Pipe data from python script...')
      dataToSend = data.toString()
    })
    subprocess.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`)
    })
    // in close event we are sure that stream from child process is closed
    subprocess.on('close', (code) => {
      console.log(`child python process close all stdio with code ${code}`)
      // send data to browser
      console.log('Dati:' + dataToSend)
      // dataToSend = 'static/ACFDsTitanic.json'
      res.json(dataToSend)
    // return dataToSend2
    })
  })

  // example: get that calls a python script
  app.get('/postParamsUNUSED', (req, res) => {
    const { spawn } = require('child_process')
    let dataToSend
    // spawn new child process to call the python script
    // const subprocess = spawn('python', ['nodePythonApp/script1.py'])
    // const subprocess = spawn('python', ['nodePythonApp/discoveryScript.py', JSON.stringify(req.body)])
    const subprocess = spawn('pipenv', ['run', 'python', 'discoveryScript.py', JSON.stringify(req.body)], { cwd: 'nodePythonApp' })
    // collect data from script
    subprocess.stdout.on('data', function (data) {
      dataToSend = data.toString()
    })
    subprocess.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`)
    })
    // in close event we are sure that stream from child process is closed
    subprocess.on('close', (code) => {
      console.log(`child process close all stdio with code ${code}`)
      // send data to browser
      // res.send('Dati:' + dataToSend)
      res.json(dataToSend)
    })
  })

  // POST FOR CFD_DISCOVERY
  app.post('/preprocessing/postParams', (req, res) => {
    let dataToSend = ''
    const { spawn } = require('child_process')
    // spawn new child process to call the python script
    console.log(req.body)
    const params = req.body
    // const subprocess = spawn('python', ['nodePythonApp/script1.py'])
    const subprocess1 = spawn('./CFDD', ['./datasets/preprocessed' + params.dataset + '.csv', params.supportCount, params.confidence, params.maxAntSize], { cwd: 'cdfAlgorithm/cfddiscovery' })
    // const subprocess = spawn('pipenv', ['run', 'python', 'discoveryScript.py', JSON.stringify(req.body)], { cwd: 'nodePythonApp' })
    // collect data from script
    subprocess1.stdout.on('data', function (data) {
      console.log('Pipe data from c++ script...')
      dataToSend += data.toString()
    })
    subprocess1.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`)
    })
    // in close event we are sure that stream from child process is closed
    subprocess1.on('close', (code) => {
      console.log(`child c++ process close all stdio with code ${code}`)
      // send data to browser
      // res.send('Dati:' + dataToSend)
      // dataToSend = 'static/ACFDsTitanic.json'
      // console.log('First output inside: ', dataToSend)
      // console.log(typeof (dataToSend), dataToSend
      console.log('Dipendenze: ' + dataToSend)
      pythonDiscoveryScript(req.body, dataToSend, res)
      // console.log('BACKKKK:', pythonDiscoveryScript(req.body, dataToSend))
      // res.json(back)
    })
    // console.log('First output: ', dataToSend)
  })

  // POST TO CHANGE ORDER CRITERION
  app.post('/filtering/sortACFDs', (req, res) => {
    let dataToSend
    console.log('Input order: ', req.body)
    const { spawn } = require('child_process')
    const subprocess = spawn('pipenv', ['run', 'python', 'sortingScript.py', JSON.stringify(req.body)], { cwd: 'nodePythonApp' })
    // collect data from script
    subprocess.stdout.on('data', function (data) {
      dataToSend = data.toString()
    })
    subprocess.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`)
    })
    // in close event we are sure that stream from child process is closed
    subprocess.on('close', (code) => {
      console.log(`child process close all stdio with code ${code}`)
      console.log(dataToSend)
      // send data to browser
      // res.send('Dati:' + dataToSend)
      res.json(dataToSend)
    })
  })

  // POST TO COMPUTE STATISTICS
  app.post('/filtering/postACFDs', (req, res) => {
    let dataToSend
    console.log('Input statistics params: ', req.body)
    const { spawn } = require('child_process')
    const subprocess = spawn('pipenv', ['run', 'python', 'statisticsScript.py', JSON.stringify(req.body)], { cwd: 'nodePythonApp' })
    // collect data from script
    subprocess.stdout.on('data', function (data) {
      dataToSend = data.toString()
    })
    subprocess.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`)
    })
    // in close event we are sure that stream from child process is closed
    subprocess.on('close', (code) => {
      console.log(`child process close all stdio with code ${code}`)
      console.log(dataToSend)
      // send data to browser
      // res.send('Dati:' + dataToSend)
      res.json(dataToSend)
    })
  })
}

init()

export default app
