<template>
  <div class="container">
    <!--<div class="ui form">
      <div class="inline fields">
        <tr v-for="item in headers" :key="item">
          <div class="field">
            <div class="ui radio checkbox">
              <input type="radio" name="frequency">
              <label>{{ item }}</label>
            </div>
          </div>
        </tr>
      </div>-->

    <table class="ui definition table">
      <tbody>
        <tr v-for="item in headers" :key="item">
          <div class="field">
            <div type="ui radio checkbox">
              <td class="two wide column">
                <input type="radio" name="example2">
              </td>
              <td>
                {{ item }}
              </td>
            </div>
          </div>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>

export default {
  data () {
    return {
      headers: null
    }
  },
  async mounted () {
    const json = await this.$axios.get('/dataTitanic.json')
    const obj = JSON.parse(json.data)
    this.headers = obj.columns
  }
  /* methods: {
    async getHeaders () {
      const json = await this.$axios.get('/dataTitanic.json')
      // console.log(Object.keys(obj))
      // if (obj) { return Object.keys(obj) } else { return {} }
      const obj = JSON.parse(json.data)
      console.log(obj.columns)
      return obj.columns
    },
    getContent (obj) {
      // console.log(Object.keys(obj))
      // if (obj) { return Object.keys(obj) } else { return {} }
      // console.log(Object.keys(obj))
      return obj.data
    },
    async getTable () {
      const json = await this.$axios.get('/dataTitanic.json')
      // import VuePapaParse from 'vue-papa-parse'
      // Vue.use(VuePapaParse)
      // const csvData = await this.$axios.get('/preprocessingTitanic.csv')
      // var blob = new Blob([Papa.unparse(jsonData)], { type: 'csvData/csv;charset=utf-8;' });
      const data = JSON.parse(json.data)
      // console.log('KEYS:\n')
      // console.log(data.data)
      // console.log(Object.keys(data[0]))
      console.log(data)
      // console.log(data.data)
      return data
      // return JSON.parse(json.data)
      // return csvJSON('csv')
    }
  } */
}
</script>

<style scoped>
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
