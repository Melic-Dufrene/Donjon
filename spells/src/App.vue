<template>
  <div id="app">
    <Spellsearch />
  </div>
</template>

<script>
import Spellsearch from './components/Spellsearch.vue'

export default {
  name: 'App',
  components: {
    Spellsearch
  }
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
