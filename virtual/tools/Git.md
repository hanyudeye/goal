# Git
<!-- GFM-TOC -->
- [Git](#git)
  - [集中式与分布式](#集中式与分布式)
  - [submodule](#submodule)
<!-- GFM-TOC -->


## 集中式与分布式

Git 属于分布式版本控制系统，而 SVN 属于集中式。

1. 什么是集中式？ 集中在一个地方，就是 一个服务器电脑?
2. 什么是分布式？ 分散在多台电脑。
3. 每次pull ，push 都组织成工作流的一部分
4. 使用HEAD指针指向当前分支的最新时间线
5. 新建提交时，当前分支的指针要向前移动
6. git 仓库传输使用 SSH 加密，

创建秘钥
```
$ ssh-keygen -t rsa -C "youremail@example.com"
```

然后把公钥 id_rsa.pub 的内容复制到 Github "Account settings" 的 SSH Keys 中。

7. 使用 .gitignore 文件来忽略版本文件

## submodule

git submodule add --depth=1   URL
git submodule update --remote -merge