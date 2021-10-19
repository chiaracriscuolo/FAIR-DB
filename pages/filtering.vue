<template>
  <div>
    <div class="container">
      <h4>Choose the ordering criterion</h4>
      <select v-model="orderingCriterion" class="ui selection dropdown">
        <option value="Support">
          Support
        </option>
        <option value="Difference">
          Difference
        </option>
        <!-- TODO <option value="Mean">
          Mean
        </option>-->
      </select>
      <button class="ui purple button" @click="sorted()">
        Apply Ordering Criterion!
      </button>

      <h4>Table of Functional Dependencies</h4>
      <table class="ui purple table">
        <thead>
          <tr>
            <th />
            <th v-for="item in headers" :key="item">
              {{ item }}
            </th>
          </tr>
        </thead><tbody>
          <tr v-for="(el, index) in data" :key="el">
            <td class="collapsing">
              <div class="ui fitted checkbox">
                <input v-model="params" type="checkbox" :value="index"> <label />
              </div>
            </td>
            <td v-for="i in el" :key="i" name="example2">
              <span class="ui black text">{{ pretty(i) }}</span>
            </td>
          </tr>
        </tbody>
      </table>

      <a href="/" aria-current="page" class="nuxt-link-exact-active nuxt-link-active">
        <button class="ui purple button">Compute Statistics!</button>
      </a>
      <a v-if="show" href="/" aria-current="page" class="nuxt-link-exact-active nuxt-link-active">
        <button class="fluid ui purple button">
          See Dependencies!
        </button>
      </a>
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
      orderingCriterion: 'Support',
      params: []
    }
  },
  async mounted () {
    const json = await this.$axios.get('/ACFDsTitanic.json')
    const obj = JSON.parse(json.data)
    this.data = obj.data.slice(0, 10)
    this.headers = obj.columns
  },
  methods: {
    pretty (value) {
      if (typeof (value) === 'number') {
        return value.toFixed(2)
      } else if (JSON.stringify(value) === 'null') { return 0 } else { return parseACFD(value) }
    },
    sorted () {
      return this.data
    }
  }
}
</script>

<style scoped>
</style>
