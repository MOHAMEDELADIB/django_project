<template>
  <div class="container mt-5 text-center">
    <GoogleChart />
   </div>
</template>

<script>
import GoogleChart from './components/GoogleChart.vue'

export default {
  name: 'App',
  components: {
    GoogleChart
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
