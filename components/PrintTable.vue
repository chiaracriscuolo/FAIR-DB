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
        <tr>
          <th />
          <th>FD</th>
          <th>Support</th>
          <th>Confidence</th>
          <th>Difference</th>
        </tr>
      </thead><tbody>
        <tr>
          <td class="collapsing">
            <div class="ui fitted slider checkbox">
              <input type="checkbox"> <label />
            </div>
          </td>
          <td>Woman => Salary</td>
          <td>0.8</td>
          <td>0.95</td>
          <td>0.1</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
// import csvJSON from '~/middelware/csvJSON.js'
export default {}
// methods: {
//  getTable () {
//    this.table = csvJSON('~/static/preprocessedTitanic.csv')
//  }
// }}
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
