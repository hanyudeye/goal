// 使用 apply 方法通过不同参数 调用函数

function getMaxNum() {
    return arguments[0];
}

ret = getMaxNum.apply("helo", [3, 2, 4])
// console.log(ret)

// 浮点分析
var price = parseFloat("32.3a41f")
// console.log(price)

// 捕捉错误
try {
    badfunction()
    console.log("a")
} catch (e) {
    console.log(e)
    console.log("b")
}

// 字符集 
// 支持显示的文字 
// Unicode 全球文字

console.log("hello\u0020world")


//字符串操作
console.log("hello".concat(" world").toUpperCase());