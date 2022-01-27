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
      <a class="active step" href="/preprocessing-census">
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
    <PrintTable url="/USCensus.json" p="A few tuples from the input dataset" />
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

    <!--<div class="required field">
        <label>Last name</label>
        <input type="text" placeholder="Full Name">
      </div>-->
    <div class="container">
      <h4 class="ui horizontal divider header">
        <i class="bar chart icon" />
        Select one or more protected attributes
      </h4>
      <p>
        A protected attribute is a characteristic for which non-discrimination should be established, like age, race, sex, etc.
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
      <p>The target is the feature of a dataset about which the user wants to gain a deeper understanding, for example the income, or a boolean label that indicates whether a loan is authorized or not,  etc. It must be binary.</p>
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
        The algorithm takes four mandatory input parameters: the confidence leeway threshold, the minimum support count threshold, the maximum antecedent size of the discovered ACFDs and the minimum difference threshold. To best choose the values, we suggest to perform a preliminary data exploration to understand the general distribution of the values and detect, if present, possible minorities
      </p>
      <table class="ui definition table">
        <tbody>
          <tr>
            <td class="five wide column">
              <div class="icon ui button" data-tooltip="This parameter shows how frequently the dependency X->Y is verified knowing that X is verified. It can assume values in the range [0, 1]. The higher this value is, higher is the probability that the dependency is verified." data-position="top left" data-variation=" fixed very wide">
                <i class="info icon" />
              </div>
              ACFD Confidence threshold
            </td>
            <td class="five wide column">
              <input id="confidence" v-model.number="params.confidence" type="text" placeholder="0.8">
            </td>
          </tr>
          <tr>
            <td class="five wide column">
              <div class="icon ui button" data-tooltip="The support count is the number of the samples in the dataset that verifies the dependency X->Y and it can assume values in the range [0, dataset-lenght]. It defines how many samples should be seen in order to consider a dependency as a valid one. We suggest to put it lower than the cardinality of the groups that you want to study." data-position="top left" data-variation=" fixed very wide">
                <i class="info icon" />
              </div>
              ACFD SupportCount threshold
            </td>
            <td class="five wide column">
              <input id="supportCount" v-model.number="params.supportCount" type="text" placeholder="10">
            </td>
          </tr>
          <tr>
            <td class="five wide column">
              <div class="icon ui button" data-tooltip="It is the maximum antecedent size of a dependency X->Y, so the maximum number of attributes that can compare in X. It should be in the range between 1 and the number of chosen protected attributes." data-position="top left" data-variation=" fixed very wide">
                <i class="info icon" />
              </div>
              Maximum Antecendent Size
            </td>
            <td class="five wide column">
              <input id="maxAntSize" v-model.number="params.maxAntSize" type="text" placeholder="2">
            </td>
          </tr>
          <tr>
            <td class="five wide column">
              <div class="icon ui button" data-tooltip="It indicates how much a dependency is ‘unethical’, it is the difference between the confidence(X->Y) and the confidence computed without the protected attributes in X. It can assume values in the range [0, 1]. To detect ethical problems we suggest to put it very low as 0.05 and perform some tests to tune it according to the ACFDs found." data-position="top left" data-variation=" fixed very wide">
                <i class="info icon" />
              </div>
              Difference threshold
            </td>
            <td class="five wide column">
              <input id="difference" v-model.number="params.difference" type="text" placeholder="0.07">
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div>
      <!-- INPUT VALIDATION -->
      <p v-if="!formIsValid" class="ui message">
        <b>Please correct the following error(s):</b>
        <ul>
          <li v-if="!protectedAttributesAreValid">
            Protected Attributes are required! They should not contain the target class
          </li>
          <li v-if="!targetIsValid">
            Target Attribute is required! (It should be binary)
          </li>
          <li v-if="!confidenceIsValid">
            Confidence  > 0 is required
          </li>
          <li v-if="!supportCountIsValid">
            Support Count  > 0 is required
          </li>
          <li v-if="!differenceIsValid">
            Difference  > 0 is required
          </li>
          <li v-if="!maxSizeAntIsValid">
            Maximum Antecedent Size  > 0 is required
          </li>
        </ul>
      </p>
    </div>

    <div class="container">
      <button v-if="show_compute" class="ui purple button" @click="postParams()">
        Compute Dependencies!
      </button>
      <div v-if="show_loading" class="ui purple bottom attached loading tab">
        The process will take a few seconds
      </div>
    </div>
    <div class="container">
      <a v-if="show_next" href="/filtering-census" aria-current="page" class="nuxt-link-exact-active nuxt-link-active">
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
      errors: [],
      headers: null,
      show_compute: true,
      show_next: false,
      show_loading: false,
      visualize_attribute: 'income',
      params: {
        protected_attr: ['race', 'sex', 'native-country'],
        target: 'income',
        confidence: 0.8,
        supportCount: 10,
        maxAntSize: 2.0,
        difference: 0.07,
        dataset: 'Census'
      }
    }
  },
  computed: {
    formIsValid () {
      return this.protectedAttributesAreValid && this.targetIsValid && this.confidenceIsValid && this.supportCountIsValid && this.differenceIsValid && this.maxSizeAntIsValid
    },
    protectedAttributesAreValid () {
      return (this.params.protected_attr.length !== 0) && !(this.params.protected_attr.includes(this.params.target))
    },
    targetIsValid () {
      return !(!this.params.target)
    },
    confidenceIsValid () {
      return (!(!this.params.confidence)) && this.params.confidence > 0
    },
    supportCountIsValid () {
      return (!(!this.params.supportCount)) && this.params.supportCount > 0
    },
    differenceIsValid () {
      return (!(!this.params.difference)) && this.params.difference > 0.01
    },
    maxSizeAntIsValid () {
      return (!(!this.params.confidence)) && this.params.maxAntSize > 0
    }
  },
  async mounted () {
    const json = await this.$axios.get('/USCensus.json')
    const obj = json.data
    this.headers = obj.columns
  },
  methods: {
    checkForm (e) {
      if (this.params.confidence && this.params.supportCount && this.params.difference && this.params.maxAntSize) {
        return true
      }

      this.errors = []

      if (!this.params.confidence) {
        this.errors.push('Confidence required.')
      }
      if (!this.params.supportCount) {
        this.errors.push('Support Count required.')
      }
      if (!this.params.difference) {
        this.errors.push('Difference required.')
      }
      if (!this.params.maxAntSize) {
        this.errors.push('Max Antecedent Size required.')
      }

      e.preventDefault()
    },
    async postParams () {
      // console.warn(this.params)
      // const self = this
      this.show_loading = true
      this.show_compute = false
      await axios.post('/api/preprocessing/postParams', this.params)
      // axios.get('/api/preprocessingApi')
      // .then(function (response) {
      // Handle success
      // this.$router.push('/filtering')
      // console.log('----------', response.body)
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
