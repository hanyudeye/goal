import { checkPhone,checkCode } from "./utils/check.js";

//1. 写入代码
console.log(checkCode('1231334'))
console.log(checkPhone('1231334'))

console.log("hhhhhh")
//2. 准备 webpack 打包环境
// "build":"webpack"
// 运行自定义命令 npm run build

document.querySelector('.btn').addEventListener('click',()=>{

    const phone=document.querySelector("#phone").value
    const code=document.querySelector("[name=code]").value

    if(!checkPhone(phone)) {
        console.log("手机号长度必要要 11位")
        return
    }

    if(!checkPhone(code)) {
        console.log("验证码长度必要要 6位")
        return
    }

    console.log('提交到服务器')

});