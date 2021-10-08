.<template>
  <main class="container">
    <h4 class="ui horizontal divider header">
      <i class="table icon" />
      Input Table
    </h4>
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
      <table class="ui definition table">
        <tbody>
          <tr>
            <td class="two wide column">
              <input type="checkbox">
            </td>
            <td>
              Protected attribute 1
            </td>
          </tr>
          <tr>
            <td class="two wide column">
              <input type="checkbox">
            </td>
            <td>
              Protected attribute 2
            </td>
          </tr>
          <tr>
            <td class="two wide column">
              <input type="checkbox">
            </td>
            <td>
              Protected attribute 3
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
              Target class 2
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
      <p>
        The input paramters are ..
      </p>
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
              Maximum Antecendent Size
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
.header{
  background-color: white;
}
</style>
