<template>
    <div class="App">
        <h2>这是一个TODO List</h2>
        <button @click="fn">按钮</button>

        <h3>{{ tips }}</h3>

        <input type="text" name="" id="">
    </div>
</template>


<script lang="js" >
export default {
    setup() {
        const tips = "请输入任务详情"
    },
    methods: {
        fn() {
            alert("hello")
        }
    }, created() {
        console.log("我是created")
    }


}

</script>

<style lang="less" scoped>
.App {
    border: 1px solid #333;
    padding: 20px;

    h2 {
        color: green;
    }

    button {
        background-color: aliceblue;
        padding: 10px;
    }
}
</style>