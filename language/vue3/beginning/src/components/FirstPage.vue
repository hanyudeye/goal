<!-- 注意：显示组件要放在 template 元素里面 -->
<template>
  <div class="FirstPage" @click="showmsg()">
    这是 page1
    <br>
    当前的计数是: {{ count }}

  </div>
  <button @click="add()">累加</button>
</template>

<script>
export default {
  name: 'FirstPage',
  data: function () {
    return {
      count: 3

    }
  },
  methods: {

    showmsg() {
      alert("hello")
    },

    add() {
      this.count++;
    }


  }
}
</script>

<style>
.FirstPage {
  background-color: khaki;
}
</style>