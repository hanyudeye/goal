<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <FirstPage></FirstPage>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import FirstPage from './components/FirstPage.vue'

export default {
  name: 'App',
  components: {
    FirstPage
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
  background-color: aquamarine;
}
</style>
