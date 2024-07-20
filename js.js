// console.log(Array.prototype.indexOf('\n'))

// 嵌入函数
// let text=`
// <p>
// ${new Date().getFullYear()}
// </p>
// `;

// console.log(text);

let fengshan = {
    挡位: [0, 1, 2, 3],
    是否摇头: [false, true],
    叶片: 3,
    罩子: {
        电机功率: "220w",
        电压: "220v",
        电机大小: "15cm"
    }
};


function 默认参数(p = fengshan) {
    console.log(`挡位是 ${p.挡位} and 电机电压是 ${p.罩子.电压}`);
}

// 默认参数();

// 箭头函数

var 箭头函数 = args => {
    console.log(`我是箭头函数  ${args}`)
}

// 箭头函数("hello")

// 还起到 省略 return 的效果

var 箭头函数1=args=>`参数是 ${args}`
// console.log(箭头函数1("hello"));



