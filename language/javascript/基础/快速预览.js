let x;
x=3;
console.log(x)

let shuzu=[2,3,1];
console.log(shuzu.length)

// 当您希望将一个未命名的函数作为参数传递给另一个函数时，最常用的是箭头函数。
// 箭头函数，用于函数 参数 为函数类型时使用
const plus1=x=>x+1;

console.log(plus1(5));

console.log([1,2,34,7].reverse())
a={"name":32,"he":"g"}
// 同样的
console.log(a['name'])
console.log(a.name)

//数组求和
function sums(arr){
    let sum=0;
    for (let x of arr){
        sum+=x;
    }
    return sum;
}

console.log(sums([1,2,4]))



