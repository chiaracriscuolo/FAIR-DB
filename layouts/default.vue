<!-- THE DEFAULT STYLE -->
<template>
  <div>
    <the-header />
    <Nuxt />
    <the-footer />
  </div>
</template>

<script>
import TheHeader from '~/components/TheHeader.vue'
import TheFooter from '~/components/TheFooter.vue'
export default {
  components: {
    TheHeader,
    TheFooter
  }
}
</script>

<style>
html {
  font-family: Lato,'Helvetica Neue',Arial,Helvetica,sans-serif;;
  box-sizing: border-box;
}

*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
}
.container {
  padding: 10px;
  margin: 40px auto;
  max-width: 800px;
  text-align: center;
}
a {
  color: white;
}
img {
  width: 100%;
}
button{
  transition: all 0.2s ease-in-out;
}
.fluid.ui.purple.button:hover{
  background-color: lightsalmon;
  color: white;
}
.ui.purple.button:hover{
  background-color: lightsalmon;
  color: white;
}
</style>
