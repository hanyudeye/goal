<template>
    <div>

        <button @click="minus">-</button>
        <span>{{ count }}</span>
        <button @click="add">+</button>

    </div>

</template>

<script>

export default {


    data() {
        return {
            count: 99
        }
    }, methods: {
        add() {
            this.count++;
            // 发送消息
            this.$emit('changeCount', this.count)
        },
        minus() {
            this.count--;
            // 发送消息
            this.$emit('changeCount', this.count)
        }
    }
}

</script>

<style scoped>
div {
    margin-bottom: 20px;
}

button {
    padding: 10px;
    font-size: 30px;
    width: 50px;
}

span {
    padding: 20px;
    width: 50px;
    font-size: 30px;
}
</style>