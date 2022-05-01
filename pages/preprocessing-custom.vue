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
      <a class="active step" href="/preprocessing-custom">
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
    <PrintTable url="/dataset.json" p="A few tuples from the input dataset" />
    <!-- TO DO: DATA VISUALIZATION
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
    </div>-->
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
                  <input v-model="params.target" type="radio" :value="item" name="example2" @click="getTargetValues(item)">
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

    <!-- Target class values div -->
    <div v-if="show_targetValues" class="container">
      <h4 class="ui horizontal divider header">
        <i class="bar chart icon" />
        Select one target class value
      </h4>
      <p>You should select the negative value that indicates discrimination</p>
      <table class="ui definition table">
        <tbody>
          <tr v-for="(i) in targetValues" :key="i">
            <div class="field">
              <div type="ui radio checkbox">
                <td class="two wide column">
                  <input v-model="params.negativeTargetValue" type="radio" :value="i" name="example3">
                </td>
                <td>
                  {{ i }}
                </td>
              </div>
            </div>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- INPUT PARAMETERS CONTAINER -->
    <div class="container">
      <p v-if="errors.length">
        <b>Please correct the following error(s):</b>
        <ul>
          <li v-for="error in errors" :key="error.id">
            {{ error }}
          </li>
        </ul>
      </p>
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
              <input id="confidence" v-model.number="params.confidence" type="text">
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
              <input id="supportCount" v-model.number="params.supportCount" type="text">
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
              <input id="maxAntSize" v-model.number="params.maxAntSize" type="text">
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
              <input id="difference" v-model.number="params.difference" type="text">
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="container">
      <p v-if="!formIsValid" class="ui error message">
        <b>Please correct the following error(s):</b>
        <ul>
          <li v-if="!protectedAttributesAreValid">
            Protected Attributes are required! They should not contain the target class
          </li>
          <li v-if="!targetIsValid">
            Target Attribute is required! (It should be binary)
          </li>
          <li v-if="!confidenceIsValid">
            Confidence greater than 0 and less than 1 is required
          </li>
          <li v-if="!supportCountIsValid">
            Support Count greater than 0 and less than the dataset length is required
          </li>
          <li v-if="!differenceIsValid">
            Difference greater than 0 and less than 1 is required
          </li>
          <li v-if="!maxSizeAntIsValid">
            Maximum Antecedent Size  greater than 0 is required
          </li>
        </ul>
      </p>
    </div>
    <div class="container">
      <button v-if="show_compute" class="ui purple button" :disabled="!formIsValid" @click="postParams()">
        Compute Dependencies!
      </button>
      <div v-if="show_loading" class="ui purple bottom attached loading tab">
        The process will take a few seconds
      </div>
    </div>
    <div class="container">
      <a v-if="show_next" href="/filtering-custom" aria-current="page" class="nuxt-link-exact-active nuxt-link-active" @click="checkForm()">
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
      show_targetValues: false,
      targetValues: [],
      params: {
        protected_attr: [],
        target: null,
        confidence: null,
        supportCount: null,
        maxAntSize: null,
        difference: null,
        negativeTargetValue: null,
        dataset: 'dataset'
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
      return (!(!this.params.confidence)) && this.params.confidence > 0 && this.params.confidence < 1
    },
    supportCountIsValid () {
      return (!(!this.params.supportCount)) && this.params.supportCount > 0
    },
    differenceIsValid () {
      return (!(!this.params.difference)) && this.params.difference > 0.01 && this.params.difference < 1
    },
    maxSizeAntIsValid () {
      return (!(!this.params.confidence)) && this.params.maxAntSize > 0
    }
  },
  async mounted () {
    const json = await this.$axios.get('/dataset.json')
    const obj = json.data
    this.headers = obj.columns
  },
  methods: {
    checkForm () {
      if (this.params.protected_attr && this.params.target && this.params.confidence && this.params.supportCount) {
        return true
      }

      this.errors = []

      if (!this.params.protected_attr) {
        this.errors.push('Protected attribute required.')
      }
      if (!this.params.target) {
        this.errors.push('Target required.')
      }
      alert(this.errors)
    },
    async getTargetValues (target) {
      if (target != null) {
        const json = await this.$axios.get('/datasetColumnsValues.json')
        // console.log(json.data[target])
        this.targetValues = json.data[target]
        this.show_targetValues = true
        return null
      }
      return null
    },
    async postParams () {
      // console.warn(this.params)
      // const self = this
      this.show_loading = true
      this.show_compute = false
      // const response =
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
