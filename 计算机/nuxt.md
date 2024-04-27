# nuxt

Nuxt.js 是一个基于 Vue.js 的服务端渲染应用框架。它可以帮助你轻松地构建同构应用（服务器端渲染的 Web 应用程序）。

### 什么是 Nuxt 3？

Nuxt 3 是 Nuxt.js 的下一代版本，其目标是进一步改进 Nuxt.js 的性能、开发体验和可扩展性。Nuxt 3 基于 Vite 构建，提供了许多新功能和改进。

### Nuxt 3 的新功能和改进

1. **基于 Vite：** Nuxt 3 切换到了 Vite 作为其默认的开发和构建工具。Vite 是一个现代化的构建工具，通过利用 ES Module（ESM）特性提供了出色的性能。
   
2. **TypeScript 支持：** Nuxt 3 具有更好的 TypeScript 支持，使得使用 TypeScript 来开发 Nuxt 应用变得更加流畅。
   
3. **更快的热重载：** 借助 Vite，Nuxt 3 提供了更快的热重载，使得开发过程更加高效。

4. **更好的构建性能：** Vite 的构建速度比 Webpack 更快，这意味着构建和重建 Nuxt 3 应用程序的速度更快。

5. **全新的插件系统：** Nuxt 3 引入了全新的插件系统，使得在应用中使用第三方库更加容易。

6. **自定义 Vite 配置：** 你可以根据需要自定义 Vite 的配置，以满足你的特定需求。

### 如何使用 Nuxt 3？

#### 安装 Nuxt 3

Nuxt 3 目前还处于开发阶段，可以通过以下命令安装：

```bash
npm init nuxt-app@latest my-nuxt-app
```

或者使用 Yarn：

```bash
yarn create nuxt-app@latest my-nuxt-app
```

#### 创建新的 Nuxt 3 项目

执行上述命令后，会出现一系列提示，你可以根据需要进行选择。完成后，将生成一个新的 Nuxt 3 项目。

#### 运行 Nuxt 3 项目

在项目目录中运行以下命令启动项目：

```bash
cd my-nuxt-app
npm run dev
```

或者使用 Yarn：

```bash
cd my-nuxt-app
yarn dev
```

#### 创建页面

在 Nuxt 3 中，页面默认情况下存储在 `pages` 目录中。每个 `.vue` 文件将成为一个页面。

```vue
<!-- pages/index.vue -->
<template>
  <div>
    <h1>Welcome to Nuxt 3!</h1>
  </div>
</template>
```

#### 自定义 Vite 配置

你可以通过在项目根目录创建 `vite.config.js` 文件来自定义 Vite 的配置。

```javascript
// vite.config.js
export default {
  // 自定义 Vite 配置
}
```

### 示例：一个基本的 Nuxt 3 应用程序

以下是一个简单的 Nuxt 3 应用程序示例：

```vue
<!-- pages/index.vue -->
<template>
  <div>
    <h1>Welcome to Nuxt 3!</h1>
    <p>Count: {{ count }}</p>
    <button @click="increment">Increment</button>
  </div>
</template>

<script setup>
let count = ref(0)

function increment() {
  count.value++
}
</script>
```

### 总结

Nuxt 3 是 Nuxt.js 的下一代版本，它引入了许多新功能和改进，使得开发同构应用更加流畅和高效。通过结合 Vite 和 Nuxt，Nuxt 3 提供了更快的开发体验和更好的构建性能。

### nuxt3 404 page not found 路由