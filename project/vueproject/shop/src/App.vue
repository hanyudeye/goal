<template>
  <!-- 配置属性 -->
  <div>
    好物数量: {{ GoodproductCount }}
  </div>
  <NavList :sunmenus="menus"></NavList>
  <BarList></BarList>

  <GoodproductList></GoodproductList>

  <!-- 监听事件 -->
  <BaseCount @changeCount="handlechange"></BaseCount>
  <BaseCount></BaseCount>
  <BaseCount></BaseCount>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import NavList from './components/NavList.vue'
import BarList from './components/BarList.vue'
import GoodproductList from './components/GoodproductList.vue'
import BaseCount from './components/BaseCount'

export default {
  name: 'App',
  components: {
    // HelloWorld
    NavList,
    BarList,
    GoodproductList,
    BaseCount
  }, data() {
    return {
      menus: ['首页', '鸡蛋', '鸭蛋', '鹅蛋'],
      // 好物数量
      GoodproductCount: ''
    }
  }, methods: {

    // 提供处理函数
    handlechange(count) {
      this.GoodproductCount = count;
      // console.log(count)
    }
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
