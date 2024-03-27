const fs = require("fs");
const path = require("path");

// J:\me\Shijian\project\htmltemplates\startadmin\index.html
// J:\me\Shijian\project\服务端\nodejs\压缩文件.js

fs.readFile(path.join(process.cwd(), "\\project\\htmltemplates\\startadmin\\index.html"), (err, data) => {
    if (err) console.log("读取文件错误", err)
    else {
        htmlStr = data.toString();
        const resultStr = htmlStr.replace(/[\r\n]/g, '')
        // console.log(resultStr)
        // 写入 新的 html
        fs.writeFile(path.join(process.cwd(), "\\test.html"), resultStr, err => {
            if (err) console.log(err)
            else console.log("写入成功")
        })

    }
});