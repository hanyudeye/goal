// console.log(Date())

// Date 对象用于处理日期和时间，获取、设置和操作日期和时间。

// 1. 创建 Date 对象
console.log('1.创建 Date 对象');

var currentDate=new Date(); //使用当前日期和时间创建Date对象
console.log(currentDate);
//转换东八区时间
console.log(currentDate.toUTCString());


var specificDate=new Date(2023,7,1); //使用指定的年月日创建Date对象
//TODO 注意，月的索引是 0开始的，日是 1-31号，这种创建方式乱，没明白
console.log(specificDate);
//转换东八区时间
console.log(specificDate.toUTCString());

var specificDate2=new Date("2023-07-31 11:01:43 GMT");
// 使用这个精准
console.log(specificDate2);

// 2. 获取日期和时间的各个部分：
console.log('2. 获取日期和时间的各个部分');
var year = currentDate.getFullYear(); // 获取年份
var month = currentDate.getMonth(); // 获取月份（0-11，0代表一月）
var day = currentDate.getDate(); // 获取日期
var hours = currentDate.getHours(); // 获取小时
var minutes = currentDate.getMinutes(); // 获取分钟
var seconds = currentDate.getSeconds(); // 获取秒数

console.log(year);
console.log(month);
console.log(day);

// 3. 设置日期和时间的各个部分：
console.log('3.设置日期和时间的各个部分：');

currentDate.setFullYear(2023); // 设置年份
currentDate.setMonth(11); // 设置月份（0-11，11代表十二月）
currentDate.setDate(25); // 设置日期
currentDate.setHours(0); // 设置小时
currentDate.setMinutes(0); // 设置分钟
currentDate.setSeconds(0); // 设置秒数

//  4. 格式化日期和时间：
console.log('4. 格式化日期和时间：');
var formattedDate = currentDate.toLocaleString(); // 格式化为本地日期和时间字符串
var formattedTime = currentDate.toTimeString(); // 格式化为时间字符串
console.log(formattedDate);
console.log(formattedTime);

