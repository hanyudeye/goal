## 搭建环境

- flutter doctor  检查环境
- flutter upgrade 更新

##  创建应用

flutter create APP_NAME

 
Flutter 是 Google 开发的开源 UI 软件开发工具包，用于构建跨平台的应用程序（Android、iOS、Web、桌面等）。Flutter 的核心是 Dart 语言，它允许开发者用单一代码库来创建漂亮的、响应迅速的应用。

下面是一个简单的 **Flutter 入门教程**，帮助你快速了解如何开始使用 Flutter 开发应用。

### 1. **安装 Flutter SDK**

#### 1.1 安装 Flutter
你需要安装 Flutter SDK 来开始开发。以下是安装步骤：

- **Windows：**
  1. 下载 Flutter SDK：[Flutter 官网](https://flutter.dev/docs/get-started/install)
  2. 解压缩文件到某个目录（例如 `C:\src\flutter`）。
  3. 将 `flutter/bin` 路径添加到你的环境变量中。
  4. 打开命令行窗口，运行 `flutter doctor` 来检查是否有缺少的依赖项。

- **macOS：**
  1. 下载并解压 Flutter SDK。
  2. 将 `flutter/bin` 路径添加到你的环境变量中。
  3. 使用终端运行 `flutter doctor` 来检查安装状况。

- **Linux：**
  1. 下载并解压 Flutter SDK。
  2. 将 `flutter/bin` 路径添加到环境变量中。
  3. 在终端中运行 `flutter doctor` 来检查。

#### 1.2 安装 Android Studio 或 Visual Studio Code
- Flutter 推荐使用 **Android Studio** 或 **Visual Studio Code**（VSCode）作为开发环境。
- 在 **Android Studio** 中安装 Flutter 和 Dart 插件，或者在 **VSCode** 中安装 Flutter 插件。

### 2. **创建一个 Flutter 项目**

1. **打开终端/命令行工具**，进入你希望保存项目的文件夹。
2. 使用以下命令创建一个新的 Flutter 项目：

   ```bash
   flutter create my_first_app
   ```

   其中 `my_first_app` 是项目名称，你可以根据自己的需要更改名称。

3. 进入项目目录：

   ```bash
   cd my_first_app
   ```

4. 使用以下命令启动项目：

   ```bash
   flutter run
   ```

   如果你连接了 Android 模拟器或设备，Flutter 将自动启动你的应用。

### 3. **Flutter 项目的结构**

Flutter 项目中包含多个文件和文件夹，以下是常见的一些结构：

- `lib/`：存放 Dart 源代码的文件夹。主要编写 Flutter 应用的界面和逻辑。
- `pubspec.yaml`：这是项目的配置文件，管理项目的依赖、资源等。
- `ios/` 和 `android/`：分别存放 iOS 和 Android 原生代码和配置文件。

### 4. **编写第一个 Flutter 应用**

在 `lib/main.dart` 文件中，你会看到一个简单的示例应用。你可以修改它并了解 Flutter 如何工作。

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Flutter Demo Home Page'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(
              'You have pushed the button this many times:',
            ),
            Text(
              '$_counter',
              style: Theme.of(context).textTheme.headline4,
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: Icon(Icons.add),
      ),
    );
  }
}
```

#### 代码解析：
- `runApp()`：启动 Flutter 应用。
- `MyApp`：应用的根组件。
- `MaterialApp`：应用的基本框架，包含了导航、主题等。
- `Scaffold`：提供了一个应用的结构，包括应用栏、内容区域和浮动按钮。
- `StatefulWidget`：这是一种可变的组件，允许组件的状态在用户交互时更新。

### 5. **常用的 Flutter 组件**

Flutter 提供了丰富的 UI 组件。以下是一些常用的组件：

- **Text**：用于显示文本。
- **Container**：用于创建矩形的容器，可以设置宽高、颜色、边框等属性。
- **Column/Row**：用于垂直或水平排列子组件。
- **Stack**：允许子组件重叠显示。
- **Scaffold**：提供基本的页面结构。
- **ListView**：用于显示可滚动的列表。
- **TextField**：用于输入文本。
- **Image**：用于显示图像。

#### 示例：简单的布局

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: Text('Simple Layout')),
        body: Column(
          children: <Widget>[
            Container(
              padding: EdgeInsets.all(20),
              color: Colors.blue,
              child: Text('First Container'),
            ),
            Container(
              padding: EdgeInsets.all(20),
              color: Colors.green,
              child: Text('Second Container'),
            ),
          ],
        ),
      ),
    );
  }
}
```

### 6. **Flutter 热重载**

Flutter 提供了强大的 **热重载** 功能。每当你修改代码并保存时，Flutter 会自动重新加载应用，只更新修改过的部分，而无需重新启动整个应用。

### 7. **调试与日志**

在开发过程中，Flutter 提供了多种调试工具：
- **Flutter DevTools**：是 Flutter 提供的一个集成的调试工具集，包含性能分析、UI 检查、网络请求调试等功能。
- **调试日志**：可以使用 `print()` 来输出调试信息。输出信息可以在终端或 Android Studio 的日志面板中看到。

### 8. **打包应用**

当你准备好发布你的应用时，可以将 Flutter 应用打包成 APK 或 IPA 文件。

#### 打包 Android 应用：
```bash
flutter build apk
```

#### 打包 iOS 应用：
```bash
flutter build ios
```

### 总结：
Flutter 是一个强大的跨平台开发工具，可以帮助你用一套代码实现多平台的应用。通过以上步骤，你可以快速上手，开始创建自己的 Flutter 应用。随着你对 Flutter 的深入了解，你可以探索更多功能，例如状态管理、网络请求、插件开发等。