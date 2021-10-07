.<template>
  <main class="container">
    Show Table
    <div class="container">
      Statistics Distribution
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
    <div class="container">
      <h4 class="ui horizontal divider header">
        <i class="bar chart icon" />
        Input Paramenters
      </h4>
      <td class="collapsing">
        <div class="ui fitted slider checkbox">
          <tbody>
            <tr>
              <td class="two wide column">
                <input type="checkbox">
                <label />
              </td>
              <td>
                Protected Attribute 1
              </td>
            </tr>
            <input type="checkbox"> Protected Attribute 2<label />
            <input type="checkbox"> Protected Attribute 3<label />
            <input type="checkbox"> Target Class 1<label />
            <input type="checkbox"> Target Class 2<label />
          </tbody>
        </div>
      </td>
    </div>
    <div class="container">
      <table class="ui definition table">
        <tbody>
          <tr>
            <td class="two wide column">
              Confidence
            </td>
            <td>
              <input type="text" placeholder="0.8">
            </td>
          </tr>
          <tr>
            <td class="two wide column">
              Support
            </td>
            <td>
              <input type="text" placeholder="0.1">
            </td>
          </tr>
          <tr>
            <td class="two wide column">
              maxAntecendentSize
            </td>
            <td>
              <input type="text" placeholder="2">
            </td>
          </tr>
          <tr>
            <td class="two wide column">
              Difference
            </td>
            <td>
              <input type="text" placeholder="0.1">
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="container">
      <a href="/filtering" aria-current="page" class="nuxt-link-exact-active nuxt-link-active">
        <button class="fluid ui purple button">Compute Dependencies!</button>
      </a>
    </div>
  </main>
</template>

<script>
export default {}
</script>

<style scoped>
</style>
