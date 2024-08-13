// 这是一个 Counter 组件

// 引入 React 框架
import React, { useState } from "react";

// 组件Counter 的属性用法，组件的状态和生命周期的用法
function Counter() {

    //使用 useState 函数设置属性
    const [count, setCount] = useState(0);

    return (
        <div>
            <h1>Count:{count}</h1>
            <button onClick={() => setCount(count + 1)}>计算</button>
        </div>
    );
}

export default Counter;