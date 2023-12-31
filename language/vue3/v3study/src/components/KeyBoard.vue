<template>
  我是一个键盘

  <div class="key">
    <div @click="a()">A</div>
    <div @click="b()">B</div>
    <div>C</div>
    <div>D</div>
    <div>E</div>
    <div>{{ key }}</div>
  </div>

  <div class="form">
    姓名: <input type="text" name="" v-model="input_value">
  </div>
</template>

<script>
export default {
  name: 'KeyBoard',
  data: function () {
    return {
      link: '<a href="http://a.com">链接</a>',
      key: 'KEY',
      input_value: "小李"
    }
  }, methods: {
    a: function () { alert("hello") },
    b: function () { alert("mes") }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.key div {
  width: 30px;
  height: 20px;
  color: #42b983;
  border: 1px solid grey;
  text-align: center;
  line-height: 20px;
  margin: 5px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
