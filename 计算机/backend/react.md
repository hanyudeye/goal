构建用户界面

1. react 是什么 : 是一个使用 javascript 来构建 DOM界面 的框架，开源，不用 html 超链接 刷新影响应用的体验。


2. 这个框架提倡 `界面组件化`， `单向数据流`

组件能保存状态(State)和属性(Props) ，并且提供了生命周期方法，来给组件合适的生命。

## 简介

- 组件: 有一种创建组件的语法，用来共用相同的东西（因为现代系统很大，很多可以重复利用的，就像函数用途）
- 组件的声明周期
- 事件

3. **props**：
   - props 是组件的属性，用于向组件传递数据。
   - props 是只读的，不能在组件内部修改。

4. **状态（State）**：
   - 状态是组件内部的数据源，用于描述组件的状态和行为。
   - 可以使用 useState Hook（函数式组件）或 setState 方法（类组件）来管理组件的状态。

5. **生命周期方法**（仅适用于类组件）：
   - 类组件具有生命周期方法，可以在组件的不同阶段执行一些操作，例如组件被挂载到 DOM 中、更新、卸载等。

6. **Hooks**：
   - Hooks 是 React 16.8 引入的新特性，允许在函数式组件中使用状态、副作用等 React 特性。
   - 常用的 Hooks 包括 useState、useEffect、useContext 等。

7. **事件处理**：
   - React 使用类似于 HTML 的事件处理方式，例如 onClick、onChange 等。
   - 事件处理程序通常是在组件内部定义的，并且通常是作为属性传递给子组件。

8. **条件渲染**：
   - 可以使用 JavaScript 的条件语句（如 if、三元运算符等）来根据条件渲染不同的内容。

9. **列表渲染**：
   - 可以使用 JavaScript 的 map 方法对数组进行映射，以渲染列表中的多个元素。

10. **样式**：
    - 可以将样式直接写在 JSX 中，也可以使用外部样式表或 CSS-in-JS 库来管理样式。

11. **表单**：
    - React 中的表单处理与普通 HTML 表单类似，但使用了受控组件的概念来管理表单状态。

12. **组件通信**：
    - 父组件可以通过 props 向子组件传递数据，子组件可以通过回调函数或 Context API 将数据传递回父组件。
    - 兄弟组件之间的通信可以通过将共享状态提升到它们的共同父组件中来实现。

这些是 React 开发中的一些核心接口和概念，它们组合在一起可以构建出强大、灵活且易于维护的用户界面。

## react 

React 是一个由 Facebook 开发的用于构建用户界面的 JavaScript 库。它主要用于构建单页面应用（SPA）中的用户界面，但也可以用于构建传统的多页面应用。

### React 的特点包括：

1. **组件化：** React 将用户界面拆分为独立的组件，每个组件都有自己的状态（state）和属性（props），可以通过组合这些组件来构建复杂的用户界面。

2. **虚拟 DOM：** React 使用虚拟 DOM 来提高性能。它会在内存中维护一个虚拟 DOM 树，然后通过比较虚拟 DOM 和真实 DOM 的差异来最小化 DOM 操作，从而提高页面渲染的效率。

3. **声明式编程：** React 采用声明式的编程模式，开发者只需要描述界面应该呈现的样子，而不需要手动操作 DOM，使得代码更加简洁易懂。

4. **单向数据流：** React 使用单向数据流来管理组件之间的数据传递和状态管理，这样可以减少出现 bug 的可能性，并且方便进行状态管理。

5. **生态系统丰富：** React 生态系统非常丰富，有大量的第三方库和工具可供开发者使用，例如 Redux、React Router、Material-UI 等，可以帮助开发者更快速地构建应用。

### React 的用法：

1. **创建 React 应用：** 首先，你需要安装 Node.js 和 npm（或者使用 Yarn）。然后，你可以使用 Create React App 工具来快速创建一个新的 React 应用。在命令行中执行以下命令：

```bash
npx create-react-app my-app
```

这会在当前目录下创建一个名为 `my-app` 的新的 React 应用。

2. **编写组件：** 在 React 应用中，你将主要编写组件来构建用户界面。每个组件通常都是一个 JavaScript 类或函数，用于描述界面的一部分。你可以创建新的组件并在其内部定义 `render` 方法来返回要呈现的 JSX（JavaScript XML）。

```jsx
import React from 'react';

function App() {
  return (
    <div>
      <h1>Hello, React!</h1>
      <p>This is a React application.</p>
    </div>
  );
}

export default App;
```

3. **渲染组件：** 一旦你编写了组件，你需要在应用的入口文件中将它们渲染到页面上。通常，你会将根组件渲染到 `index.html` 文件中的某个容器中。

```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```

4. **运行应用：** 最后，你可以在命令行中执行以下命令来启动 React 应用：

```bash
npm start
```

或者使用 Yarn：

```bash
yarn start
```

这会启动一个开发服务器，并在浏览器中打开你的 React 应用。

这只是 React 的基础用法介绍，还有很多其他方面需要学习，如组件间通信、状态管理、路由等。建议你阅读官方文档以及其他教程来深入了解 React。
