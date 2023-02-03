<template>
    <h1> 标题：{{ title }} </h1>
    <p>{{ content }}</p>
    <button @click="handle1">按钮</button>
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
    methods:{
        handle(){
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
            handle1:handle1,
        }
    }
})
</script>