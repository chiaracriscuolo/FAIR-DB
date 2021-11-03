<template>
  <div>
    <highcharts
      ref="chart"
      class="hc"
      :options="chartOptions"
    />
  </div>
</template>

<script>
export default {
  data () {
    return {
      chartOptions: {
        chart: {
          type: 'column'
        },
        series: [
          {
            data: [1, 2, 3]
          }
        ]
      }
    }
  }
}
</script>
