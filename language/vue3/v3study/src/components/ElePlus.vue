<!-- 注意：显示组件要放在 template 元素里面 -->
<template>
  这是一个 element-plus 页面
  <el-button>Elebutton</el-button>
</template>

<script>
import { ElButton } from 'element-plus';
export default {
  name: 'ElePlus',
  data: function () {
    return {
      count: 3

    }
  }, components: {
    ElButton
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