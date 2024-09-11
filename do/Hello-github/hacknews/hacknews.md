要制作一个简单的 Hacker News 克隆站，你可以使用 PHP 和一个数据库（例如 MySQL）来构建一个基础的新闻聚合网站。这个项目将包括以下主要功能：

1. 用户可以查看最新的新闻列表。
2. 用户可以提交新闻。
3. 用户可以对新闻进行投票。
4. 用户可以查看新闻详情页并发表评论。

### 项目结构

我们将构建以下结构的项目：

```
/hacknews-clone
    ├── index.php          # 首页，显示新闻列表
    ├── submit.php         # 提交新闻页面
    ├── news.php           # 新闻详情页和评论页面
    ├── vote.php           # 投票处理脚本
    ├── config.php         # 数据库配置文件
    └── database.sql       # 数据库结构文件
```

### 1. 创建数据库

首先，创建一个名为 `hacknews` 的数据库，并在其中创建以下表结构。在 MySQL 数据库中运行以下 SQL 脚本（保存为 `database.sql` 文件）：

```sql
CREATE DATABASE hacknews;

USE hacknews;

CREATE TABLE news (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    url VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    votes INT DEFAULT 0
);

CREATE TABLE comments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    news_id INT,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (news_id) REFERENCES news(id)
);
```

### 2. 配置文件 (`config.php`)

创建一个配置文件 `config.php`，用于数据库连接设置：

```php
<?php
$servername = "localhost";
$username = "root";   // 替换为你的数据库用户名
$password = "";       // 替换为你的数据库密码
$dbname = "hacknews";

// 创建数据库连接
$conn = new mysqli($servername, $username, $password, $dbname);

// 检查连接
if ($conn->connect_error) {
    die("连接失败: " . $conn->connect_error);
}
?>
```

### 3. 创建首页 (`index.php`)

`index.php` 显示新闻列表，并提供投票按钮。

```php
<?php
require 'config.php';

// 获取新闻列表，按投票数排序
$sql = "SELECT * FROM news ORDER BY votes DESC";
$result = $conn->query($sql);
?>

<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <title>Hacker News Clone</title>
</head>
<body>
    <h1>Hacker News Clone</h1>
    <a href="submit.php">提交新闻</a>
    <hr>

    <?php while($row = $result->fetch_assoc()): ?>
        <div>
            <a href="<?php echo $row['url']; ?>"><?php echo $row['title']; ?></a>
            <br>
            <a href="vote.php?id=<?php echo $row['id']; ?>">投票</a> | 
            <a href="news.php?id=<?php echo $row['id']; ?>">评论</a>
            (<?php echo $row['votes']; ?> votes)
        </div>
        <hr>
    <?php endwhile; ?>

</body>
</html>

<?php $conn->close(); ?>
```

### 4. 提交新闻页面 (`submit.php`)

用户可以通过此页面提交新的新闻。

```php
<?php
require 'config.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $title = $_POST['title'];
    $url = $_POST['url'];

    $stmt = $conn->prepare("INSERT INTO news (title, url) VALUES (?, ?)");
    $stmt->bind_param("ss", $title, $url);
    $stmt->execute();
    $stmt->close();

    header("Location: index.php");
    exit();
}
?>

<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <title>提交新闻</title>
</head>
<body>
    <h1>提交新闻</h1>
    <form method="post">
        标题: <input type="text" name="title" required><br>
        URL: <input type="url" name="url" required><br>
        <input type="submit" value="提交">
    </form>
    <a href="index.php">返回首页</a>
</body>
</html>
```

### 5. 新闻详情页面 (`news.php`)

用户可以查看新闻的详情并添加评论。

```php
<?php
require 'config.php';

$news_id = $_GET['id'];

// 获取新闻详情
$sql = "SELECT * FROM news WHERE id = $news_id";
$news_result = $conn->query($sql);
$news = $news_result->fetch_assoc();

// 获取评论
$sql = "SELECT * FROM comments WHERE news_id = $news_id ORDER BY created_at DESC";
$comments_result = $conn->query($sql);

// 处理评论提交
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $content = $_POST['content'];

    $stmt = $conn->prepare("INSERT INTO comments (news_id, content) VALUES (?, ?)");
    $stmt->bind_param("is", $news_id, $content);
    $stmt->execute();
    $stmt->close();

    header("Location: news.php?id=" . $news_id);
    exit();
}
?>

<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <title><?php echo $news['title']; ?> - 详情</title>
</head>
<body>
    <h1><?php echo $news['title']; ?></h1>
    <p><a href="<?php echo $news['url']; ?>"><?php echo $news['url']; ?></a></p>

    <hr>
    <h2>评论</h2>
    <form method="post">
        <textarea name="content" required></textarea><br>
        <input type="submit" value="提交评论">
    </form>

    <hr>
    <?php while($comment = $comments_result->fetch_assoc()): ?>
        <p><?php echo $comment['content']; ?> - <?php echo $comment['created_at']; ?></p>
        <hr>
    <?php endwhile; ?>

    <a href="index.php">返回首页</a>
</body>
</html>

<?php $conn->close(); ?>
```

### 6. 投票处理脚本 (`vote.php`)

用户可以对新闻进行投票，增加其投票数。

```php
<?php
require 'config.php';

$news_id = $_GET['id'];

// 更新新闻的投票数
$sql = "UPDATE news SET votes = votes + 1 WHERE id = $news_id";
$conn->query($sql);

header("Location: index.php");
exit();
?>
```

### 如何运行项目

1. **设置数据库**：在你的 MySQL 数据库中运行 `database.sql` 文件中的脚本。
2. **配置数据库连接**：修改 `config.php` 中的数据库配置，填写你自己的数据库信息。
3. **将项目文件放在服务器上**：确保所有 PHP 文件都在你的 Web 服务器上运行，如 Apache 或 Nginx。
4. **打开浏览器**：访问 `index.php`，开始使用你的 Hacker News 克隆站。

### 功能扩展

这个基础项目可以扩展以下功能：

1. **用户注册和登录**：实现用户系统，允许用户注册、登录和管理自己提交的新闻。
2. **新闻分类**：支持多种类型的新闻分类（如技术、娱乐、新闻等）。
3. **页面美化**：使用 CSS 和 JavaScript 增加页面的美观度和交互性。
4. **搜索功能**：支持用户按关键词搜索新闻。

这个简单的克隆站项目是一个很好的起点，你可以根据自己的需求和想法进行进一步的开发和完善。