<template>
    <div class="demo">
        <h2>学校名称: {{ schoolName }}</h2>
    </div>
</template>

<script>
export default {
    name: 'ThirdPage',
    data() {
        return {
            schoolName: "小学"
        }
    }
}
</script>

<style>
/* 组件的样式 */
.demo {
    background-color: antiquewhite;
}
</style>

