<template>
    <div class="SecondPage">
        <div>链接属性
            <div v-html="link"></div>
        </div>
        这是 page2
    </div>
</template>

<script>
export default {
    name: "SecondPage",
    data:function(){
        return{
            link:'<a href="http://a.com">链接</a>'
        }
    }
}
</script>

<style>
.SecondPage {
    background-color: darkgray;
    margin-top: 1em;
}
</style>