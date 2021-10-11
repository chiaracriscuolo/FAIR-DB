<!-- INPUT PARAMETERS CONTAINER -->
.<template>
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
            Support {{ Support }}
          </td>
          <td>
            <input id="support" v-model="Support" type="text" placeholder="0.1">
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data () {
    return {
      Support: null
    }
  },
  methods: {
    postParams (e) {
      console.warn(this.params)
      e.preventDefault()
    }
  }
}
</script>

<style scoped>
.header{
  background-color: white;
}
