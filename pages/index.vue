<template>
  <main class="container">
    <section>
      <img  src="~/static/fairnessPhoto.png" alt="Bot ADS">
      <!--<img src="https://images.unsplash.com/photo-1587740896339-96a76170508d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=471&q=80" alt="Bot ADS"> -->
      <h2>FunctionAl dependencIes to discoveR Data Bias</h2>
      <p>
        <b>FAIR-DB (FunctionAl dependencIes to discoveR Data Bias)</b> is a novel framework
        to detect biases and discover discrimination in datasets. By exploiting various kinds of functional
        dependencies, called Approximate Conditional Functional Dependencies (ACFDs), FAIR-DB can identify those attributes in a database that encompass discrimination (e.g.
        sex, ethnicity or religion) and the ones that instead satisfy various fairness criteria.
      </p>
      <p>
        To have more information see FAIR-DB papers (
        <a href="http://ceur-ws.org/Vol-2841/PIE+Q_4.pdf">
          1, </a>
        <a href="http://ceur-ws.org/Vol-2994/paper19.pdf">
          2 </a> )
      </p>
    </section>
    <div class="container">
      <a href="/import" aria-current="page" class="nuxt-link-exact-active nuxt-link-active">
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
