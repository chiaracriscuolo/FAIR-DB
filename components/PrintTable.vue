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
        <th />
        <tr v-for="item in getHeaders(getTable()[0])" :key="item">
          <th />
          <th>{{ item }}</th>
        </tr>
      </thead><tbody>
        <tr v-for="el in getTable()" :key="el._id">
          <td class="collapsing">
            <div class="ui fitted slider checkbox">
              <input type="checkbox"> <label />
            </div>
          </td>
          <div v-for="item in getHeaders(el)" :key="item._id">
            <td>{{ el[item] }}</td>
          </div>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
// import { csvJSON } from '~/middleware/csvJSON.js'
export default {
  methods: {
    getHeaders (obj) {
      // console.log(Object.keys(obj))
      if (obj) { return Object.keys(obj) } else { return {} }
    },
    async getTable () {
      const json = await this.$axios.get('/data.json')
      console.log(JSON.parse(json)[0])
      return JSON.parse(json)
      // return csvJSON('csv')
    }
  }
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

</style>
