---
layout: default
toc: false
title: VS Code
date:  2025-01-04T13:55:48+08:00
---


## 本地配置 .vscode

- settings.json：这个文件包含了项目的设置选项。
- launch.json：这个文件用于配置调试器。
- tasks.json：这个文件用于定义和配置任务（Tasks）
- extensions.json：这个文件用于记录项目所依赖的扩展插件。
- sconfig.json（对于 JavaScript/TypeScript 项目）：这个文件用于配置 JavaScript 或 TypeScript 项目的编译选项、语言服务设置等
- C:\Users\Administrator\AppData\Roaming\Code\User\keybindings.json  : 键盘快捷键

## 多光标操作

进入块选择模式：
按下 Ctrl + v 进入 Visual Block Mode（可视块模式）。

编辑块内的内容：

插入文本：按下 I 进入插入模式，然后开始输入文本。输入的文本会插入到所选区域的每一行。
追加文本：按下 A 进入插入模式，光标会移到所选区域的行尾，你可以在该区域末尾追加文本。
删除文本：按下 d 来删除选择的区域。
替换文本：按下 r 后，再输入一个字符，将块区域内的字符替换为该字符。