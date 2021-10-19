<template>
  <main class="container">
    <div class="container">
      <section>
        <img src="https://images.unsplash.com/photo-1483736762161-1d107f3c78e1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80" alt="Bot ADS">
        <h2>Dataset Selection</h2>
        <p>
          You can try our demo <b>FAIR-DB</b> with our sample the <i>"Titanic dataset"</i> or you can upload your own dataset <b>(json format is required)</b>.
          Remember to delete all the missing values, categorize numerical attributes into bins and we suggest to use dataset with binary target variable.
          If you dataset have more than 1000 tuples we suggest to use the notebook version of the demo.
        </p>
        <p>
          To use our python notebook see our
          <a href="http://ceur-ws.org/Vol-2841/PIE+Q_4.pdf">
            github repo</a>
        </p>
      </section>
    </div>
    <section>
      <div class="ui grid">
        <a href="/preprocessing" aria-current="page" class="nuxt-link-exact-active nuxt-link-active">
          <button class="ui purple button">
            Titanic Dataset
          </button>
        </a>
        <!-- <div class="three wide column">
          <button class="ui purple button">
            Dataset 2
          </button>
        </div>-->
        <button class="ui purple button" @click="onPickFile">
          Upload your dataset
        </button>
        <input
          ref="fileInput"
          type="file"
          style="display: none"
          accept="json/*"
          @change="onFilePicked"
        >
      </div>
    </section>
    <div v-show="show" class="container">
      <a href="/preprocessing" aria-current="page" class="nuxt-link-exact-active nuxt-link-active">
        <button class="fluid ui purple button"> Use the dataset!</button>
      </a>
    </div>
  </main>
</template>

<script>
export default {
  data () {
    return {
      dataset: null,
      show: false
    }
  },
  methods: {
    onPickFile () {
      this.$refs.fileInput.click()
    },
    onFilePicked (event) {
      const files = event.target.files
      // const filename = files[0].name
      const fileReader = new FileReader()
      fileReader.addEventListener('load', () => {
        this.imageUrl = fileReader.result
      })
      fileReader.readAsDataURL(files[0])
      this.dataset = files[0]
      this.show = true
    }
  }
}
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
