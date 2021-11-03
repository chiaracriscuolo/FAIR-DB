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
      <a class="completed link step" href="/preprocessing">
        <!--<i class="truck icon"></i>-->
        <div class="content">
          <div class="title">Preprocessing</div>
          <!--<div class="description">Analyze the dataset</div>-->
        </div>
      </a>
      <a class="completed link step" href="/filtering">
        <div class="content">
          <div class="title">Selection</div>
          <!--<div class="description">Analyze ACFDs</div>-->
        </div>
      </a>
      <a class="active link step" href="/statistics">
        <div class="content">
          <div class="title">Statistics</div>
          <!--<div class="description">Analyze Statistics</div>-->
        </div>
      </a>
    </div>
    <!-- END OF STEPS -->
    <div>
      <br>
      <h4 class="ui horizontal divider header">
        Table of Selected Functional Dependencies
      </h4>
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
    <br>
    <div>
      <br>
      <h4 class="ui horizontal divider header">
        <i class="table icon" />
        Problematic Tuples in the Dataset
      </h4>
      <PrintTable url="/TitanicProblematicTuples.json" />
    </div>
    <div>
      <h4 class="ui horizontal divider header">
        Metrics
      </h4>
      <!-- progress bar?<div class="ui purple inverted progress">
        <div class="bar">
          <div class="centered active progress">
            {{ params.cumulativeSupport }}
          </div>
        </div>
      </div>-->
      <table class="ui purple table">
        <tbody>
          <tr>
            <td>
              <b>Cumulative Support:</b>
            </td>
            <td>
              <b>{{ pretty(params.cumulativeSupport) }}</b>
              <i v-if="show_support" class="exclamation red icon" />
            </td>
          </tr>
          <tr>
            <td>
              <b>Difference Mean:</b>
            </td>
            <td>
              <b>{{ pretty(params.differenceMean) }}</b>
              <i v-if="show_difference" class="exclamation red icon" />
            </td>
          </tr>
          <tr v-for="(index,item) in params.pDiffs" :key="item">
            <td>
              <b>P-Difference {{ item }}:</b>
            </td>
            <td>
              <b>{{ pretty(params.pDiffs[item]) }}</b>
            </td>
          </tr>
          <tr>
            <td>
              <b>Total number of tuples in the dataset:</b>
            </td>
            <td>
              <b>{{ params.totTuples }}</b>
            </td>
          </tr>
          <tr>
            <td>
              <b>Total number of "problematic" tuples:</b>
            </td>
            <td>
              <b>{{ params.totTuplesInterested }}</b>
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
        cumulativeSupport: null,
        differenceMean: null,
        pDiffs: {},
        totTuplesInterested: null,
        totTuples: null
      },
      show_difference: false,
      show_support: false
    }
  },
  pretty (value) {
    if (typeof (value) === 'number') {
      return value.toFixed(4)
    }
  },
  async mounted () {
    const json = await this.$axios.get('/TitanicFinalACFDs.json')
    const obj = json.data
    this.data = obj.data.slice(0, 10)
    this.headers = obj.columns
    const jsonMetrics = await this.$axios.get('/TitanicMetrics.json')
    const objMetrics = jsonMetrics.data
    this.params.cumulativeSupport = objMetrics.cumulativeSupport
    if (this.params.cumulativeSupport > 0.5) { this.show_support = true }
    this.params.differenceMean = objMetrics.differenceMean
    if (this.params.differenceMean > 0.05) { this.show_difference = true }
    this.params.totTuples = objMetrics.totTuples
    this.params.totTuplesInterested = objMetrics.totTuplesInterested
    this.params.pDiffs = objMetrics.pDiffs
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
