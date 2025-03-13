## **4. 优化网络性能**

### **(1) 减少请求数量**
合并 CSS、JS 文件，减少 HTTP 请求次数，或者使用 HTTP/2。

### **(2) 使用延迟加载（Lazy Loading）**
对于图片、视频等资源，可以延迟加载，只加载用户当前视图需要的内容。

```html
<img src="placeholder.jpg" data-src="actual-image.jpg" loading="lazy" />
```

### **(3) 启用缓存**
在服务器端启用缓存，以减少重复加载资源。

---

## **5. 使用现代 JavaScript 特性**

### **(1) 使用 ES6+ 语法**
ES6+ 提供更高效的特性，例如解构赋值、`let`/`const` 替代 `var`，更适合现代浏览器优化。

```javascript
// ES6 示例
const [first, second] = array;
const sum = (a, b) => a + b;
```

### **(2) 使用异步代码**
通过 `async/await` 替代回调函数链，提升代码可读性和性能。

```javascript
// 不推荐
fetch('url')
  .then(response => response.json())
  .then(data => console.log(data));

// 推荐
async function fetchData() {
  const response = await fetch('url');
  const data = await response.json();
  console.log(data);
}
```

---

## **6. 内存优化**

### **(1) 避免内存泄漏**
常见的内存泄漏原因包括：
- 未清除的全局变量。
- 未解绑的事件监听器。
- 闭包未释放的变量。

```javascript
// 清除事件监听器
const btn = document.getElementById("btn");
const handleClick = () => console.log("clicked");
btn.addEventListener("click", handleClick);

// 当不需要时移除监听器
btn.removeEventListener("click", handleClick);
```

### **(2) 使用弱引用**
在不需要长期保存引用的情况下，使用 `WeakMap` 或 `WeakSet` 来避免内存泄漏。

---

## **7. 使用工具分析性能**
- **Chrome DevTools：** 用于分析渲染、脚本执行、内存使用等性能问题。
- **Lighthouse：** 评估页面性能、SEO 和最佳实践。
- **WebPageTest：** 评估网页加载速度。

---

### **总结**
提高 JavaScript 性能需要从代码结构、算法优化、DOM 操作、网络请求和内存管理等多个方面入手。通过减少不必要的操作、优化资源加载和利用现代工具，能够有效提升代码运行效率和用户体验。

## defer 属性

 
在 HTML 中，`defer` 属性是用来优化 JavaScript 文件加载的，它可以确保脚本在**HTML 文档完全解析完成后**才执行，同时不会阻塞 HTML 的解析过程。

---

### **defer 属性的作用**
1. **异步加载脚本（非阻塞）：**
   - 使用 `defer` 的脚本文件会以异步方式加载，浏览器在下载脚本的同时，不会阻塞 HTML 文档的解析。
   
2. **按顺序执行脚本：**
   - 即使多个带有 `defer` 属性的脚本是异步加载的，它们仍会按照它们在 HTML 中的顺序依次执行。

3. **等待 DOM 解析完成：**
   - `defer` 脚本会等到整个 HTML 文档解析完成后（`DOMContentLoaded` 事件触发之前）再开始执行。

---

### **使用方式**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Defer Example</title>
  <script src="script1.js" defer></script>
  <script src="script2.js" defer></script>
</head>
<body>
  <h1>Hello, World!</h1>
</body>
</html>
```

---

### **defer 的特点：**
1. **与 `async` 的区别：**
   - `defer` 和 `async` 都是异步加载，但执行时机不同：
     - `defer`: 脚本按顺序执行，并在 HTML 解析完成后再执行。
     - `async`: 脚本加载完成后立即执行，可能会打断 HTML 的解析。
     
   | 属性      | 加载方式     | 执行顺序                | 是否阻塞 HTML |
   |-----------|-------------|-------------------------|---------------|
   | 无属性    | 同步加载     | 按顺序执行              | 阻塞          |
   | `defer`   | 异步加载     | 按顺序执行，HTML 解析后 | 不阻塞        |
   | `async`   | 异步加载     | 加载完成立即执行        | 不阻塞        |

2. **适用于外部脚本：**
   - `defer` 仅对外部脚本（`<script src="...">`）有效，对内联脚本无效。

3. **浏览器支持：**
   - 所有现代浏览器都支持 `defer` 属性。

---

### **defer 的应用场景**
- 当脚本依赖于完整的 HTML 结构（如 DOM 元素）时，使用 `defer` 确保脚本在 DOM 解析完成后执行。
- 当有多个脚本需要按顺序执行时，`defer` 能确保顺序一致性。
- 优化页面加载性能，避免脚本阻塞 HTML 解析。

---

### **例子：defer 和 async 的区别**

假设有以下代码：
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <script src="script1.js" defer></script>
  <script src="script2.js" async></script>
  <script src="script3.js" defer></script>
</head>
<body>
  <h1>Hello, World!</h1>
</body>
</html>
```

#### 执行顺序：
1. **script1.js 和 script3.js（defer）：**
   - 异步加载，不阻塞 HTML 解析。
   - 按顺序执行：先 `script1.js`，再 `script3.js`。
   - 在 HTML 解析完成后执行。

2. **script2.js（async）：**
   - 异步加载，不阻塞 HTML 解析。
   - **加载完成后立即执行**，与加载顺序无关。

---

### **总结**
`defer` 属性是一个简单而强大的工具，用于提升页面性能和脚本加载效率：
- **不阻塞 HTML 解析。**
- **保证脚本顺序执行。**
- **适合需要操作完整 DOM 的脚本。**

在优化网页加载时，推荐优先考虑使用 `defer`。