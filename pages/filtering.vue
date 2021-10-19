<template>
  <div>
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
          <tr v-for="el in data" :key="el">
            <td class="collapsing">
              <div class="ui fitted checkbox">
                <input v-model="params[el]" type="checkbox"> <label />
              </div>
            </td>
            <td v-for="i in el" :key="i" type="number" @="setTwoNumberDecimal(i)">
              {{ i }}
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
export default {
  data () {
    return {
      headers: null,
      data: null,
      show: false,
      params: {}
    }
  },
  async mounted () {
    const json = await this.$axios.get('/ACFDsTitanic.json')
    const obj = JSON.parse(json.data)
    this.data = obj.data.slice(0, 10)
    this.headers = obj.columns
  }
}
</script>

<style scoped>

</style>
