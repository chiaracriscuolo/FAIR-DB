<template>
  <main class="container">
    <section>
      <img src="~/static/fairnessPhoto.png" alt="Bot ADS">
      <h2>FunctionAl dependencIes to discoveR Data Bias</h2>
      <p>
        We present FAIR-DB (FunctionAl dependencIes to discoveR Data Bias), a novel framework
        to detect biases and discover discrimination in datasets. By exploiting various kinds of functional
        dependencies, our tool can identify those attributes in a database that encompass discrimination (e.g.
        sex, ethnicity or religion) and the ones that instead satisfy various fairness criteria.
      </p>
      <p>
        To have more information see our
        <a href="http://ceur-ws.org/Vol-2841/PIE+Q_4.pdf">
          paper</a>
      </p>
    </section>
    <div class="container">
      <a href="/preprocessing" aria-current="page" class="nuxt-link-exact-active nuxt-link-active">
        <button class="fluid ui purple button">Start the demo!</button>
      </a>
    </div>
  </main>
</template>

<script>
export default {}
</script>

<style scoped>
h2 {
  color: #9627ba;
  margin-bottom: 30px;
}
h4 {
  margin-bottom: 30px;
}
img {
  max-width: 600px;
}
p {
  text-align: left;
}
a {
  color: #9627ba;
  text-underline-position: below;
  text-align: left;
}
button{
  color: #9627ba;
  transition: all 0.2s ease-in-out;
}
.fluid.ui.purple.button:hover{
  background-color: lightsalmon;
  color: white;
}
</style>
