## 2024-06-05

项目 目录 

content\
public\ 
resources\
static\
themes\
config.toml


页面 首页:

themes: 
head : title  思维 


子页面
/mnt/j/me/blog/themes/even/layouts/partials/head.html
/mnt/j/me/blog/themes/even/layouts/partials/slideout.html 这是是手机端适配的 页面
/mnt/j/me/blog/themes/even/layouts/partials/header.html
/mnt/f/me/blog/themes/even/layouts/partials/footer.html
/mnt/f/me/blog/themes/even/layouts/partials/footer.html

这个才是最终调用的列表页，里面会引入 上面的子页面作为集成
这个页面在 _defualt目录，有默认baseof.html ,然后是自己创建的菜单。。。 等等
/mnt/f/me/blog/themes/even/layouts/_default/baseof.html  
/mnt/f/me/blog/themes/even/layouts/_default/information.html  


/mnt/f/me/blog/themes/even/layouts/post/single.html
这个是文章详情页面,里面引入的也是上面的分页面 ,和 文件内容 {{ .Content }}

