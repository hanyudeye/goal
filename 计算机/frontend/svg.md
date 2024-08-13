SVG(可缩放矢量图形)

包含属性 : width ,height，viewBox

## 画圆

```html
<svg width="100" height="100">
<circle cx="50" cy="50" r="40" style="fill:red; stroke:black;stroke-width: 3;"
</svg>
```
stroke: 笔画

## viewBox

> 用来确定 SVG 元素如何在给定的区域内进行缩放和定位。

viewBox 属性通常以四个数值组成：min-x min-y width height，其中：

min-x 是视口中可见区域的左上角 x 坐标，可以使用复数控制位移。
min-y 是视口中可见区域的左上角 y 坐标，可以使用复数控制位移。
width 是视口的宽度。
height 是视口的高度。

举例：

```html
<svg width="200" height="200" viewBox="0 0 100 100">
  <rect x="10" y="10" width="80" height="80" fill="blue" />
</svg>

```