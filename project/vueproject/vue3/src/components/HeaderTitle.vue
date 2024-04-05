<template>
    <h1>
        这里是头部
    </h1>

    <h2>a 的值是 {{ a }}</h2>

</template>

<script>
export default {
    setup() {
        return {
            a: 1,
            b: 2
        }
    }
}
</script>