## i3wm 高分辨率显示器配置缩放
 
 You can create ~/.Xresources
 
 Xft.dpi:180

使用 96 的整数倍通常效果最好，例如 192 表示 200% 缩放

xdpyinfo|grep -B 2 resolution
此命令可以提供推荐值


## 应用程序在高分辨率屏幕进行缩放

Exec=netease-cloud-music --force-device-scale-factor=2 %U
