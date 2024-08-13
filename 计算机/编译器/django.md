
## 安装
``` sh
pip install django
```

## 开始一个新项目
要开始一个新的 Django项目，运行下面的命令：

到目前为止，我们终于可以开始一个新的 Django 项目了，运行下面的命令，创建一个 Django 项目：
``` sh 
django-admin startproject myproject
```

## 运行开发服务器
为了确保项目创建成功并且可以正常运行，进入项目目录并启动开发服务器：
```sh
cd myproject
python manage.py runserver
```
打开浏览器并访问 http://127.0.0.1:8000/，你应该会看到Django的欢迎页面。

## 创建Django应用

在Django中，项目可以包含多个应用。应用是一个功能模块，例如博客、商城等。你可以使用以下命令创建一个新的应用：

``` sh
python manage.py startapp myapp
```

将 myapp 替换为你的应用名称。创建完成后，项目结构会变为：
```
myproject/
    manage.py
    myproject/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    myapp/
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py
        migrations/
            __init__.py
```

## 6. 注册应用
在 myproject/settings.py 文件中，找到 INSTALLED_APPS 列表，并添加你的应用：
```
INSTALLED_APPS = [
    ...
    'myapp',
]
```

## 7. 配置URL
在 myproject/urls.py 文件中，将应用的URL包含进来：
``` py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
]
```
然后，在你的应用目录 myapp 中，创建一个 urls.py 文件：
```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```
在 views.py 文件中定义一个简单的视图函数：
```py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the myapp index.")
```

## 8. 运行开发服务器
再次运行开发服务器：
```sh
python manage.py runserver
```
然后在浏览器中访问 http://127.0.0.1:8000/myapp/，你应该会看到 "Hello, world. You're at the myapp index."。