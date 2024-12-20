---
layout: default
toc: false
title: JavaScript 模块化规范（ESM 和 CommonJS）
date:  2024-12-20T10:47:40+08:00
categories: ['']
---
 
JavaScript 的模块化规范主要包括两种：ESM（ECMAScript 模块）和 CommonJS。它们分别是如何定义和组织 JavaScript 模块的标准，具体内容如下：

<!--more-->

### 1. ESM（ECMAScript 模块）

**定义**：
- ESM 是 ECMAScript 标准中定义的官方模块系统，自 ECMAScript 6（ES6）开始引入。
- 使用 `import` 和 `export` 关键字来定义模块的导入和导出。

**特点与用法**：
- **导出模块成员**：
  ```javascript
  // 导出单个成员
  export function foo() { ... }

  // 导出多个成员
  export { foo, bar };

  // 默认导出（一个模块只能有一个默认导出）
  export default function() { ... }
  ```

- **导入模块成员**：
  ```javascript
  // 导入具名成员
  import { foo, bar } from './module.js';

  // 导入默认成员
  import defaultExport from './module.js';

  // 导入所有成员（不推荐）
  import * as module from './module.js';
  ```

- **异步加载**：支持动态导入，可以在运行时异步加载模块：
  ```javascript
  import('./module.js').then(module => {
    // 使用模块
  });
  ```

- **运行环境**：适用于现代浏览器和 Node.js 12+（需要启用 `--experimental-modules` 标志）。

### 2. CommonJS

**定义**：
- CommonJS 是 Node.js 中广泛使用的模块化规范，用于组织和导入导出 JavaScript 模块。
- 使用 `require()` 函数来引入模块，使用 `module.exports` 或 `exports` 导出模块。

**特点与用法**：
- **导出模块成员**：
  ```javascript
  // 导出单个成员
  module.exports = function() { ... };

  // 导出多个成员
  exports.foo = function() { ... };
  exports.bar = function() { ... };
  ```

- **导入模块成员**：
  ```javascript
  // 导入模块
  const module = require('./module.js');

  // 使用导入的成员
  module.foo();
  module.bar();
  ```

- **同步加载**：由于 Node.js 的同步特性，模块在代码执行前被加载，不支持动态导入。

- **运行环境**：主要用于 Node.js 环境，不适用于浏览器端。

### 比较与应用场景选择

- **ESM vs CommonJS**：
  - **ESM** 支持静态分析、异步加载、编译时优化，适合浏览器环境和现代 Node.js。
  - **CommonJS** 简单易用，适合于传统的服务器端开发，但在浏览器端不可用且不能静态分析，限制了某些优化。

- **应用场景选择**：
  - 如果在浏览器中或者希望使用现代 JavaScript 的优化功能，选择 **ESM** 更为合适。
  - 如果在 Node.js 旧版本或特定需求下，使用 **CommonJS** 仍然是一种稳定且有效的选择。

综上所述，选择模块化规范应基于具体的运行环境和项目需求来决定，ESM 和 CommonJS 各有其适用场景和优缺点。