import express from 'express'

const app = express()

// We need this one if we send data inside the body as JSON
app.use(express.json())

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
    // const subprocess = spawn('python', ['nodePythonApp/script1.py'])
    const subprocess = spawn('python', ['nodePythonApp/discoveryScript.py', JSON.stringify(req.body)])
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
      console.log(`child process close all stdio with code ${code}`)
      // send data to browser
      // res.send('Dati:' + dataToSend)
      dataToSend = 'static/ACFDsTitanic.json'
      res.json(dataToSend)
    })
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
