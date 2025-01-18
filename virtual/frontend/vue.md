## 安装 

``` sh
npm create vue@latest
```

## 组件之间通信

在Vue.js中，组件之间通信是一个非常常见的需求。以下是几种常用的Vue组件之间通信的方式：

1. **Props/Events（属性/事件）**:
   - **Props**: 父组件通过props向子组件传递数据。
   - **Events**: 子组件通过触发事件，向父组件传递消息。

2. **Vuex**:
   - Vuex是Vue.js官方提供的状态管理库，用于管理应用中的共享状态。通过Vuex，不同组件可以共享状态并实现通信。

3. **$emit / $on**:
   - Vue实例提供了`$emit`和`$on`方法，可以用于自定义事件的触发和监听。

4. **$refs**:
   - 通过`ref`属性可以在父组件中引用子组件，然后通过`$refs`访问子组件的属性和方法。

5. **Provide/Inject**:
   - 父组件通过`provide`提供数据，子组件通过`inject`注入数据，实现跨层级组件之间的通信。

6. **Event Bus**:
   - 可以使用一个空的Vue实例作为事件总线，通过它来触发和监听事件，实现组件之间的通信。

7. **$parent / $children**:
   - 可以通过`$parent`和`$children`访问父组件和子组件实例，从而实现通信。

8. **$attrs / $listeners**:
   - 在父组件中可以通过`$attrs`访问子组件的所有属性，通过`$listeners`访问子组件的所有事件监听器。

这些是Vue.js中常用的组件之间通信方式。根据具体的场景和需求，选择合适的方式来实现组件之间的通信。

## 模块化开发

import 结构，就是模块化开发

## 根组件

传递给 createApp 的选项用于配置根组件。 一个应用需要被挂载到一个DOM 元素中。
例如，如果我们想把一个 Vue应用挂载到 <div id="app"></div>,我们应该传递#app:

```js
const RootComponent={/*选项*/}
const app=Vue.createApp(RootComponent)
const vm=app.mount('#app')

```

与大多数应用方法不同的是，mount 不返回应用本身，相反，它返回的是根组件实例vm，根组件实例与其它组件实例没什么不同。


## 组件实例 property

具体有:
- data
- methods
- props
- computed
- inject
- setup
- 内置 property ,如 $attrs 、$emit

在 Vue 3 中，setup() 函数是一个新的组件选项，它取代了 Vue 2.x 中的 data、computed、methods 等选项。setup() 函数提供了一种新的方式来配置组件，它的主要用途和优点包括：

组合式 API 支持：

setup() 函数是支持组合式 API 的基础。组合式 API 允许开发者将组件的逻辑进行更细粒度的组织，例如可以通过单独的函数来组合和重用代码。

更加透明和灵活：

setup() 函数在组件的创建阶段运行，并且是在组件实例化之前执行的，这使得可以更好地控制组件的初始化行为。
可以在 setup() 中直接访问 props、context、attrs 等，并且不需要使用 this。
逻辑分离：

setup() 函数将组件的逻辑与声明分离，使得组件更容易理解和维护。每个功能块可以被组织为一个单独的函数，然后在 setup() 中进行组合。

更灵活的响应式数据：

在 setup() 中可以通过 reactive、ref 等 API 来创建响应式数据，以及监听副作用。
``` js
<template>
  <div>{{ count }}</div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const count = ref(0);

onMounted(() => {
setInterval(() => {
    count.value++;
  }, 1000);
});
</script>
```
在上面的示例中，setup() 函数内部使用了 ref 来创建一个响应式的 count 变量，并在 onMounted 钩子中开始计时。这种方式相比于 Vue 2.x 的 data 和 methods 选项更为直观和简洁。

## 生命周期钩子

每个组件在被创建时要经过一系列初始化过程，如设置数据监听、编译模板、将实例挂载到DOM并在数据变化时更新DOM等。同时也会运行叫做生命周期钩子的函数，这给了用户在不同阶段添加自己代码的机会。

如：
- created : 用来在一个实列被创建后执行代码
- mounted
- updated
- unmounted

## 模板语法

Vue.js 使用了基于 HTML的模板语法，允许开发者声明式地将DOM绑定至底层组件实例的数据。



