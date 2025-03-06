 在 Vue 3 中安装 Tailwind CSS，并使用其样式美化博客是一个很好的选择。下面是一个简单的安装和适配教程：

### 步骤 1：安装 Vue 3 项目

如果还没有创建 Vue 3 项目，可以使用以下命令创建：

```bash
vue create my-blog
cd my-blog
```

### 步骤 2：安装 Tailwind CSS

在项目目录中，运行以下命令以安装 Tailwind CSS 和其相关依赖：

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

### 步骤 3：配置 Tailwind CSS

1. 打开生成的 `tailwind.config.js` 文件，并配置 `content` 选项，以便 Tailwind 可以扫描所有的 Vue 文件：

   ```javascript
   /** @type {import('tailwindcss').Config} */
   module.exports = {
     content: [
       "./index.html",
       "./src/**/*.{vue,js,ts,jsx,tsx}",
     ],
     theme: {
       extend: {},
     },
     plugins: [],
   };
   ```

2. 接下来，在 `src/assets` 目录中创建一个名为 `tailwind.css` 的文件，并添加以下内容：

   ```css
   @tailwind base;
   @tailwind components;
   @tailwind utilities;
   ```

3. 在 `src/main.js` 文件中引入这个 `tailwind.css` 文件：

   ```javascript
   import { createApp } from 'vue';
   import App from './App.vue';
   import router from './router';
   import './assets/tailwind.css'; // 引入 Tailwind CSS

   createApp(App).use(router).mount('#app');
   ```

### 步骤 4：使用 Tailwind CSS 美化博客

接下来，您可以在博客中使用 Tailwind 的样式。以下是一些简单的示例，您可以在 `BlogList.vue` 和 `BlogDetail.vue` 中应用这些样式。

#### 示例：美化 `BlogList.vue`

```vue
<template>
  <div class="container mx-auto p-4">
    <h1 class="text-3xl font-bold mb-4">博客列表</h1>
    <ul class="space-y-2">
      <li v-for="post in posts" :key="post.id">
        <router-link
          :to="{ name: 'BlogDetail', params: { id: post.id } }"
          class="block p-4 border rounded-lg hover:bg-gray-100 transition"
        >
          {{ post.title }}
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      posts: [
        { id: 1, title: '第一篇博客' },
        { id: 2, title: '第二篇博客' },
        { id: 3, title: '第三篇博客' },
      ],
    };
  },
};
</script>

<style scoped>
/* 这里可以添加其他样式 */
</style>
```

#### 示例：美化 `BlogDetail.vue`

```vue
<template>
  <div class="container mx-auto p-4">
    <h1 class="text-2xl font-bold mb-2">{{ post.title }}</h1>
    <p class="text-gray-700">{{ post.content }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      post: {},
    };
  },
  mounted() {
    const id = this.$route.params.id;
    const posts = [
      { id: 1, title: '第一篇博客', content: '这是第一篇博客内容。' },
      { id: 2, title: '第二篇博客', content: '这是第二篇博客内容。' },
      { id: 3, title: '第三篇博客', content: '这是第三篇博客内容。' },
    ];
    this.post = posts.find((post) => post.id === parseInt(id));
  },
};
</script>

<style scoped>
/* 这里可以添加其他样式 */
</style>
```

### 步骤 5：桌面端和移动端适配

Tailwind CSS 提供了响应式设计工具，您可以使用断点类（如 `sm:`, `md:`, `lg:`, `xl:`）来为不同的屏幕大小添加样式。例如：

```vue
<h1 class="text-3xl md:text-4xl lg:text-5xl font-bold mb-4">博客列表</h1>
```

上面的代码会在小屏幕上使用 `text-3xl`，在中等屏幕上使用 `text-4xl`，在大屏幕上使用 `text-5xl`。

### 总结

通过以上步骤，您已经成功在 Vue 3 中安装了 Tailwind CSS，并使用它来美化您的博客。您可以根据需要进一步自定义样式和布局，使其更符合您的设计需求。