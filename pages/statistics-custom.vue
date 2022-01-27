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
      <a class="completed link step" href="/preprocessing-custom">
        <!--<i class="truck icon"></i>-->
        <div class="content">
          <div class="title">Preprocessing</div>
          <!--<div class="description">Analyze the dataset</div>-->
        </div>
      </a>
      <a class="completed link step" href="/filtering-custom">
        <div class="content">
          <div class="title">Selection</div>
          <!--<div class="description">Analyze ACFDs</div>-->
        </div>
      </a>
      <a class="active link step" href="/statistics-custom">
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
        <i class="bookmark icon" />
        Table of Selected ACFDs
      </h4>
      <div class="ui two column grid">
        <div class="two column row">
          <div class="center aligned nine wide column">
            <br>
            <p> User-selected ACFDs </p>
          </div>
          <div class="five wide right aligned column">
            <h4>Number of ACFDs to display</h4>
            <select v-model="nTuplesACFD" class="ui dropdown">
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
      </div>
    </div>
    <br>
    <div>
      <br>
      <h4 class="ui horizontal divider header">
        <i class="table icon" />
        Problematic Tuples in the Dataset
      </h4>
      <PrintTable url="/datasetProblematicTuples.json" p="In this table we show the tuples that are most affected by the user-selected ACFDs. The column named 'marked' indicates for each tuple how many ACFDs impact it" />
    </div>
    <br>
    <br>
    <div>
      <h4 class="ui horizontal divider header">
        <i class="temperature high icon" />
        Metrics
      </h4>
      <p> Summary of the interesting metrics on the selected ACFDs regarding the input dataset. </p>
      <table class="ui purple table">
        <tbody>
          <tr>
            <td>
              <div class="icon ui button" data-tooltip="It is the percentage of tuples in the dataset involved by the selected ACFDs. The more this value is close to 1, the more tuples are impacted by the unfair dependencies." data-position="top left" data-variation=" fixed very wide">
                <i class="info icon" />
              </div>
              <b>Cumulative Support:</b>
            </td>
            <td>
              <b>{{ pretty(params.cumulativeSupport) }}</b>
              <i v-if="show_support" class="exclamation red icon" />
            </td>
          </tr>
          <tr>
            <td>
              <div class="icon ui button" data-tooltip="It is the mean of all the ‘Difference’ scores of the selected ACFDs. It indicates how much the dataset is unethical according to the dependencies selected. The greater the value, the higher the bias in the dataset." data-position="top left" data-variation=" fixed very wide">
                <i class="info icon" />
              </div>
              <b>Difference Mean:</b>
            </td>
            <td>
              <b>{{ pretty(params.differenceMean) }}</b>
              <i v-if="show_difference" class="exclamation red icon" />
            </td>
          </tr>
          <tr v-for="(index,item) in params.pDiffs" :key="item">
            <td>
              <div class="icon ui button" data-tooltip="It is the mean of the P-Difference (P is the protected attribute that is analyzed) over all the selected ACFDs. It indicates how much the dataset is ethical over P according to the selected dependencies. The greater the value, the higher the bias in the dataset." data-position="top left" data-variation=" fixed very wide">
                <i class="info icon" />
              </div>
              <b>{{ item }}-Difference Mean:</b>
            </td>
            <td>
              <b>{{ pretty(params.pDiffs[item]) }}</b>
            </td>
          </tr>
          <tr>
            <td>
              <div class="icon ui button" data-tooltip="They are exemplar tuples impacted by the selected ACFDs, this information might be useful in a future phase of bias mitigation." data-position="top left" data-variation=" fixed very wide">
                <i class="info icon" />
              </div>
              <b>Total number of "problematic" tuples:</b>
            </td>
            <td>
              <b>{{ params.totTuplesInterested }}</b>
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
        </tbody>
      </table>
    </div>
    <br>
    <br>
    <div>
      <h4 class="ui horizontal divider header">
        <i class="balance scale icon" />
        More favoured and more discriminated groups
      </h4>
      <p>In this table, given the selected ACFDs, we display the favoured and discrinated protected attribute values of the dataset. </p>
      <table class="ui purple table">
        <tbody>
          <tr>
            <td>
              <b>Attribute:</b>
            </td>
            <td>
              <b>Favoured Groups</b>
              <i class="balance scale left green icon" />
            </td>
            <td>
              <b>Discriminated Groups</b>
              <i class="balance scale right red icon" />
            </td>
          </tr>
          <tr v-for="item in protected_attr" :key="item">
            <td> {{ item }} </td>
            <td> {{ print(params.favoured[item]) }} </td>
            <td> {{ print(params.discriminated[item]) }} </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>

function parseACFD (value) {
  return ' ' + JSON.stringify(value.lhs) + ' => ' + JSON.stringify(value.rhs)
}
export default {
  data () {
    return {
      headers: null,
      data: null,
      show: false,
      nTuplesACFD: 10,
      protected_attr: null,
      params: {
        cumulativeSupport: null,
        differenceMean: null,
        pDiffs: {},
        totTuplesInterested: null,
        totTuples: null,
        favoured: null,
        discriminated: null,
        dataset: 'dataset'
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
    const json = await this.$axios.get('/datasetFinalACFDs.json')
    const obj = json.data
    this.data = obj.data.slice(0, this.nTuplesACFD)
    this.headers = obj.columns
    const jsonMetrics = await this.$axios.get('/datasetMetrics.json')
    const objMetrics = jsonMetrics.data
    this.params.cumulativeSupport = objMetrics.cumulativeSupport
    if (this.params.cumulativeSupport > 0.5) { this.show_support = true }
    this.params.differenceMean = objMetrics.differenceMean
    if (this.params.differenceMean > 0.05) { this.show_difference = true }
    this.params.totTuples = objMetrics.totTuples
    this.params.totTuplesInterested = objMetrics.totTuplesInterested
    this.params.pDiffs = objMetrics.pDiffs
    this.params.favoured = objMetrics.favoured
    this.params.discriminated = objMetrics.discriminated
    const jsonP = await this.$axios.get('/datasetParams.json')
    const objP = jsonP.data
    this.protected_attr = objP.protected_attr
  },
  methods: {
    pretty (value) {
      if (typeof (value) === 'number') {
        return value.toFixed(3)
      } else if (JSON.stringify(value) === 'null') { return 0 } else { return parseACFD(value) }
    },
    print (value) {
      const s = value.toString()
      return s.replace(',', ', ')
    },
    async displayTuples () {
      const json = await this.$axios.get('/datasetFinalACFDs.json')
      const obj = json.data
      this.data = obj.data.slice(0, this.nTuplesACFD)
      this.headers = obj.columns
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
