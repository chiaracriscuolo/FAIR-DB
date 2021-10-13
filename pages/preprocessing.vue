.<template>
  <main class="container">
    <h4 class="ui horizontal divider header">
      <i class="table icon" />
      Input Table
    </h4>
    <PrintTable />
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
      <PrintAttributes />
    </div>

    <!-- Target class div -->
    <div class="container">
      <h4 class="ui horizontal divider header">
        <i class="bar chart icon" />
        Select ONE binary target class
      </h4>
      <PrintTarget />
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
              <input id="confidence" v-model="params.Confidence" type="text" placeholder="0.8">
            </td>
          </tr>
          <tr>
            <td class="two wide column">
              Support {{ params.Support }}
            </td>
            <td>
              <input id="support" v-model="params.Support" type="text" placeholder="0.1">
            </td>
          </tr>
          <tr>
            <td class="two wide column">
              Maximum Antecendent Size
            </td>
            <td>
              <input id="maxAntSize" v-model="params.MaxAntSize" type="text" placeholder="2">
            </td>
          </tr>
          <tr>
            <td class="two wide column">
              Difference
            </td>
            <td>
              <input id="difference" v-model="params.Difference" type="text" placeholder="0.1">
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="container">
      <!--<a href="/api/filtering" aria-current="page" class="nuxt-link-exact-active nuxt-link-active">
          <button class="fluid ui purple button">Compute Dependencies!</button>
        </a>-->
      <button class="fluid ui purple button" @click="postParams()">
        Compute Dependencies!
      </button>
    </div>
  </main>
</template>

<script>
import axios from 'axios'
export default {

  data () {
    return {
      params: {
        Support: null,
        Difference: null,
        Confidence: null,
        MaxAntSize: null
      }
    }
  },
  methods: {
    postParams () {
      // console.warn(this.params)
      // axios.post('/api/postParams', this.params)
      axios.get('/api/preprocessingApi')
        .then(function (response) {
          // Handle success
          console.log('successo')
        })
    }

  }
}
</script>

<style scoped>
.header{
  background-color: white;
}
</style>
