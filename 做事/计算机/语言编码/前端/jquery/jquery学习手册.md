---
title: jQuery学习手册
permalink: jquery.html
theme: jekyll-theme-cayman
---


## 选择符

>选择符用来获取 html 对象

   | 选择符              | 匹配                                                     |
   |----------------------|-------------------------------------------------|
   | #                   | 所有元素                                                 |
   | #id                 | 带有给定 ID 的元素                                       |
   | element             | 给定类型的所有元素，比如说 html 标签                     |
   | .class              | 带有给定类的所有元素                                     |
   | a,b                 | 匹配 a 或者匹配 b 的元素                                 |
   | a b                 | 作为 a 后代的匹配 b 的元素（包括孙子辈的）               |
   | a > b               | 作为 a 子元素的匹配 b 的元素（只包括儿子辈）             |
   | a + b               | 相邻兄弟选择器，选择与A相邻的元素B            |
   | a ~ b               | 兄弟选择器，选择与A同层的元素B  |
   | :first              | 结果集中的第一个元素                                     |
   | :last               | 结果集中的最后一个元素                                   |
   | :not(a)             | 结果集中与 a 不匹配的所有元素                            |
   | :even               | 结果集中的偶数元素（从 0 开始计数）                      |
   | :odd                | 结果集中的奇数元素（从 0 开始计数）                      |
   | :eq(index)          | 结果集中索引为 index 的元素（从 0 开始计数）             |
   | :gt(index)          | 结果集中所有位于给定索引之后的元素（从 0 开始计数）      |
   | :lt(index)          | 结果集中所有位于给定索引之前的元素（从 0 开始计数）      |
   | :header            | 标题元素（<h1><h2>）                                     |
   | :animated          | 其动画正在播放的元素                                     |
   | :contains(text)    | 包含给定文本 text 的元素                                 |
   | :empty              | 不包含子节点的元素                                       |
   | :has(a)             | 后代元素中至少有一个匹配 a 的元素                        |
   | :parent             | 当前元素的直接父元素                                     |
   | :hidden             | 隐藏的元素，包括通过 css 隐藏以及<input type="hidden" /> |
   | :visible            | 与:hidden 匹配的元素相反                                |
   | [attr]              | 带有属性 attr 的元素                                     |
   | [attr=value]        | attr 属性的值为 value 的元素                             |
   | [attr!=value]       | attr 属性的值不为 value 的元素                           |
   | [attr^=value]       | attr 属性的值以 value 开头的元素                         |
   | [attr$=value]       | attr 属性的值以 value 结尾的元素                         |
   | [attr#=value]       | attr 属性的值包含字符串 value 的元素                     |
   | :nth-child(index)   | 匹配集合中每个元素的第 index 个子元素（从 1 开始计数）   |
   | :nth-child(even)    | 匹配集合中每个元素的排在偶数位的子元素（从 1 开始计数）  |
   | :nth-child(formula) | Formula 是个公式，格式为 an+b，a、b 为整数               |
   | :first-child        | 匹配集合中每个元素的第一个子元素                         |
   | :last-child         | 匹配集合中每个元素的最后一个子元素                       |
   | :only-child         | 匹配集合中每个元素的惟一子元素,如果不唯一,则不执行       |
   | :input              | 所有<input><select><textarea>和<button>元素              |
   | :text               | Type＝“text”的<input>元素                              |
   | :password           | Type＝“password”的<input>元素                          |
   | :radio              | Type=“radio”的<input>元素                              |
   | :checkbox           | Type＝“checkbox”的<input>元素                          |
   | :submit             | Type＝“submit”的<input>元素                            |
   | :image              | Type＝“image”的<input>元素                             |
   | :reset              | Type＝“reset”的<input>元素                             |
   | :button             | Type＝“button”的<input>元素及<button>元素              |
   | :file               | Type＝“file”的<input>元素                              |
   | :enabled            | 启用的表单元素                                           |
   | :disabled           | 禁用的表单元素                                           |
   | :checked            | 选中的复选框和单选按钮元素                               |
   | :selected           | 选中的<option>元素                                       |
  
## 事件

文档载入事件
``` js
$(document).ready(function(){});
等效于
$(function(){})
```

以上这些事件在 jQuery 内部，都是.bind()的便捷方式。使用.bind()可以更灵活地控制事件，比如为多个事件绑定同一个函数：

   ``` js
       $('input').bind(
           'click change'， //同时绑定click和change事件  
           function(){
               alert('Hello');
           }
       );
   ```

   如果你只想让事件运行一次，这时可以使用.one()方法。

   ``` js
     $("p").one("click"， function(){
         alert("Hello"); //只运行一次，以后的点击不会运行
     });
   ```

   .unbind()用来解除事件绑定。

   ``` js
   $('p').unbind('click'); 
   ```

   所有的事件处理函数，都可以接受一个事件对象(event object)作为参数，比如下面例子中的 e：

   ``` js
     $("p").click(function(e){  
         alert(e.type); //"click"  
     }); 
   ```

   这个事件对象有一些很有用的属性和方法：

   - event.pageX 事件发生时，鼠标距离网页左上角的水平距离
   - event.pageY 事件发生时，鼠标距离网页左上角的垂直距离
   - event.type 事件的类型(比如 click)
   - event.which 按下了哪一个键
   - event.data 在事件对象上绑定数据，然后传入事件处理函数
   - event.target 事件针对的网页元素
   - event.preventDefault() 阻止事件的默认行为(比如点击链接，会自动打开新页面)
   - event.stopPropagation() 停止事件向上层元素冒泡

     在事件处理函数中，可以用 this 关键字，返回事件针对的 DOM 元素：

     ``` js
       $('a').click(function(){  
           if ($(this).attr('href').match('evil')){//如果确认为有害链接
               e.preventDefault(); //阻止打开
               $(this).addClass('evil'); //加上表示有害的class
           }  
       });  
     ```
     有两种方法，可以自动触发一个事件。一种是直接使用事件函数，另一种是使用.trigger()或.triggerHandler()。

     ``` js
       $('a').click();
       $('a').trigger('click');
     ```


##  效果
   jQuery 允许对象呈现某些特殊效果。

   ``` js
     $('h1').show(); //展现一个h1标题 
   ```
   除了.show()和.hide()，所有其他特效的默认执行时间都是 400ms(毫秒)，但是你可以改变这个设置。

   ``` js
     $('h1').fadeIn(300); // 300毫秒内淡入  
     $('h1').fadeOut('slow'); //缓慢地淡出 
   ```

   在特效结束后，可以指定执行某个函数。

   ``` js
     $('p').fadeOut(300, function(){$(this).remove(); }); 
   ```

   更复杂的特效，可以用.animate()自定义。

   ``` js
     $('div').animate(
  {
      left : "+=50"，//不断右移
      opacity : 0.25 //指定透明度
  },
  300,// 持续时间
  function(){ alert('done!'); }//回调函数
     ); 
   ```

   - .stop()和.delay()用来停止或延缓特效的执行。
   - $.fx.off 如果设置为 true，则关闭所有网页特效。
## AJax

### $.ajax

``` js
    $(function(){
        //请求参数
        var list = {};
        $.ajax({
            //请求方式
            type : "POST",
            //请求的媒体类型
            contentType: "application/json;charset=UTF-8",
            //请求地址
            url : "http://127.0.0.1/admin/list/",
            data : JSON.stringify(list),
            success : function(result) {},
            //请求失败，包含具体的错误信息
            error : function(e){}
        });
    });
```
     
可选字段：
 1. url：链接地址，字符串表示
 2. data：需发送到服务器的数据，GET与POST都可以，格式为{A: '...', B: '...'}
 3. type："POST" 或 "GET"，请求类型
 4. timeout：请求超时时间，单位为毫秒，数值表示
 5. cache：是否缓存请求结果，bool表示
 6. contentType：内容类型，默认为"application/x-www-form-urlencoded"
 7. dataType：服务器响应的数据类型，字符串表示；当填写为json时，回调函数中无需再对数据反序列化为json
 8. success：请求成功后，服务器回调的函数
 9. error：请求失败后，服务器回调的函数
 10. complete：请求完成后调用的函数，无论请求是成功还是失败，都会调用该函数；如果设置了success与error函数，则该函数在它们之后被调用
 11. async：是否异步处理，bool表示，默认为true；设置该值为false后，JS不会向下执行，而是原地等待服务器返回数据，并完成相应的回调函数后，再向下执行
 12. username：访问认证请求中携带的用户名，字符串表示
 13. password：返回认证请求中携带的密码，字符串表示

### $.post
    形式：$.post(url, data, func, dataType);
    
    ``` js
    $.post(
    "/greet",
    {name: 'Brad'},
    function(data) {
        ...
    },
    "json"
);
    ```

### $.get()
    形式：$.get(url, data, func, dataType);

### $.getJSON()
    形式：$.getJSON(url, data, func);

### $.load()
    形式：$.load(url, data, func);
    其中data如果存在则使用POST方式发送请求，不存在则使用GET方式发送请求。

### $(selector).serialize()


# [[http://jquery.cuishifeng.cn/index.html][速查表]]

## 遍历方法

   | 遍历方法              | 返回值的 jQuery 对象包含                                     |
   |-----------------------|--------------------------------------------------------------|
   | .filter(selector)     | 与给定的选择符匹配的选中元素, !注意, 是选中的集合中再filter                                |
   | .filter(callback)     | 回调函数 callback 返回 true 的选中元素                       |
   | .eq(index)            | 从 0 开始计数的第 index 个选中元素                           |
   | .slice(start,[end])   | 从 0 开始计数的给定范围的选中元素                            |
   | .not(selector)        | 与给定的选择符不匹配的选中元素                               |
   | .add(selector)        | 选中元素再加上与给定选择符匹配的元素                         |
   | .find(selector)       | 与给定选择符匹配的后代元素                                   |
   | .contents             | 子节点，包括文本节点                                         |
   | .children([selector]) | 匹配选择符的子节点                                           |
   | .next([selector])     | 每个选中元素的下一个匹配选择符的同辈元素                     |
   | .nextAll([selector])  | 每个选中元素之后的所有匹配选择符的同辈元素                   |
   | .prev([selector])     | 每个选中元素的上一个匹配选择符的同辈元素                     |
   | .prevAll([selector])  | 每个选中元素之后的所有匹配选择符的同辈元素                   |
   | .siblings([selector]) | 匹配选择符的所有同辈元素                                     |
   | .parent([selector])   | 每个选中元素的匹配选择符的父元素                             |
   | .parents([selector])  | 每个选中元素的匹配选择符的所有祖先元素                       |
   | .offsetParent()       | 第一个选中元素被定位的父元素(用 relative 或者 absolute 定位) |
   | .andSelf()            | 选中元素再加上内部 jQuery 栈中之前选中的元素                 |
   | .end()                | 内部 jQuery 栈中之前选中的元素                               |
   | .map(callback)        | 对每个选中元素调用回调函数 callback 之后的结果               |

## 事件方法

   | 事件方法                     | 说明                                                       |
   | .ready(fun)                  | 绑定在 DOM 和 CSS 完全加载后调用的处理程序 fun             |
   | .bind(type,[data],fun)       | 绑定在给定类型的事件 type 发送到元素时调用的处理程序 fun   |
   | .one(type,[data],fun)        | fun 方法只执行一次                                         |
   | .unbind(type,[fun])          | 解除元素上绑定的处理程序                                   |
   | .live(type,fun)              | 绑定当给定事件发送到元素后调用的处理程序，动态生成使用这个 |
   | .die(type,[fun])             | 移除前面通过 live()绑定到元素上的处理程序                  |
   | .blur(fun)                   | 失去焦点事件                                               |
   | .change(fun)                 | 当前值改变事件                                             |
   | .click(fun)                  | 点击事件                                                   |
   | .dbclick(fun)                | 双击事件                                                   |
   | .error(fun)                  | 错误事件                                                   |
   | .focus(fun)                  | 获取键盘焦点事件                                           |
   | .keydown(fun)                | 获取键盘焦点且有键被按下事件                               |
   | .keypress(fun)               | 获取键盘焦点且有按键事件发生事件                           |
   | .keyup(fun)                  | 获取键盘焦点且有键被释放事件                               |
   | .load(fun)                   | 元素加载完成事件                                           |
   | .mousedown(fun)              | 按下鼠标键事件                                             |
   | .mouseenter(fun)             | 鼠标指针进入元素事件，不受事件冒泡影响                     |
   | .mouseleave(fun)             | 鼠标指针离开元素事件，不受事件冒泡影响                     |
   | .mousemove(fun)              | 移动鼠标指针事件                                           |
   | .mouseout(fun)               | 鼠标指针离开事件                                           |
   | .mouseover(fun)              | 鼠标指针进入事件                                           |
   | .mouseup(fun)                | 鼠标指针释放事件                                           |
   | .resize(fun)                 | 调整元素大小事件                                           |
   | .scroll(fun)                 | 元素滚动位置改变事件                                       |
   | .select(fun)                 | 文本被选中事件                                             |
   | .submit(fun)                 | 提交事件                                                   |
   | .unload(fun)                 | 元素从内存被卸载后调用事件                                 |
   | .hover(enter,leave)          | 进入执行 enter，离开执行 leave                             |
   | .toggle(fun1,fun2)           | 顺序执行事件，来回循环                                     |
   | .trigger(type,[data])        | 触发元素事件，并执行该事件默认操作                         |
   | .triggerHandler(type,[data]) | 触发元素事件，不执行该事件默认操作                         |
   | .blur()                      | 触发 blur 事件，下面道理一样，方法变动                     |
   | .change()                    |                                                            |
   | .click()                     | ...                                                        |
   | .dbclick()                   | ...                                                        |
   | .error()                     | ...                                                        |
   | .focus()                     | ...                                                        |
   | .keydown()                   | ...                                                        |
   | .keypress()                  | ...                                                        |
   | .keyup()                     | ...                                                        |
   | .select()                    | ...                                                        |
   | .submit()                    | ...                                                        |
## 效果方法

   | 效果方法                          | 说明                                 |
   | .show()                           | 显示                                 |
   | .hide()                           | 隐藏                                 |
   | .show(speed,[callback])           | 显示速度                             |
   | .hide(speed,[callback])           | 隐藏速度                             |
   | .toggle(speed,[callback])         | 显示或者隐藏                         |
   | .slideDown(speed,[callback])      | 滑入显示                             |
   | .slideUp(speed,[callback])        | 滑出显示                             |
   | .slideToggle(speed,[callback])    | 滑动显示或者隐藏                     |
   | .fadeIn(speed,[callback])         | 淡入显示                             |
   | .fadeOut(speed,[callback])        | 淡入隐藏                             |
   | .fadeTo(speed,opacity,[callback]) | 匹配调整元素的不透明度               |
   | .animate(attr,[speed],[easing])   | 针对指定的 css 属性执行自定义动画    |
   | .animate(attr,options)            | 动画队列                             |
   | .stop([clearQueue],[jumpToEnd])   | 停止当前播放动画，然后启动排列的动画 |
   | .queue()                          | 取得第一个匹配元素上的动画队列       |
   | .queue(callback)                  | 动画队列最后添加函数                 |
   | .queue(newQueue)                  | 新队列替换原队列                     |
   | .dequeue()                        | 执行队列中的下一个动画               |

## 方法                        
   | 方法                        | 说明                                                          |
   | .attr(key)                  | 获取属性 key 的值                                             |
   | .attr(key,value)            | 设置属性 key 的值为 value                                     |
   | .attr(key,fun)              | 设置属性 key 的值为 fun 函数的返回值                          |
   | .attr(map)                  | 根据传入的键值对参数设置属性的值                              |
   | .removeAttr(key)            | 移除属性 key                                                  |
   | .addClass(class)            | 添加 css 样式                                                 |
   | .removeClass(class)         | 移除 css 样式                                                 |
   | .toggleClass(class)         | 不存在就添加，存在就删除 css                                  |
   | .hasClass(class)            | 匹配元素至少有一个包含传入的类，就返回 true                   |
   | .html()                     | 取得第一个匹配元素的 html 内容                                |
   | .html(value)                | 将每个匹配元素的 html 内容设置为传入的 value                  |
   | .text()                     | 取得所有匹配元素的文本内容，返回一个字符串                    |
   | .text(value)                | 设置每个匹配元素的文本内容为 value                            |
   | .val()                      | 取得第一个匹配元素的 value 属性的值                           |
   | .val(value)                 | 设置每个匹配元素的 value 属性值为传入的 value                 |
   | .css(key)                   | 取得 css 属性的 key 的值                                      |
   | .css(key,value)             | 设置 css 属性的 key 值为传入的 value                          |
   | .css(map)                   | 根据传入的键值对参数设置 css 属性的值                         |
   | .offset()                   | 取得第一个匹配元素相对于适口的上左坐标值（单位为像素）        |
   | .position()                 | 取得第一个匹配元素相对于.offsetParent()返回元素的上、左坐标值 |
   | .scrollTop()                | 取得第一个匹配元素的垂直滚动位置                              |
   | .scrollTop(value)           | 设置每个匹配元素的垂直滚动位置为传入的 vlaue                  |
   | .scrollLeft()               | 取得第一个匹配元素的水平滚动位置                              |
   | .scrollLeft(value)          | 设置每个匹配元素的水平滚动位置为传入的 vlaue                  |
   | .height()                   | 取得第一个匹配元素的高度                                      |
   | .height(value)              | 设置每个匹配元素的高度为传入的 value                          |
   | .width()                    | 取得第一个匹配元素的宽度                                      |
   | .width(value)               | 设置每个匹配元素的宽度为传入的 value                          |
   | .innerHeight()              | 取得第一个匹配元素的包含内边距但不包含边框的高度              |
   | .innerWidth()               | 取得第一个匹配元素的包含内边距但不包含边框的宽度              |
   | .outerHeight(includeMargin) | 取得第一个匹配元素的包含内边距、边框及可选的外边距的高度      |
   | .outWidth(includeMargin)    | 取得第一个匹配元素的包含内边距、边框及可选的外边距的宽度      |
   | .append(content)            | 在每个匹配元素内部的末尾插入 content                          |
   | .appendTo(selector)         | 将匹配的元素插入到 selector 选择符匹配的元素内部的末尾        |
   | .prepend(content)           | 在每个匹配元素内部的开头插入 content                          |
   | .prependTo(selector)        | 将匹配的元素插入到 selector 选择符匹配的元素内部的开头        |
   | .after(content)             | 在每个匹配元素的后面插入 content                              |
   | .insertAfter(selector)      | 将匹配元素插入到 selector 选择符匹配的元素的后面              |
   | .before(content)            | 在每个匹配元素的前面插入 content                              |
   | .insertBefore(selector)     | 将匹配元素插入到 selector 选择符匹配的元素的前面              |
   | .wrap(content)              | 将匹配的每个元素包装在 content 中                             |
   | .wrapAll(content)           | 将匹配的所有元素作为一个单元包装在 content 中                 |
   | .wrapInner(content)         | 将匹配的每个元素内部的内容包装在 content 中                   |
   | .replaceWith(content)       | 将匹配的元素替换成 content                                    |
   | .replaceAll(selector)       | 将 selector 选择符匹配的元素替换成匹配的元素                  |
   | .empty()                    | 移除每个匹配元素的子节点                                      |
   | .remove([selector])         | 从 dom 中移除匹配的节点，可以通过 selector 筛选               |
   | .clone([withHandlers])      | 返回所有匹配元素的副本                                        |
   | .data(key)                  | 取得与第一个匹配元素关联的 key 键的数据项                     |
   | .data(key,value)            | 设置与每个匹配元素关联的 key 键的数据项为 value               |
   | .removeData(key)            | 移除与每个匹配元素关联的 key 键的数据项                       |

prop() 方法应该用于检索属性值，例如 DOM 属性（如 selectedIndex, tagName, nodeName, nodeType, ownerDocument, defaultChecked, 和 defaultSelected）

提示：如需检索 HTML 属性，请使用 attr() 方法代替。
提示：如需移除属性，请使用 removeProp() 方法。



## AJAX方法
   | AJAX 方法                                  | 说明                                                    |
   | $.ajax(options)                            | 使用传入的 options 生成一次 ajax 请求                   |
   | .load(url,[data],[callback])               | 向传入的 url 生成一次 ajax 请求，然后将响应放入匹配元素 |
   | $.get(url,[data],[callback],[returnType])  | 使用 get 方法向传入的 url 生成一次 ajax 请求            |
   | $.getJSON(url,[data],[callback])           | 向传入的 url 生成一次请求，将响应作为 json 数据结构解析 |
   | $.getScript(url,[callback])                | 向传入的 url 生成一次请求，将响应作为 js 脚本执行       |
   | $.post(url,[data],[callback],[returnType]) | 使用 post 方法向传入的 url 生成一次 ajax 请求           |
   | .ajaxComplete(handler)                     | 绑定当任意 ajax 事务完成后调用 fun                      |
   | .ajaxError(handler)                        | 绑定当任意 ajax 事务发生错误时调用 fun                  |
   | .ajaxSend(handler)                         | 绑定当任意 ajax 事务开始时调用 fun                      |
   | .ajaxStart(handler)                        | 绑定当任意 ajax 事务开始没有其他事务还在活动时调用 fun  |
   | .ajaxStop(handler)                         | 绑定当任意 ajax 事务结束没有其他事务还在活动时调用 fun  |
   | .ajaxSuccess(handler)                      | 绑定当任意 ajax 事务成功完成时调用的程序                |
   | $.ajaxSetup(options)                       | 为后续的 ajax 事务设置默认选项                          |
   | .serialize()                               | 将一组表单控件的值编码为一个查询字符串                  |
   | .serializeArray()                          | 将一组表单控件的值编码为一个 json 数据结构              |
   | $.param(map)                               | 将任意值的映射编码为一个查询字符串                      |
## 方法或属性                     

   | 方法或属性                    | 说明                                                   |
   | $.support                     | 返回一个属性的映射，表示浏览器是否支持各种特性和标准   |
   | $.each(collection,callback)   | 迭代遍历集合，针对集合中的每一项执行回调函数           |
   | $.extend(target,addition,...) | 扩展 target 对象，即将后面传入对象的属性添加入这个对象 |
   | $.makeArray(object)           | 将对象转换为一个数组                                   |
   | $.map(array,callback)         | 针对数组中每一项执行回调函数，返回新数组               |
   | $.inArray(value,array)        | 确定数组 array 中是否包含值 value                      |
   | $.merge(array1,array2)        | 合并两个数组                                           |
   | $.unique(array)               | 从数组中移除重复的 dom 元素                            |
   | $.isFunction(object)          | 确定对象是否一个函数                                   |
   | $.trim(String)                | 从字符串末尾移除空白符                                 |
   | $.noConflict([extreme])       | 让渡$符号使用权，恢复使用 jquery 标识符                |
   | .hasClass(className)          | 确定匹配元素是否包含给定的类                           |
   | .is(selector)                 | 确定是否有匹配元素与给定的选择符表达式匹配             |
   | .each(callback)               | 迭代遍历匹配元素，针对每个元素执行回调函数             |
   | .length                       | 取得匹配元素的个数                                     |
   | .get()                        | 取得与匹配元素对应的 dom 节点的数组                    |
   | .get(index)                   | 取得匹配元素中与传入的索引值对应的 dom 节点            |
   | .index(element)               | 取得给定 dom 节点在匹配元素集合中的索引值              |

``` js
  $.each([52, 97], function(index, value) {
        alert(index + ': ' + value);
    });
```

## 获取表单数据
``` js 
 var form = new FormData();
  form.append("username","zxj");
  form.append("password",123456);
```

还能提交文件

``` js  
var form = new FormData(document.getElementById("tf"));

$('#formAddHandlingFee').serialize()
```

## ajax 提交事件

``` js 
        //ajax提交form表单的方式
        $('#formAddHandlingFee').submit(function() {
            var AjaxURL= "../OrderManagement/AjaxModifyOrderService.aspx";      
            alert($('#formAddHandlingFee').serialize());
                $.ajax({
                    type: "POST",
                    dataType: "html",
                    url: AjaxURL + '?Action=' + 'SubmitHandlingFee' + '&OrderNumber=' + $.trim($("#<%=this.txtOrderNumber.ClientID %>").val()),
                    data: $('#formAddHandlingFee').serialize(),
                    success: function (data) {
                        var strresult=data;
                        alert(strresult);
                        //加载最大可退金额
                        $("#spanMaxAmount").html(strresult);
                    },
                    error: function(data) {
                        alert("error:"+data.responseText);
                     }
                });

               //非常重要
               return false;
        }

    );
```
## 获取文件上传内容
``` js
$("#fileUpload").change(function () {
    console.log($("#fileUpload")[0].files);
});

```

## ajax 文件上传

>form 表单需要设置 enctype="multipart/form-data" 属性

### 单个文件的上传
注意：ajax实现文件上传的话用到的是：绝对路径

``` html
<!DOCTYPE html> 
<html> 
<head lang="en"> 
 <meta charset="UTF-8"> 
 <script src="https://cdn.bootcss.com/jquery/1.10.2/jquery.min.js"></script> 
</head> 
<body> 
       <form id="uploadForm" enctype="multipart/form-data"> 
             文件:<input id="file" type="file" name="file"/> 
       </form> 
            <button id="upload">上传文件</button> 
</body> 
      <script type="text/javascript"> 
             $(function () { 
               $("#upload").click(function () { 
               var formData = new FormData($('#uploadForm')[0]); 
                $.ajax({ 
                type: 'post', 
                url: "http://192.168.1.101:8080/springbootdemo/file/upload", //上传文件的请求路径必须是绝对路劲
                data: formData, 
                cache: false, 
                processData: false, 
                contentType: false, 
            }).success(function (data) { 
                alert(data); 
           }).error(function () { 
                alert("上传失败"); 
       }); 
    }); 
 }); 
</script> 
</html>
```

### Ajax实现多文件的上传 
这个是多选上传，关键是multiple="multiple"这个属性，另外使用的接口也是多文件上传的接口

    ``` html
<!DOCTYPE html> 
<html> 
<head lang="en"> 
 <meta charset="UTF-8"> 
 <script src="https://cdn.bootcss.com/jquery/1.10.2/jquery.min.js"></script> 
 <title></title> 
</head> 
<body> 
        <form id="uploadForm" enctype="multipart/form-data"> 
             文件:<input type="file" name="file" multiple="multiple"/><br> 
        </form> 
            <button id="upload">上传文件</button> 
</body> 
<script type="text/javascript"> 
         $(function () { 
             $("#upload").click(function () { 
              var formData = new FormData($('#uploadForm')[0]); 
          $.ajax({ 
          type: 'post', 
              url: "http://192.168.1.101:8080/springbootdemo/file/uploadFiles", 
              data: formData, 
              cache: false, 
              processData: false, 
              contentType: false, 
         }).success(function (data) { 
            alert(data); 
         }).error(function () { 
             alert("上传失败"); 
          }); 
     }); 
 }); 
</script> 
</html>
```



# 最佳实践

## 基础
jQuery.parent(expr)，找父亲节点，可以传入expr进行过滤，比如$("span").parent()或者$("span").parent(".class")
jQuery.parents(expr)，类似于jQuery.parents(expr),但是是查找所有祖先元素，不限于父元素
jQuery.children(expr)，返回所有子节点，这个方法只会返回直接的孩子节点，不会返回所有的子孙节点
jQuery.contents()，返回下面的所有内容，包括节点和文本。这个方法和children()的区别就在于，包括空白文本，也会被作为一个jQuery对象返回，children()则只会返回节点
jQuery.prev()，返回上一个兄弟节点，不是所有的兄弟节点
jQuery.prevAll()，返回所有之前的兄弟节点
jQuery.next()，返回下一个兄弟节点，不是所有的兄弟节点
jQuery.nextAll()，返回所有之后的兄弟节点
jQuery.siblings()，返回兄弟姐妹节点，不分前后
jQuery.find(expr)，跟jQuery.filter(expr)完全不一样：
jQuery.filter()，是从初始的jQuery对象集合中筛选出一部分，而
jQuery.find()，的返回结果，不会有初始集合中的内容，比如$("p").find("span")，是从<p>元素开始找<span>，等同于$("p span")


## jQuery 对象转换为DOM对象

   ``` js
     var $v =$("#v");    //jQuery 对象
     var v=$v[0];       //DOM 对象 
     var v=$v.get(0);   //DOM 对象 
   ```
   
## jQuery获取和设置checkbox的checked属性小结

在jquery里，有两种操作元素属性的方法，一种是attr()，另一种是prop()。

attr()的属性在页面首次加载时就确定。当页面初始状态checkbox没有选中，

("#cb1").attr("checked")为undefined，点击选中后，还是undefined，不管选中与否
(“#cb1”).attr(“checked”)始终都是undefined；当页面初试状态checkbox选中，
$(“#cb1”).attr(“checked”)为checked，之后取消选中还是checked。

prop()方法随checked属性改变而改变，选中时为true，为选中时为false。

最后，总结下获取和设置checked属性的方法。

得到选中属性
``` js
$("#id").prop("checked")
$("#id").get(0).checked)
document.getElementById("#id").checked
$("#id").is(":checked")
```

设置选中
```js
$("#id").prop("checked",true)
$("#id").get(0).checked = true
document.getElementById("#id").checked = true
```

## 4. 使用 jQuery 切换样式
``` js
     //Look for the media-type you wish to switch then set the href to your new style sheet  
     $('link[media='screen']').attr('href', 'Alternative.css');
```
    
## 5. 限制选择的区域
   ``` html
     <ul id="shopping_cart_items">  
       <li>  
         <input value="Item-X" name="item" class="is_in_stock" type="radio"> Item X</li>  
       <li>  
         <input value="Item-Y" name="item" class="3-5_days" type="radio"> Item Y</li>  
       <li>  
         <input value="Item-Z" name="item" class="unknown" type="radio"> Item Z</li>  
     </ul>
   #+end_src
   ``` js
     //Where possible, pre-fix your class names with a tag name  
     //so that jQuery doesn't have to spend more time searching  
     //for the element you're after. Also remember that anything  
     //you can do to be more specific about where the element is  
     //on your page will cut down on execution/search times  
     var in_stock = $('#shopping_cart_items input.is_in_stock');
   #+end_src
     
## 6. 如何正确使用 ToggleClass
``` js
     //Toggle class allows you to add or remove a class  
     //from an element depending on the presence of that  
     //class. Where some developers would use:  
     a.hasClass('blueButton') ? a.removeClass('blueButton') : a.addClass('blueButton');  
     //toggleClass allows you to easily do this using  
     a.toggleClass('blueButton');
```
     
## 7. 设置 IE 指定的功能
   ``` js
     if ($.browser.msie) { // Internet Explorer is a sadist. }
   ```
    
## 8. 使用 jQuery 来替换一个元素
   ``` js
     $('#thatdiv').replaceWith('fnuh');
   ```
## 9. 验证一个元素是否为空
   ``` js
     if ($('#keks').html()) { //Nothing found ;}
   ```
## 10. 在无序的 set 中查找一个元素的索引
   ``` js
     $("ul > li").click(function () {  
         var index = $(this).prevAll().length;  
     });
   ```
## 14. 使用过滤器过滤多属性
   ``` js
     var elements = $('#someid input[type=sometype][value=somevalue]').get();
   ```
## 15. 使用 jQuery 预加载图片
   ``` js
     jQuery.preloadImages = function() { for(var i = 0; i').attr('src', arguments[i]); } };  
     // Usage $.preloadImages('image1.gif', '/path/to/image2.png', 'some/image3.jpg');
   ```
## 16. 设置任何匹配一个选择器的事件处理程序
   ``` js
     $('button.someClass').live('click', someFunction);
     //Note that in jQuery 1.4.2, the delegate and undelegate options have been
     //introduced to replace live as they offer better support for context
     //For example, in terms of a table where before you would use..
     // .live()
     $("table").each(function(){
         $("td", this).live("hover", function(){
             $(this).toggleClass("hover");
         });
     });
     //Now use..
     $("table").delegate("td", "hover", function(){
         $(this).toggleClass("hover");
     });
   ```
## 17. 找到被选择到的选项(option)元素
   ``` js
     $('#someElement').find('option:selected');
   ```
## 18. 隐藏包含特定值的元素
   ``` js
     $("p.value:contains('thetextvalue')").hide();
   ```
## 19. 自动的滚动到页面特定区域
   ``` js
     jQuery.fn.autoscroll = function(selector) {
         $('html,body').animate(
             {scrollTop: $(selector).offset().top},
             500
         );
     }
     //Then to scroll to the class/area you wish to get to like this:
     $('.area_name').autoscroll();
   ```
## 20. 检测各种浏览器
   ``` js
     Detect Safari (if( $.browser.safari)),
     Detect IE6 and over (if ($.browser.msie && $.browser.version > 6 )),
     Detect IE6 and below (if ($.browser.msie && $.browser.version <= 6 )),
     Detect FireFox 2 and above (if ($.browser.mozilla && $.browser.version >= '1.8' ))
   ```
## 21. 替换字符串中的单词
   ``` js
     var el = $('#id');
     el.html(el.html().replace(/word/ig, ''));
   ```
## 22. 关闭右键的菜单
   ``` js
     $(document).bind('contextmenu',function(e){ return false; });
   ```
## 23. 定义一个定制的选择器
   ``` js
     $.expr[':'].mycustomselector = function(element, index, meta, stack){
         // element- is a DOM element
         // index - the current loop index in stack
         // meta - meta data about your selector
         // stack - stack of all elements to loop
         // Return true to include current element
         // Return false to explude current element
     };
     // Custom Selector usage:
     $('.someClasses:test').doSomething();
   ```
## 25. 使用 jQuery 判断鼠标的左右键点击
``` js
     $("#someelement").live('click', function(e) {
         if( (!$.browser.msie && e.button == 0) || ($.browser.msie && e.button == 1) ) {
             alert("Left Mouse Button Clicked");
         }
         else if(e.button == 2)
             alert("Right Mouse Button Clicked");
     });
```
## 26. 显示或者删除输入框的缺省值
``` js
     //This snippet will show you how to keep a default value
     //in a text input field for when a user hasn't entered in
     //a value to replace it
     swap_val = [];
     $(".swap").each(function(i){
         swap_val[i] = $(this).val();
         $(this).focusin(function(){
             if ($(this).val() == swap_val[i]) {
                 $(this).val("");
             }
         }).focusout(function(){
             if ($.trim($(this).val()) == "") {
                 $(this).val(swap_val[i]);
             }
         });
     });
```

   <input class="swap" type="text" value="Enter Username here.." />
## 27. 指定时间后自动隐藏或者关闭元素(1.4 支持）
   ``` js
     //Here's how we used to do it in 1.3.2 using setTimeout
     setTimeout(function() {
         $('.mydiv').hide('blind', {}, 500)
     }, 5000);
     //And here's how you can do it with 1.4 using the delay() feature (this is a lot like sleep)
     $(".mydiv").delay(5000).hide('blind', {}, 500);
   ```
## 28. 动态创建元素到 DOM
   ``` js
     var newgbin1Div = $('');
     newgbin1Div.attr('id','gbin1.com').appendTo('body');
   ```
## 29. 限制 textarea 的字符数量
   ``` js
     jQuery.fn.maxLength = function(max){
         this.each(function(){
             var type = this.tagName.toLowerCase();
             var inputType = this.type? this.type.toLowerCase() : null;
             if(type == "input" && inputType == "text" || inputType == "password"){
                 //Apply the standard maxLength
                 this.maxLength = max;
             }
             else if(type == "textarea"){
                 this.onkeypress = function(e){
                     var ob = e || event;
                     var keyCode = ob.keyCode;
                     var hasSelection = document.selection? document.selection.createRange().text.length > 0 : this.selectionStart != this.selectionEnd;
                     return !(this.value.length >= max && (keyCode > 50 || keyCode == 32 || keyCode == 0 || keyCode == 13) && !ob.ctrlKey && !ob.altKey && !hasSelection);
                 };
                 this.onkeyup = function(){
                     if(this.value.length > max){
                         this.value = this.value.substring(0,max);
                     }
                 };
             }
         });
     };
     //Usage:
     $('#gbin1textarea').maxLength(500);
   ```
## 30. 为函数创建一个基本测试用例
   ``` js
     //Separate tests into modules.
     module("Module B");
     test("some other gbin1.com test", function() {
         //Specify how many assertions are expected to run within a test.
         expect(2);
         //A comparison assertion, equivalent to JUnit's assertEquals.
         equals( true, false, "failing test" );
         equals( true, true, "passing test" );
     });
   ```
## 31. 使用 jQuery 克隆元素
   ``` js
     var cloned = $('#gbin1div').clone();
   ```
## 32. 测试一个元素在 jQuery 中是否可见
   ``` js
     if($(element).is(':visible') == 'true') { //The element is Visible }
   ```
## 33. 元素屏幕居中
   ``` js
     jQuery.fn.center = function () {
         this.css('position','absolute');
         this.css('top', ( $(window).height() - this.height() ) / +$(window).scrollTop() + 'px');
         this.css('left', ( $(window).width() - this.width() ) / 2+$(window).scrollLeft() + 'px');return this;
     }
     //Use the above function as: $('#gbin1div').center();
     34. 使用特定名字的元素对应的值生成一个数组
     var arrInputValues = new Array();
     $("input[name='table[]']").each(function(){
         arrInputValues.push($(this).val());
     });
   ```
## 35. 剔除元素中的 HTML
   ``` js
     (function($) {
         $.fn.stripHtml = function() {
             var regexp = /<("[^"]#"|'[^']#'|[^'">])#>/gi;
             this.each(function() {
                 $(this).html(
                     $(this).html().replace(regexp,"")
                 );
             });
             return $(this);
         }
     })(jQuery);
     //usage:
     $('p').stripHtml();
   ```
## 36. 使用 closest 来得到父元素
   ``` js
     $('#searchBox').closest('div');
   ```
## 37. 使用 firebug 来记录 jQuery 事件
   ``` js
     // Allows chainable logging
     // Usage: $('#someDiv').hide().log('div hidden').addClass('someClass');
     jQuery.log = jQuery.fn.log = function (msg) {
         if (console){
             console.log("%s: %o", msg, this);
         }
         return this;
     };
   ```
## 38. 点击链接强制弹出新窗口
   ``` js
     jQuery('a.popup').live('click', function(){
         newwindow=window.open($(this).attr('href'),'','height=200,width=150');
         if (window.focus) {newwindow.focus()}
         return false;
     });
   ```
## 39. 点击链接强制打开新标签页
   ``` js
     jQuery('a.newTab').live('click', function(){
         newwindow=window.open($(this).href);
         jQuery(this).target = "_blank";
         return false;
     });
   ```
## 40. 使用 siblings()来处理同类元素
   ``` js
     // Rather than doing this
     $('#nav li').click(function(){
         $('#nav li').removeClass('active');
         $(this).addClass('active');
     });
     // Do this instead
     $('#nav li').click(function(){
         $(this).addClass('active').siblings().removeClass('active');
     });
   ```
## 41. 选择或者不选页面上全部复选框
   ``` js
     var tog = false; // or true if they are checked on load
     $('a').click(function() {
         $("input[type=checkbox]").attr("checked",!tog);
         tog = !tog;
     });
   ```
## 42. 基于输入文字过滤页面元素
   ``` js
     //If the value of the element matches that of the entered text
     //it will be returned
     $('.gbin1Class').filter(function() {
         return $(this).attr('value') == $('input#gbin1Id').val() ;
     })
   ```
## 43. 取得鼠标的 X 和 Y 坐标
   ``` js
     $(document).mousemove(function(e){
         $(document).ready(function() {
             $().mousemove(function(e){
                 $('#XY').html("Gbin1 X Axis : " + e.pageX + " | Gbin1 Y Axis " + e.pageY);
             });
         });
   ```
## 44. 使得整个列表元素(LI)可点击
   ``` js
     $("ul li").click(function(){
         window.location=$(this).find("a").attr("href"); return false;
     });
   ```
## 45. 使用 jQuery 来解析 XML
   ``` js
     function parseXml(xml) {
         //find every Tutorial and print the author
         $(xml).find("Tutorial").each(function()
                                      {
                                          $("#output").append($(this).attr("author") + "");
                                      });
     }
   ```
## 46. 判断一个图片是否加载完全
   ``` js
     $('#theGBin1Image').attr('src', 'image.jpg').load(function() {
         alert('This Image Has Been Loaded');
     });
   ```
## 47. 使用 jQuery 命名事件
   ``` js
     //Events can be namespaced like this
     $('input').bind('blur.validation', function(e){
         // ...
     });
     //The data method also accept namespaces
     $('input').data('validation.isValid', true);
   ```
## 48. 判断 cookie 是否激活或者关闭
   ``` js
     var dt = new Date();
     dt.setSeconds(dt.getSeconds() + 60);
     document.cookie = "cookietest=1; expires=" + dt.toGMTString();
     var cookiesEnabled = document.cookie.indexOf("cookietest=") != -1;
     if(!cookiesEnabled)
     {
         //cookies have not been enabled
     }
   ```
## 49. 强制过期 cookie
   ``` js
     var date = new Date();
     date.setTime(date.getTime() + (x # 60 # 1000));
     $.cookie('example', 'foo', { expires: date });
   ```
## 50. 使用一个可点击的链接替换页面中所有 URL
   ``` js
     $.fn.replaceUrl = function() {
         var regexp = /((ftp|http|https)://(w+:{0,1}w#@)?(S+)(:[0-9]+)?(/|/([w#!:.?+=&%@!-/]))?)/gi;
     this.each(function() {
         $(this).html(
             $(this).html().replace(regexp,'<a href="$1">$1</a>')
         );
     });
     return $(this);
     }
     //usage
     $('#GBin1div').replaceUrl();
   ```
## 51: 在表单中禁用“回车键”
   大家可能在表单的操作中需要防止用户意外的提交表单，那么下面这段代码肯定非常有帮助：
   ``` js
     $("#form").keypress(function(e) {
         if (e.which == 13) {
             return false;
         }
     });
   ```
## 52: 清除所有的表单数据
   可能针对不同的表单形式，你需要调用不同类型的清楚方法，不过使用下面这个现成方法，绝对能让你省不少功夫。
   ``` js
     function clearForm(form) {
         // iterate over all of the inputs for the form
         // element that was passed in
         $(':input', form).each(function() {
             var type = this.type;
             var tag = this.tagName.toLowerCase(); // normalize case
             // it's ok to reset the value attr of text inputs,
             // password inputs, and textareas
             if (type == 'text' || type == 'password' || tag == 'textarea')
                 this.value = "";
             // checkboxes and radios need to have their checked state cleared
             // but should #not# have their 'value' changed
             else if (type == 'checkbox' || type == 'radio')
                 this.checked = false;
             // select elements need to have their 'selectedIndex' property set to -1
             // (this works for both single and multiple select elements)
             else if (tag == 'select')
                 this.selectedIndex = -1;
         });
     };
   ```
## 53: 将表单中的按钮禁用

   下面的代码对于 ajax 操作非常有用，你可以有效的避免用户多次提交数据，个人也经常使用：
   ``` js
     $("#somebutton").attr("disabled", true);//禁用按钮
     $("#submit-button").removeAttr("disabled");//启动按钮
   ```
   可能大家往往会使用.attr(‘disabled’,false);，不过这是不正确的调用。
## 54: 输入内容后启用递交按钮
   这个代码和上面类似，都属于帮助用户控制表单递交按钮。使用这段代码后，递交按钮只有在用户输入指定内容后才可以启动。
   ``` js
     $('#username').keyup(function() {
         $('#submit').attr('disabled', !$('#username').val()); 
     });
   ```
## 55: 禁止多次递交表单
   多次递交表单对于 web 应用来说是个比较头疼的问题，下面的代码能够很好的帮助你解决这个问题：
   ``` js
     $(document).ready(function() {
         $('form').submit(function() {
             if(typeof jQuery.data(this, "disabledOnSubmit") == 'undefined') {
                 jQuery.data(this, "disabledOnSubmit", { submited: true });
                 $('input[type=submit], input[type=button]', this).each(function() {
                     $(this).attr("disabled", "disabled");
                 });
                 return true;
             }
             else
             {
                 return false;
             }
         });
     });
   ```
## 56: 高亮显示目前聚焦的输入框标示
   有时候你需要提示用户目前操作的输入框，你可以使用下面代码高亮显示标示：
   ``` js
     $("form :input").focus(function() {
         $("label[for='" + this.id + "']").addClass("labelfocus");
     }).blur(function() {
         $("label").removeClass("labelfocus");
     });
   ```
## 57: 动态方式添加表单元素
   这个方法可以帮助你动态的添加表单中的元素，比如，input 等：
   ``` js
     //change event on password1 field to prompt new input
     $('#password1').change(function() {
         //dynamically create new input and insert after password1
         $("#password1").append("<input id="password2" name="password2" type="text" />");
     });
   ```
## 自动将数据导入 selectbox 中

   下面代码能够使用 ajax 数据自动生成选择框的内容

   ``` js
     $(function(){
         $("select#ctlJob").change(function(){
             $.getJSON("/select.php",{id: $(this).val(), ajax: 'true'}, function(j){
                 var options = '';
                 for (var i = 0; i < j.length; i++) {
                     options += '' + j[i].optionDisplay + '';
                 }
                 $("select#ctlPerson").html(options);
             })
         })
     })
   ```
## 59: 判断一个复选框是否被选中
   ``` js
     $('#checkBox').attr('checked');
   ```
## 60: 使用代码来递交表单
   ``` js
   $("#myform").submit();
   ```
