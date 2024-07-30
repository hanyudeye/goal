1. 使用 epub.js 读取 epub 文件，并把读取的内容渲染成html 格式输出到浏览器
2. 解压缩的 epub 是 html 、css、图形和媒体的集合，并标准化了目录


## start

1. 先要使用 JSZip 库 解压 .epub文件

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.1.5/jszip.min.js"></script>
```

2. 然后 引入 epub.js 库
``` html
<script src="../dist/epub.min.js"></script>
```

3. 设置要渲染的元素:
``` html
<div id="area"></div>
```

4. 