<template>
  <div>
    <ul>
      <li v-for="tab in tabs">{{ tab }}</li>
    </ul>

    <label>日期：{{ Date() }}</label>
  </div>
  <p>{{ content }}</p>
  <button @click="handle1">按钮</button>
  <label for="">标签的使用</label>

  {{ 1+1 }}{{ [1, 3, 5] }}{{ { name: "aming", age: 36 } }}{{ "helo" | toUpper}}

  <label for="">数组的使用 </label>
  <ul>
    <li v-for="f in furniture">{{ f }}</li>
  </ul>

 <h2>指令的用法</h2> 
显示或隐藏 <a v-if="true">显示链接</a> <a v-if="false">隐藏连接</a>
<div @click="handle">按钮</div>


<h2>表单的用法</h2>

  <form action="">
    <div class="form-group">
      <label >名字的值是 {{ name }}</label>
      <input type="text" v-model="name" class="form-control" @blur="updatename(this)">



    </div>
  </form>
</template>

<script>

import { defineComponent } from 'vue';

export default defineComponent({
  name: "home",
  methods: {
    handle() {
      console.log("handle1");
    }
  },
  setup() {

    const handle1 = () => {
      console.log("handle");
    };

    const toUpper = () => {
      content.toUpperCase();
      // console.log("hello".toUpperCase())
    };

    const updatename=()=>{
      // ;
      console.log("fuck")
    }
    //这里是数据
    return {
      name:"名字",
      tabs: ["1:browser</br>", "2:document", "3:shell"],
      title: "我是标题",
      content: "lorem lorem",
      furniture: ["电视", "冰箱", "沙发"],
      handle1: handle1,
      toUpper: toUpper,
      updatename:updatename
    }
  }
})
</script>