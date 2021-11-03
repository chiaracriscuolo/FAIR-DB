.<template>
  <main class="container">
    <!-- STEPS -->
    <div class="ui  ordered steps">
      <a class="completed link step" href="/import">
        <div class="content">
          <div class="title">Import Dataset</div>
          <!--<div class="description">Select the dataset</div>-->
        </div>
      </a>
      <a class="active step" href="/preprocessing">
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
    <h4 class="ui horizontal divider header">
      <i class="table icon" />
      Input Dataset
    </h4>
    <PrintTable />
    <!-- TO DO: DATA VISUALIZATION
    <div class="container">
      <h4 class="ui horizontal divider header">
        <i class="chart area icon" />
        Data Visualization
      </h4>
      <div v-for="(item) in headers" :key="item" class="ui grid">
        <div class="four wide column">
          <input v-model="params.visualize_attribute" type="button" class="ui purple button">
          {{ item }}
        </div>
      </div>
    </div> -->
    <!-- Protected attribute div -->
    <div class="container">
      <h4 class="ui horizontal divider header">
        <i class="bar chart icon" />
        Select one or more protected attributes
      </h4>
      <p>
        Protected attributes could be qualities, traits or characteristics that, by law, should not be discriminated against (for example sex or native country)
      </p>
      <table class="ui definition table">
        <tbody>
          <tr v-for="(item) in headers" :key="item">
            <td class="two wide column">
              <input v-model="params.protected_attr" :value="item" type="checkbox">
            </td>
            <td>
              {{ item }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Target class div -->
    <div class="container">
      <h4 class="ui horizontal divider header">
        <i class="bar chart icon" />
        Select ONE binary target class
      </h4>
      <p>The target is whatever the output of the input variables</p>
      <table class="ui definition table">
        <tbody>
          <tr v-for="(item) in headers" :key="item">
            <div class="field">
              <div type="ui radio checkbox">
                <td class="two wide column">
                  <input v-model="params.target" type="radio" :value="item" name="example2">
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
    <highchart :options="chartOptions" />

    <!-- INPUT PARAMETERS CONTAINER -->
    <div class="container">
      <h4 class="ui horizontal divider header">
        <i class="bar chart icon" />
        Input Parameters
      </h4>
      <p>
        The algorithm takes four mandatory inputs paramters: the confidence leeway threshold, the minimum support count threshold, the maximum antecedent size of the discovered ACFDs and the minimum difference threshold.
      </p>
      <table class="ui definition table">
        <tbody>
          <tr>
            <td class="two wide column">
              Confidence
            </td>
            <td>
              <input id="confidence" v-model.number="params.confidence" type="text" placeholder="0.8">
            </td>
          </tr>
          <tr>
            <td class="two wide column">
              SupportCount
            </td>
            <td>
              <input id="supportCount" v-model.number="params.supportCount" type="text" placeholder="80">
            </td>
          </tr>
          <tr>
            <td class="two wide column">
              Maximum Antecendent Size
            </td>
            <td>
              <input id="maxAntSize" v-model.number="params.maxAntSize" type="text" placeholder="2">
            </td>
          </tr>
          <tr>
            <td class="two wide column">
              Difference
            </td>
            <td>
              <input id="difference" v-model.number="params.difference" type="text" placeholder="0.07">
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="container">
      <!--<a href="/api/filtering" aria-current="page" class="nuxt-link-exact-active nuxt-link-active">
          <button class="fluid ui purple button">Compute Dependencies!</button>
        </a>-->
      <button v-if="show_compute" class="ui purple button" @click="postParams()">
        Compute Dependencies!
      </button>
      <div v-if="show_loading" class="ui purple bottom attached loading tab">
        The process will take few seconds
      </div>
    </div>
    <div class="container">
      <a v-if="show_next" href="/filtering" aria-current="page" class="nuxt-link-exact-active nuxt-link-active">
        <button class="fluid ui purple button">
          See Dependencies!
        </button>
      </a>
    </div>
  </main>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      headers: null,
      show_compute: true,
      show_next: false,
      show_loading: false,
      visualize_attribute: 'Survived',
      params: {
        protected_attr: [],
        target: 'Survived',
        confidence: 0.8,
        supportCount: 80,
        maxAntSize: 2.0,
        difference: 0.07,
        dataset: 'Titanic'
      },
      chartOptions: {
        series: [
          {
            data: [1, 2, 3]
          }
        ]
      }
    }
  },
  async mounted () {
    const json = await this.$axios.get('/dataTitanic.json')
    const obj = json.data
    this.headers = obj.columns
  },
  methods: {
    async postParams () {
      // console.warn(this.params)
      // const self = this
      this.show_loading = true
      this.show_compute = false
      const response = await axios.post('/api/preprocessing/postParams', this.params)
      // axios.get('/api/preprocessingApi')
      // .then(function (response) {
      // Handle success
      // this.$router.push('/filtering')
      console.log('----------', response.body)
      this.show_loading = false
      this.show_next = true
      // response.redirect('/filtering')
      // })
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
