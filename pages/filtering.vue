<template>
  <div>
    <div class="container">
      <h4>Choose the ordering criterion</h4>
      <select v-model="params.orderingCriterion" class="ui selection dropdown">
        <option disabled value="">
          Select an ordering criterion
        </option>
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
        Apply Ordering Criterion!
      </button>

      <h4>Table of Functional Dependencies</h4>
      <table class="ui purple table">
        <thead>
          <tr>
            <th />
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
        <button class="ui purple button" @click="postACFDs()">
          Compute Statistics!
        </button>
      </div>
      <div class="container">
        <a v-if="show" href="/" aria-current="page" class="nuxt-link-exact-active nuxt-link-active">
          <button class="fluid ui purple button">
            See Statistics!
          </button>
        </a>
      </div>
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
      show: false,
      params: {
        acfds: [],
        orderingCriterion: ''
      }
    }
  },
  async mounted () {
    const json = await this.$axios.get('/ACFDsTitanicComputed.json')
    const obj = JSON.parse(json.data)
    this.data = obj.data.slice(0, 10)
    this.headers = obj.columns
  },
  methods: {
    pretty (value) {
      if (typeof (value) === 'number') {
        return value.toFixed(2)
      } else if (JSON.stringify(value) === 'null') { return 0 } else { return parseACFD(value) }
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
      // window.location.reload(true)
      // this.show = true
      // response.redirect('/filtering')
      // })
      return this.data
    },
    async postACFDs () {
      const response = await axios.post('/api/filtering/postACFDs', this.params)
      console.log('----------', response.body)
      this.show = true
      return this.data
    }
  }
}
</script>

<style scoped>
</style>
