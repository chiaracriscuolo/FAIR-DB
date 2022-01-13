<template>
  <div class="container">
    <!-- STEPS -->
    <div class="ui  ordered steps">
      <a class="completed link step" href="/import">
        <div class="content">
          <div class="title">Import Dataset</div>
          <!--<div class="description">Select the dataset</div>-->
        </div>
      </a>
      <a class="completed link step" href="/preprocessing-census">
        <!--<i class="truck icon"></i>-->
        <div class="content">
          <div class="title">Preprocessing</div>
          <!--<div class="description">Analyze the dataset</div>-->
        </div>
      </a>
      <a class="active link step" href="/filtering-census">
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
    <h4 class="ui horizontal divider header">
      <i class="search icon" />
      Table of Functional Dependencies
    </h4>
    <p> This is the list of ACFDs that are extracted given the input parameters, select the ones that are more interesting for your research purpose. </p>
    <div class="ui two column grid">
      <div class="two column row">
        <div class="center aligned nine wide column">
          <h4>Choose the number of ACFDs to display</h4>
          <select v-model="nTuples" class="ui dropdown">
            <option value="10">
              10
            </option>
            <option value="50">
              50
            </option>
            <option value="100">
              100
            </option>
          </select>
          <button class="ui purple button" @click="displayTuples()">
            Display!
          </button>
        </div>
        <div class="five wide right aligned column">
          <h4>Choose the ordering criterion</h4>
          <select v-model="params.orderingCriterion" class="ui dropdown">
            <option value="Support">
              Support
            </option>
            <option value="Difference">
              Difference
            </option>
            <option value="Mean">
              Mean
            </option>
          </select>
          <button class="ui purple button" @click="sorted()">
            Order!
          </button>
        </div>
      </div>
    </div>
    <!--    TABLE -->
    <table class="ui purple table">
      <thead>
        <tr>
          <th><input v-model="selectAll" type="checkbox"></th>
          <th v-for="item in headers" :key="item">
            {{ item }}
          </th>
        </tr>
      </thead><tbody>
        <tr v-for="(el, index) in data" :key="el">
          <td class="collapsing">
            <div class="ui fitted checkbox">
              <input v-model="params.acfds" type="checkbox" :value="index"> <label />
            </div>
          </td>
          <td v-for="i in el" :key="i" name="example2">
            <span class="ui black text">{{ pretty(i) }}</span>
          </td>
        </tr>
      </tbody>
    </table>

    <div class="container">
      <button v-if="show_compute" class="ui purple button" @click="postACFDs()">
        Compute Statistics on the selected ACFDs!
      </button>
      <div v-if="show_loading" class="ui purple bottom attached loading tab">
        The process will take a few seconds
      </div>
    </div>
    <div class="container">
      <a v-if="show_next" href="/statistics-census" aria-current="page" class="nuxt-link-exact-active nuxt-link-active">
        <button class="fluid ui purple button">
          See Statistics!
        </button>
      </a>
    </div>
  </div>
</template>

<script>

import axios from 'axios'

function parseACFD (value) {
  /* value = value.replace('{', '')
  value = value.replace('},', '=>')
  value = value.replace('},', '')
  value = value.replace('"lhs":', '')
  value = value.replace('"rhs":', '') */

  return ' ' + JSON.stringify(value.lhs) + ' => ' + JSON.stringify(value.rhs)
}
export default {
  data () {
    return {
      headers: null,
      data: null,
      all: [],
      show_compute: true,
      show_next: false,
      show_loading: false,
      nTuples: 10,
      params: {
        acfds: [],
        orderingCriterion: '',
        dataset: 'Census'
      }
    }
  },
  computed: {
    selectAll: {
      get () {
        return this.all ? this.params.acfds.length === this.all.length : false
      },
      set (value) {
        let selected = []

        if (value) {
          selected = this.all
        }

        this.params.acfds = selected
      }
    }
  },
  async mounted () {
    const json = await this.$axios.get('/ACFDsCensusComputed.json')
    // const obj = JSON.parse(json.data)
    const obj = json.data
    this.all = obj.index
    this.data = obj.data.slice(0, 10)
    this.headers = obj.columns
  },
  methods: {
    pretty (value) {
      if (typeof (value) === 'number') {
        return value.toFixed(3)
      } else if (JSON.stringify(value) === 'null') { return 0 } else { return parseACFD(value) }
    },
    async displayTuples () {
      const json = await this.$axios.get('/ACFDsCensusComputed.json')
      const obj = json.data
      this.data = obj.data.slice(0, this.nTuples)
      this.headers = obj.columns
    },
    async sorted () {
      // console.warn(this.params)
      // const self = this
      console.log('---Order:', this.params.orderingCriterion)
      const response = await axios.post('/api/filtering/sortACFDs', this.params)
      // axios.get('/api/preprocessingApi')
      // .then(function (response) {
      // Handle success
      // this.$router.push('/filtering')
      console.log('----------', response.body)
      // To update the dataset
      const json = await this.$axios.get('/ACFDsCensusComputed.json')
      const obj = json.data
      this.data = obj.data.slice(0, 10)
      this.headers = obj.columns
      // window.location.reload(true)
      // this.show = true
      // response.redirect('/filtering')
      // })
      return this.data
    },
    async postACFDs () {
      this.show_compute = false
      this.show_loading = true
      const response = await axios.post('/api/filtering/postACFDs', this.params)
      console.log('----------', response.body)
      this.show_loading = false
      this.show_next = true
      return this.data
    }
  }
}
</script>

<style scoped>
.header{
  background-color: white;
}
table {
  margin: 0 auto;
  text-align: center;
  border-collapse: collapse;
  border: 1px solid #d4d4d4;
}

tr:nth-child(even) {
  background: #d4d4d4;
}

th, td {
  padding: 10px 30px;
}

th {
  border-bottom: 1px solid #d4d4d4;
}

.ui.selection.dropdown {
    height: 45px;
}
</style>
