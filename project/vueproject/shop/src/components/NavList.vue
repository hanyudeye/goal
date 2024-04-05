<template>
    <h1>导航</h1>
    <ul>
        <li v-for="item in menus" :key="item">{{ item }}</li>
    </ul>

    <h3>副导航</h3>
    <ul class="sunmenus">
        <li v-for="item in sunmenus" :key="item">{{ item }}</li>
    </ul>

</template>

<script>
export default {
    // data是一个函数，当组件实例化后，可以数据间不冲突
    data() {
        return {
            menus: ['首页', '博客', '新闻', '关于', '招聘']
        }
        //引入属性，类型校验
    }, 
    // props: { sunmenus: Array}
    // 校验完整写法
    props:{
        sunmenus:{
            type:Array,
            required:true, //必传
            // default:0
            //自定义校验
            validator(value){
                // if(value)
                console.log(value)
                //校验正确，返回 true
                return true
            }
        }
    }

}


</script>

<!-- 样式局部化 ,原理是添加了 data-v-hash 值-->
<style scoped>
div {
    background-color: aquamarine;
}

ul {
    margin: 0;
    padding: 0;
}

li {
    list-style: none;
    display: inline-block;
    margin-right: 10px;
    padding: 5px;
    border: 1px solid gray;
    margin-top: 20px;
    margin-bottom: 20px;
}

.sunmenus {
    background-color: aquamarine;
}
</style>