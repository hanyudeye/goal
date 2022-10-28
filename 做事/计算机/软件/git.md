

## 初始化配置

```
git config --global user.email XX
git config --global user.name XX
```
## 创建 ssh key

ssh-keygen -t rsa -C XX 

测试  ssh-v git@github.com

## 中文文件名乱码
git 默认中文文件名是 \xxx\xxx 等八进制形式，是因为 对0x80以上的字符进行quote。

只需要设置core.quotepath设为false，就不会对0x80以上的字符进行quote。中文显示正常

git config --global core.quotepath false

## question
### git 取消对文件的跟踪
git rm 
### git 排除入库的文件
对于已入库的文件，取消状态跟踪
命令：git update-index –assume-unchanged FILENAME 路径+文件名

# github
- 趋势 https://github.com/trending

## 一些问题
### fatal: protocol 'https' is not supported
当你使用 Ctrl +v 在终端粘贴的时候，不会成功，但会粘贴一个隐藏的符号 ^? ， 删除掉就可以了。

## 代码仓库  github

- [热门](https://github.com/trending)
- [专题](https://github.com/topics)

搜索
``` 
优秀项目  Awesome + 关键字  
stars: fork
qt in:name：表示在项目名称中搜索 qt 关键字
qt in:readme：表示在项目 readme 中搜索 qt 关键字
qt in:description：表示在 项目描述中搜索 qt 关键字
qt in:USERNAME：表示在 USERNAME 中搜索 qt 关键字
qt in:ORGNAME：表示在组织或机构名中搜索 qt 关键字
size:>=5000 Qt ：搜索大小超过 5M 的包含 Qt 关键字项目
language:C++ location:china 搜索国内的开发者，语言限定为 C++
``` 
后缀
```
stars:>20 extension:el language:elisp
```

