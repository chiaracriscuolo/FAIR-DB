.<template>
  <main class="container">
    <h4 class="ui horizontal divider header">
      <i class="table icon" />
      Input Table
    </h4>
    <PrintTable />
    <!-- TO DO: DATA VISUALIZATION -->
    <div class="container">
      <h4 class="ui horizontal divider header">
        <i class="chart area icon" />
        Data Visualization
      </h4>
      <div class="ui grid">
        <div class="four wide column">
          <button class="ui purple button">
            Attribute 1
          </button>
        </div>
        <div class="four wide column">
          <button class="ui purple button">
            Attribute 2
          </button>
        </div>
        <div class="four wide column">
          <button class="ui purple button">
            Attribute 3
          </button>
        </div>
        <div class="four wide column">
          <button class="ui purple button">
            Attribute 4
          </button>
        </div>
      </div>
    </div>
    <!-- Protected attribute div -->
    <div class="container">
      <h4 class="ui horizontal divider header">
        <i class="bar chart icon" />
        Select one or more protected attributes
      </h4>
      <p>
        A protected attribute is a ..
      </p>
      <div class="container">
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
    </div>

    <!-- Target class div -->
    <div class="container">
      <h4 class="ui horizontal divider header">
        <i class="bar chart icon" />
        Select ONE binary target class
      </h4>
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

    <!-- INPUT PARAMETERS CONTAINER -->
    <div class="container">
      <h4 class="ui horizontal divider header">
        <i class="bar chart icon" />
        Input Parameters
      </h4>
      <p>
        The input parameters are ..
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
              Support
            </td>
            <td>
              <input id="support" v-model.number="params.support" type="text" placeholder="0.1">
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
      <button class="ui purple button" @click="postParams()">
        Compute Dependencies!
      </button>
    </div>
    <div class="container">
      <a v-if="show" href="/filtering" aria-current="page" class="nuxt-link-exact-active nuxt-link-active">
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
      show: false,
      params: {
        protected_attr: [],
        target: 'Survived',
        confidence: 0.8,
        support: 0.1,
        maxAntSize: 2,
        difference: 0.07
      }
    }
  },
  async mounted () {
    const json = await this.$axios.get('/dataTitanic.json')
    const obj = JSON.parse(json.data)
    this.headers = obj.columns
  },
  methods: {
    async postParams () {
      // console.warn(this.params)
      // const self = this
      const response = await axios.post('/api/postParams', this.params)
      // axios.get('/api/preprocessingApi')
      // .then(function (response) {
      // Handle success
      // this.$router.push('/filtering')
      console.log('----------', response.body)
      this.show = true
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
