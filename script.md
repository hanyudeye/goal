## 1. 删除 git 仓库中提交的文件

``` bash
git remove -f  删除文件
```

调用 find 
``` bash
find . -name "*.pyc"  -exec git rm -f {} \;

```

