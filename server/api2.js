import express from 'express'

const app = express()

// We need this one if we send data inside the body as JSON
app.use(express.json())

function init () {
  // API to get an article by ID.

  // This one is just an example
  app.get('/api/preprocessing', (req, res) => {
    return res.json({
      url:
        'https://wordstream-files-prod.s3.amazonaws.com/s3fs-public/styles/simple_image/public/images/media/images/google-display-ads-example-2-final.png?oV7qevVB2XtFyF_O64TG6L27AFM3M2oL&itok=TBfuuTM_'
    })
  })
  app.post('/postParams', (req, res) => {
    return res.send(req.body)
  })
}

init()

export default app
