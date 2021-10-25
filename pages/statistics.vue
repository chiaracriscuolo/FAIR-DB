<template>
  <div class="container">
    <div>
      <h4>Table of Selected Functional Dependencies</h4>
      <table class="ui purple table">
        <thead>
          <tr>
            <th v-for="item in headers" :key="item">
              {{ item }}
            </th>
          </tr>
        </thead><tbody>
          <tr v-for="el in data" :key="el">
            <td v-for="i in el" :key="i" name="example2">
              <span class="ui black text">{{ pretty(i) }}</span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <br/>
    <div>
      <h4 class="ui horizontal divider header">
        <i class="table icon" />
        Problematic Tuples in the Dataset
      </h4>
      <PrintTable />
    </div>
    <div>
      <h4>Metrics</h4>
      <table class="ui purple table">
        <tbody>
          <tr>
            <td>
              Cumulative Support:
            </td>
            <td>
              {{ params.cumulativeSupport }}
            </td>
          </tr>
          <tr>
            <td>
              Difference Mean:
            </td>
            <td>
              {{ params.differenceMean }}
            </td>
          </tr>
          <tr v-for="(index,item) in params.pDiffs" :key="item">
            <td>
              P-Difference {{ item }}:
            </td>
            <td>
              {{ params.pDiffs[item] }}
            </td>
          </tr>
          <tr>
            <td>
              Total number of tuples:
            </td>
            <td>
              {{ params.totTuples }}
            </td>
          </tr>
          <tr>
            <td>
              Total number of problematic tuples:
            </td>
            <td>
              {{ params.tuplesInterested }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>

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
        cumulativeSupport: 0.86,
        differenceMean: 0.35,
        pDiffs: {
          Class: 0.12,
          Sex: 0.29
        },
        tuplesInterested: 100,
        totTuples: 876
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
