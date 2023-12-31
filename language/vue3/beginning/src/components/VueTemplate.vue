<!-- 注意：显示组件要放在 template 元素里面 -->
<template>
  <div class="VueTemplate">
    <h1>Vue模板用法：</h1>
    <div>1. 今年是： {{ riqi }}</div>
    <div>2. 开关判断:
      <span v-if="kaiguan">开</span>
      <span v-else>关</span>
    </div>
    <div>3. 循环遍历 动物们</div>
    <ul>
      <li v-bind:key="index" v-for="(item,index) in animals">{{ index+1 }}:{{ item }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'VueTemplate',
  data() {
    return {
      count: 3,
      riqi: new Date().getFullYear(),
      kaiguan: 0,
      animals: ['鸡', '老虎', '狮子', '大象']

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
.VueTemplate {
  background-color: gray;
  border: 1px solid red;
  width: 50%;
}
</style>