### Vue 订阅管理工具实现方案

本文为你提供一个基于 Vue 的订阅管理工具的具体实现方案，包括项目结构、功能划分和编码示例。

#### 1. 需求分析

订阅管理工具的核心功能：
- **订阅列表展示**：展示所有用户订阅的服务信息。
- **新增订阅**：用户可以添加新的订阅服务。
- **编辑订阅**：用户可以修改已订阅的服务。
- **删除订阅**：用户可以删除不再需要的订阅服务。
- **状态更新**：标记订阅服务的有效期及状态（活跃、过期、即将过期）。
- **提醒功能**：提醒用户某个订阅即将过期。

#### 2. 技术栈
- **Vue 3**：前端框架。
- **Vue Router**：实现路由导航。
- **Vuex/Pinia**：状态管理（用于存储订阅数据）。
- **Axios**：发送 HTTP 请求（如需后端 API 支持）。
- **Tailwind CSS 或 Element Plus**：用于 UI 风格和组件。

#### 3. 项目结构

```
├── public
│   └── index.html
├── src
│   ├── assets          // 静态资源，如图片、样式等
│   ├── components      // 通用组件
│   ├── pages           // 页面组件
│   ├── router          // 路由配置
│   ├── store           // Vuex/Pinia 状态管理
│   ├── services        // API 服务文件
│   ├── App.vue         // 根组件
│   └── main.js         // 入口文件
├── package.json        // 项目依赖配置
└── vue.config.js       // Vue 配置文件
```

#### 4. 实现细节

##### 4.1 路由配置（`router/index.js`）

我们将设置几个基础页面：订阅列表页面、添加/编辑订阅页面。

```js
import { createRouter, createWebHistory } from 'vue-router';
import SubscriptionList from '../pages/SubscriptionList.vue';
import AddSubscription from '../pages/AddSubscription.vue';
import EditSubscription from '../pages/EditSubscription.vue';

const routes = [
  { path: '/', component: SubscriptionList },
  { path: '/add', component: AddSubscription },
  { path: '/edit/:id', component: EditSubscription, props: true },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
```

##### 4.2 状态管理（使用 Pinia 作为状态管理库）

安装 Pinia:

```bash
npm install pinia
```

创建 `store/subscription.js` 文件：

```js
import { defineStore } from 'pinia';

export const useSubscriptionStore = defineStore('subscription', {
  state: () => ({
    subscriptions: [],
  }),
  actions: {
    addSubscription(subscription) {
      this.subscriptions.push(subscription);
    },
    updateSubscription(updatedSubscription) {
      const index = this.subscriptions.findIndex(sub => sub.id === updatedSubscription.id);
      if (index !== -1) {
        this.subscriptions[index] = updatedSubscription;
      }
    },
    deleteSubscription(id) {
      this.subscriptions = this.subscriptions.filter(sub => sub.id !== id);
    },
  },
});
```

##### 4.3 订阅列表页面（`pages/SubscriptionList.vue`）

```vue
<template>
  <div>
    <h1>我的订阅</h1>
    <router-link to="/add" class="btn">新增订阅</router-link>
    <ul v-if="subscriptions.length">
      <li v-for="sub in subscriptions" :key="sub.id">
        <span>{{ sub.name }} - {{ sub.status }}</span>
        <router-link :to="'/edit/' + sub.id">编辑</router-link>
        <button @click="deleteSubscription(sub.id)">删除</button>
      </li>
    </ul>
    <p v-else>没有订阅。</p>
  </div>
</template>

<script setup>
import { useSubscriptionStore } from '../store/subscription';
const store = useSubscriptionStore();

const subscriptions = store.subscriptions;
const deleteSubscription = (id) => store.deleteSubscription(id);
</script>

<style scoped>
/* 简单样式 */
.btn {
  background-color: #3490dc;
  color: white;
  padding: 5px 10px;
  border-radius: 5px;
  text-decoration: none;
}
</style>
```

##### 4.4 新增/编辑订阅页面（`pages/AddSubscription.vue` 和 `pages/EditSubscription.vue`）

###### AddSubscription.vue

```vue
<template>
  <div>
    <h1>新增订阅</h1>
    <form @submit.prevent="addNewSubscription">
      <input v-model="name" placeholder="服务名称" />
      <input v-model="status" placeholder="订阅状态" />
      <button type="submit">保存</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useSubscriptionStore } from '../store/subscription';
import { useRouter } from 'vue-router';

const store = useSubscriptionStore();
const router = useRouter();

const name = ref('');
const status = ref('');

const addNewSubscription = () => {
  const newSubscription = { id: Date.now(), name: name.value, status: status.value };
  store.addSubscription(newSubscription);
  router.push('/');
};
</script>
```

###### EditSubscription.vue

```vue
<template>
  <div>
    <h1>编辑订阅</h1>
    <form @submit.prevent="updateCurrentSubscription">
      <input v-model="name" placeholder="服务名称" />
      <input v-model="status" placeholder="订阅状态" />
      <button type="submit">更新</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useSubscriptionStore } from '../store/subscription';
import { useRoute, useRouter } from 'vue-router';

const store = useSubscriptionStore();
const route = useRoute();
const router = useRouter();

const id = route.params.id;
const name = ref('');
const status = ref('');

onMounted(() => {
  const subscription = store.subscriptions.find(sub => sub.id === Number(id));
  if (subscription) {
    name.value = subscription.name;
    status.value = subscription.status;
  }
});

const updateCurrentSubscription = () => {
  store.updateSubscription({ id: Number(id), name: name.value, status: status.value });
  router.push('/');
};
</script>
```

##### 4.5 API 服务示例（`services/api.js`）

如果要对接后端 API，可以通过 Axios 实现。

```js
import axios from 'axios';

const API_URL = 'https://api.example.com/subscriptions';

export const getSubscriptions = () => axios.get(API_URL);
export const addSubscription = (data) => axios.post(API_URL, data);
export const updateSubscription = (id, data) => axios.put(`${API_URL}/${id}`, data);
export const deleteSubscription = (id) => axios.delete(`${API_URL}/${id}`);
```

#### 5. 运行项目

初始化并运行项目：

1. 创建 Vue 3 项目：
```bash
npm init vue@latest
```

2. 安装依赖：
```bash
npm install
```

3. 启动项目：
```bash
npm run dev
```

### 6. 总结

通过该方案，你可以快速搭建一个 Vue 3 订阅管理工具，具备增删改查功能。如果需要扩展功能，比如分页、搜索或高级筛选，可以在此基础上继续完善。