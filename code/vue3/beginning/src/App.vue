<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <FirstPage></FirstPage>
  <SecondPage></SecondPage>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import FirstPage from './components/FirstPage.vue'
import SecondPage from './components/SecondPage.vue';

export default {
  name: 'App',
  components: {
    FirstPage,
    SecondPage
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
