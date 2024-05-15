Flask 是一个轻量级的 Python Web 框架，用于快速开发 Web 应用程序。它被称为微框架，因为它的核心非常简单，但是可以通过各种扩展来实现更复杂的功能。Flask 是一个非常受欢迎的框架，因为它易于学习、灵活性强、文档完善，并且可以用于开发各种规模的 Web 应用程序。

下面是 Flask 的基本用法：

1. **安装 Flask：** 首先，您需要安装 Flask。可以使用 pip 工具来安装 Flask：

    ```
    pip install Flask
    ```

2. **创建应用：** 在您的项目目录中，创建一个 Python 文件，例如 `app.py`，然后导入 Flask：

    ```python
    from flask import Flask
    ```

    创建 Flask 应用：

    ```python
    app = Flask(__name__)
    ```

3. **定义路由：** 使用 `@app.route` 装饰器来定义路由，即指定 URL 和相应的处理函数：

    ```python
    @app.route('/')
    def index():
        return 'Hello, World!'
    ```

    在上面的例子中，当访问根 URL（`/`）时，会执行 `index` 函数，并返回 `'Hello, World!'`。

4. **运行应用：** 在应用文件的末尾，添加如下代码以运行 Flask 应用：

    ```python
    if __name__ == '__main__':
        app.run(debug=True)
    ```

    这将启动 Flask 的开发服务器，并在调试模式下运行应用。

5. **访问应用：** 在终端中执行 `python app.py` 启动应用后，在浏览器中访问 `http://127.0.0.1:5000/`，就可以看到 `'Hello, World!'` 的消息了。

以上是 Flask 的基本用法，您可以根据需要添加更多功能，如模板、表单、数据库操作等。Flask 的官方文档提供了丰富的资源和示例，以帮助您更好地了解和使用 Flask。