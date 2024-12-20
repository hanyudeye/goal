---
layout: default
toc: false
title: 异步任务
date:  2024-12-20T18:24:30+08:00
categories: ['']
---

异步任务相当于托管任务，在一些非主线的任务中，可以使用的旁支任务。

<!--more-->


## 前端使用异步编程的场景
什么时候需要等待，就什么时候用异步。常见的异步场景如下：

- 1、事件监听（比如说，按钮绑定点击事件之后，用户爱点不点。我们不可能卡在按钮那里，什么都不做。所以，应该用异步）
- 2、回调函数：
  - 2.1、定时器：setTimeout（定时炸弹）、setInterval（循环执行）
  - 2.2、ajax请求。
  - 2.3、Node.js：FS文件读写、数据库操作。
- 3、ES6 中的 Promise、Generator、async/await

现在的大部分软件项目，都是前后端分离的。后端生成接口，前端请求接口。前端发送 ajax 请求，向后端请求数据，然后等待一段时间后，才能拿到数据。这个请求过程就是异步任务。


## Ajax

Ajax：Asynchronous Javascript And XML（异步 JavaScript 和 XML）。

发送 Ajax 请求的五个步骤：

- （1）创建异步对象，即 XMLHttpRequest 对象。

- （2）使用 open 方法设置请求参数。open(method, url, async)。参数解释：请求的方法、请求的 url、是否异步。第三个参数如果不写，则默认为 true。

- （3）发送请求：send()。

- （4）注册事件：注册 onreadystatechange 事件，状态改变时就会调用。
        如果要在数据完整请求回来的时候才调用，我们需要手动写一些判断的逻辑。

- （5）服务端响应，获取返回的数据。


get 请求：
``` js
//【发送ajax请求需要五步】
//（1）创建XMLHttpRequest对象
var xmlhttp = new XMLHttpRequest();

//（2）设置请求的参数。包括：请求的方法、请求的url。
xmlhttp.open('get', '02-ajax.php');

//（3）发送请求
xmlhttp.send();

//（4）注册事件。 onreadystatechange事件，状态改变时就会调用。
//如果要在数据完整请求回来的时候才调用，我们需要手动写一些判断的逻辑。
xmlhttp.onreadystatechange = function () {
    // 为了保证 数据 完整返回，我们一般会判断 两个值
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
        //（5）服务端相应：如果能够进入这个判断，说明数据请求成功了
        console.log('数据返回成功：' + JSON.stringify(xmlhttp.responseText));

        // 伪代码：按业务需要，将接口返回的内容显示在页面上
        // document.querySelector('h1').innerHTML = xmlhttp.responseText;
    }
};
```
post 请求：
``` js
//（1）异步对象
var xmlhttp = new XMLHttpRequest();

//（2）设置请求参数。包括：请求的方法、请求的url。
xmlhttp.open('post', '02.post.php');

// 如果想要使用post提交数据,必须添加此行
xmlhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

//（3）发送请求
xmlhttp.send('name=fox&age=18');

//（4）注册事件
xmlhttp.onreadystatechange = function () {
    //（5）服务端相应
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
        alert(xmlhttp.responseText);
    }
};
```