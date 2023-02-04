<template>
  <h1> 标题：{{ title }} </h1>
  <p>{{ content }}</p>
  <button @click="handle1">按钮</button>

  <label for="">数组的使用</label>
  <ul>
    <li v-for="f in furniture">{{ f }}</li>
  </ul>

  <form action="">
    <div class="form-group">
      <label for="">名字</label>
      <input type="text" name="name" class="form-control" placeholder="请输入名字">
    </div>
  </form>
</template>

<script>

import { defineComponent } from 'vue';

export default defineComponent({
  name: "home",
  // data 是 vue2 中方法 
  // data() {
  // return {
  //     title: "我是标题",
  //     content:"lorem lorem"
  // },
  // },
  methods: {
    handle() {
      console.log("handle1");
    }
  },
  setup() {

    const handle1 = () => {
      console.log("handle");
    };

    //这里是数据
    return {
      title: "我是标题",
      content: "lorem lorem",
      furniture: ["电视", "冰箱", "沙发"],
      handle1: handle1,
    }
  }
})
</script>