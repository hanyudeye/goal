<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <!-- <FirstPage></FirstPage> -->
  <!-- <SecondPage></SecondPage> -->
  <!-- <VueTemplate></VueTemplate> -->
  <!-- <KeyBoard></KeyBoard> -->
  <ElePlus></ElePlus>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
// import FirstPage from './components/FirstPage.vue'
// import SecondPage from './components/SecondPage.vue';
// import VueTemplate from './components/VueTemplate.vue';
// import KeyBoard from './components/KeyBoard.vue';
import ElePlus from './components/ElePlus.vue';

export default {
  name: 'App',
  components: {
    // FirstPage,
    // SecondPage,
    // VueTemplate
    // KeyBoard
    ElePlus
  }
}
</script>

<style>
#app1 {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  background-color: aquamarine;
}
</style>
