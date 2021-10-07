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
    <!-- Protected attribute div -->
    <div class="container">
      <h4 class="ui horizontal divider header">
        <i class="bar chart icon" />
        Protected attributes
      </h4>
      <table class="ui definition table">
        <tbody>
          <tr>
            <td class="two wide column">
              <input type="checkbox">
            </td>
            <td>
              P attr 1
            </td>
          </tr>
          <tr>
            <td class="two wide column">
              <input type="checkbox">
            </td>
            <td>
              P attr 2
            </td>
          </tr>
          <tr>
            <td class="two wide column">
              <input type="checkbox">
            </td>
            <td>
              P attr 3
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Protected attribute div -->
    <div class="container">
      <h4 class="ui horizontal divider header">
        <i class="bar chart icon" />
        Select one target class
      </h4>
      <table class="ui definition table">
        <tbody>
          <tr>
            <td class="two wide column">
              <input type="checkbox">
            </td>
            <td>
              Target class 1
            </td>
          </tr>
          <tr>
            <td class="two wide column">
              <input type="checkbox">
            </td>
            <td>
              Target Class 2
            </td>
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
