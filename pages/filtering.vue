<template>
  <div>
    <print-table />
    <div class="container">
      <a href="/" aria-current="page" class="nuxt-link-exact-active nuxt-link-active">
        <button class="fluid ui purple button">Compute Statistics!</button>
      </a>
    </div>
  </div>
</template>

<script>
import PrintTable from '../components/PrintTable.vue'

export default {
  components: {
    PrintTable
  }
}
</script>

<style scoped>

</style>
