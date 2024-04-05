
// common js 标准，这是默认标准，node环境默认支持这种方法，不用创建 package.json 文件，因为里面 {"type":"commonjs"} 是默认
// const mymodule=require("./mymodule")
// console.log(mymodule.name);

// 下面是 ECMAScript 标准
// 如需使用 ECMAScript 标准语法，再运行模块所在文件夹新建 package.json文件，并设置 {"type":"module"}

import ecmamodule from "./ecmamodule.js";
console.log(ecmamodule)

// 使用命名导入
import {age} from "./ecmamodule.js";
console.log(age)

// 注意，两者不能公用