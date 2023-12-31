---
layout: default
toc: false
title: unix命令
date:  2023-12-16T18:10:15+08:00
categories: ['']
---

## 可编程计算机 依赖  **软件** 执行任务

## 文件 (软件和文件)

软件：
 - 查看文件  cat 
 - 拷贝文件 cp
 - 删除 rm
 - 列出文件目录  ls,list
 - 编辑文件 ed，emacs
 - 分割文件  split 
 - 内容查找 grep
 - 内容删除, 将每个文件中行的选定部分打印到标准输出 cut
 - 截取每一行的第3个字符 cut -b 3 (-c 能匹配中文，而 -b 会乱码)
 - 排序 sort 
 - 去重 uniq
 - 合并 join

## 进程

- 查看进程 ps
- 查看进程树 pstree
- 查看占用端口的进程 netstat -anp | grep port
### 进程状态

| 状态 | 说明 |
| :---: | --- |
| R | running or runnable (on run queue)<br>正在执行或者可执行，此时进程位于执行队列中。|
| D | uninterruptible sleep (usually I/O)<br>不可中断阻塞，通常为 IO 阻塞。 |
| S | interruptible sleep (waiting for an event to complete) <br> 可中断阻塞，此时进程正在等待某个事件完成。|
| Z | zombie (terminated but not reaped by its parent)<br>僵死，进程已经终止但是尚未被其父进程获取信息。|
| T | stopped (either by a job control signal or because it is being traced) <br> 结束，进程既可以被作业控制信号结束，也可能是正在被追踪。|

## 定时任务软件

at,crontab

## 系统服务软件 service

## centos

- 查看系统版本 cat /etc/issue 或 cat /etc/redhat-release

