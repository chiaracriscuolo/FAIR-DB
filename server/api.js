import express from 'express'

const app = express()

// We need this one if we send data inside the body as JSON
app.use(express.json())

function pythonDiscoveryScript (body, dataToSend, res) {
  let dataToSend2
  const { spawn } = require('child_process')
  // spawn new child process to call the python script
  // const subprocess = spawn('python', ['nodePythonApp/script1.py'])
  // const subprocess1 = spawn('./CFDD', ['./datasets/preprocessedTitanic.csv', 80, params.confidence, params.maxAntSize], { cwd: 'cdfAlgorithm/cfddiscovery' })
  const subprocess2 = spawn('pipenv', ['run', 'python', 'discoveryScript.py', JSON.stringify(body), JSON.stringify(dataToSend)], { cwd: 'nodePythonApp' })
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
    console.log(`child process close all stdio with code ${code}`)
    // send data to browser
    console.log('Dati:' + dataToSend2)
    // dataToSend = 'static/ACFDsTitanic.json'
    res.json(dataToSend2)
    // return dataToSend2
  })
}

function init () {
  // API to get a python script
  // API to get a python script
  app.get('/postParams', (req, res) => {
    const { spawn } = require('child_process')
    let dataToSend
    // spawn new child process to call the python script
    // const subprocess = spawn('python', ['nodePythonApp/script1.py'])
    const subprocess = spawn('python', ['nodePythonApp/discoveryScript.py', JSON.stringify(req.body)])
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
  app.post('/postParams', (req, res) => {
    const { spawn } = require('child_process')
    let dataToSend
    // spawn new child process to call the python script
    console.log(req.body)
    const params = req.body
    // const subprocess = spawn('python', ['nodePythonApp/script1.py'])
    const subprocess1 = spawn('./CFDD', ['./datasets/preprocessedTitanic.csv', params.supportCount, params.confidence, params.maxAntSize], { cwd: 'cdfAlgorithm/cfddiscovery' })
    // const subprocess = spawn('pipenv', ['run', 'python', 'discoveryScript.py', JSON.stringify(req.body)], { cwd: 'nodePythonApp' })
    // collect data from script
    subprocess1.stdout.on('data', function (data) {
      console.log('Pipe data from c++ script...')
      dataToSend = data.toString()
    })
    subprocess1.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`)
    })
    // in close event we are sure that stream from child process is closed
    subprocess1.on('close', (code) => {
      console.log(`child process close all stdio with code ${code}`)
      // send data to browser
      // res.send('Dati:' + dataToSend)
      // dataToSend = 'static/ACFDsTitanic.json'
      // console.log('First output inside: ', dataToSend)
      pythonDiscoveryScript(req.body, dataToSend, res)
      // console.log('Dati:' + back)
      // console.log('BACKKKK:', pythonDiscoveryScript(req.body, dataToSend))
      // res.json(back)
    })
    // console.log('First output: ', dataToSend)
  })
  // This one is just an example
  app.get('/api/preprocessing', (req, res) => {
    return res.json({
      url:
        'https://wordstream-files-prod.s3.amazonaws.com/s3fs-public/styles/simple_image/public/images/media/images/google-display-ads-example-2-final.png?oV7qevVB2XtFyF_O64TG6L27AFM3M2oL&itok=TBfuuTM_'
    })
  })
  // app.post('/postParams', (req, res) => {
  //  return res.send(req.body)
  // })
}

init()

export default app
