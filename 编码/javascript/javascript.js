// 使用 apply 方法通过不同参数 调用函数

function getMaxNum(){
    return arguments[0];
}

ret=getMaxNum.apply("helo",[3,2,4])
console.log(ret)

  