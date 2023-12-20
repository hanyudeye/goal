<<<<<<< HEAD
<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>

export default {
  name: 'app',
  components: {
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
body {
  margin: 0;
  background: #f3f6f8;
}
</style>
=======
<template>
  <div id="app">
    <router-view></router-view>
    <Test></Test>
  </div>
</template>

<script>
import Test from './components/Test.vue';


export default {
  name: 'app',
  components: {
    Test
}
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
body {
  margin: 0;
  background: #f3f6f8;
}
</style>
>>>>>>> 1a0c6d66e3606d60229f5a0cab58b4f83be294d9
