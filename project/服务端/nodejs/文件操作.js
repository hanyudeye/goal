const fs = require('fs');
const os = require('os');

const path = require('path');

console.log(process.cwd());
// 打印执行文件当前路径
console.log(__dirname);

// return;

// 写入文件
fs.writeFile('./test.txt', "hello,Node.js", (err) => {
    if (err) console.log(err);
    else console.log('写入成功');
})

fs.readFile('test.txt',(err,data)=>{

    if(err) console.log(err)
    else  console.log(data.toString())
})