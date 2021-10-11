<template>
  <div class="container">
    <div class="container">
      <h4>Choose the ordering criterion</h4>
      <select class="ui selection dropdown">
        <option value="">
          Support
        </option>
        <option value="0">
          Confidence
        </option>
        <option value="1">
          Difference
        </option>
      </select>
    </div>

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
        <tr v-for="el in data" :key="el">
          <td class="collapsing">
            <div class="ui fitted checkbox">
              <input type="checkbox"> <label />
            </div>
          </td>
          <td v-for="i in el" :key="i">
            {{ i }}
          </td>

        <!--<div v-for="item in getHeaders(el)" :key="item._id">
            <td>{{ el[item] }}</td>
          </div>-->
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>

export default {
  data () {
    return {
      headers: null,
      data: null
    }
  },
  async mounted () {
    const json = await this.$axios.get('/dataTitanic.json')
    const obj = JSON.parse(json.data)
    this.data = obj.data.slice(0, 10)
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
