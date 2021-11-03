<template>
  <main class="container">
    <!-- STEPS -->
    <div class="ui  ordered steps">
      <a class="active link step" href="/import">
        <div class="content">
          <div class="title">Import Dataset</div>
          <!--<div class="description">Select the dataset</div>-->
        </div>
      </a>
      <a class="step">
        <!--<i class="truck icon"></i>-->
        <div class="content">
          <div class="title">Data preprocessing</div>
          <!--<div class="description">Analyze the dataset</div>-->
        </div>
      </a>
      <a class="step">
        <div class="content">
          <div class="title">Selection</div>
          <!--<div class="description">Analyze ACFDs</div>-->
        </div>
      </a>
      <a class="step">
        <div class="content">
          <div class="title">Statistics</div>
          <!--<div class="description">Analyze Statistics</div>-->
        </div>
      </a>
    </div>
    <!-- END OF STEPS -->
    <div class="container">
      <section>
        <img style="width: 400px; height: 200px;" src="https://images.unsplash.com/photo-1483736762161-1d107f3c78e1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80" alt="Bot ADS">
        <h2>Import Dataset</h2>
        <p>
          You can try our demo <b>FAIR-DB</b> with our sample the <i>"Titanic dataset"</i> or you can upload your own dataset <b>(csv format is required)</b>.
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
        <a v-if="show" href="/preprocessing" aria-current="page" class="nuxt-link-exact-active nuxt-link-active">
          <button class="ui purple button">
            Titanic Dataset
          </button>
        </a>
        <a v-if="show" href="/preprocessing-census" aria-current="page" class="nuxt-link-exact-active nuxt-link-active">
          <button class="ui purple button">
            U.S. Census Dataset
          </button>
        </a>
        <!-- <div class="three wide column">
          <button class="ui purple button">
            Dataset 2
          </button>
        </div>-->
        <button v-if="show" class="ui purple button" @click="onPickFile">
          Upload your dataset
        </button>
        <input
          ref="fileInput"
          type="file"
          style="display: none"
          accept="json/*"
          @change="onFilePicked"
        >
        <div v-show="show_next">
          <a href="/preprocessing-custom" aria-current="page" class="nuxt-link-exact-active nuxt-link-active">
            <button class="ui purple button"> Use the dataset!</button>
          </a>
        </div>
      </div>
    </section>
  </main>
</template>

<script>
// import axios from 'axios'
export default {
  data () {
    return {
      dataset: null,
      // name: null,
      show: true,
      show_next: false
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
      this.$store.commit('updateFile', this.dataset)
      this.show_next = true
      this.show = false
    }
    // async postDataset () {
    // console.warn(this.params)
    // const self = this
    // this.show_loading = true
    // this.show_compute = false
    // const response = await axios.post('/api/selection/postParams', this.dataset, this.name)
    // axios.get('/api/preprocessingApi')
    // .then(function (response) {
    // Handle success
    // this.$router.push('/filtering')
    // console.log('----------', response.body)
    // this.show_loading = false
    // this.show_next = true
    // response.redirect('/filtering')
    // })
    // }
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
