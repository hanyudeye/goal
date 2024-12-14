// 六种基本数据类型：Undefined，Null，Boolean，Number，String，Symbol ( ES 6新增 )；
// 一种引用数据类型：统称为 Object 类型；具体又细分为 Object，Array，Date，RegExp，Function 等类型。另外和 Java 语言类似，对于布尔，数值，字符串等基本类型，分别存在其对应的包装类型 Boolean，Number，String，但通常我们并不会使用到这些包装类型，只需要使用其基本类型即可。

// a=[]
// a[0]=323
// a[1]="1abc"
// a.forEach((element,index,w)=> {
//    console.log(element,index,w) 
// });


let 小兔子 = "小兔子"
小兔子 += " 笨笨"


// for(let i=0;i<小兔子.length;i++){
//    setTimeout(()=>{
//       console.log(小兔子[i])
//    },1000 *(i+1))
// }

let countries = ['USA', 'US', "AUS", "UK", "CHINA", "JAPAN", "KOREA", "INDIA", "TAIWAN", "HONGKONG", "MACAO"]

countries.push('NEWZLAND')
// countries= countries.join(',')

// console.log(countries)

// countries.forEach((element, index) => {
//     console.log(element)
// })


// 数字的进制表示;进制显示
// console.log(56);
// console.log(0o70);
// console.log(0x38);

设置 - 特色功能 - 极简模式