1. 
## Tutorials 1

### 基础概念

1. **Workflow**：自动化过程的定义。
2. **Job**：工作流中独立执行的一组任务。
3. **Step**：Job 中的单个任务，可以是运行命令或执行操作。
4. **Action**：可重复使用的任务，可以由社区共享或自己创建。

### 创建第一个 Workflow

#### 步骤 1：创建仓库

如果还没有 GitHub 仓库，先创建一个。

#### 步骤 2：创建工作流文件

在你的仓库中，导航到 `.github/workflows` 目录。如果没有该目录，请创建一个。

在该目录下创建一个新的 YAML 文件，例如 `ci.yml`。

#### 步骤 3：编写工作流文件

以下是一个简单的工作流示例，当代码推送到主分支时运行：

```yaml
name: CI

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up Node.js
      uses: actions/setup-node@v2
      with:
        node-version: '14'

    - name: Install dependencies
      run: npm install

    - name: Run tests
      run: npm test
```

#### 步骤 4：提交工作流文件

将该文件提交到你的仓库中：

```sh
git add .github/workflows/ci.yml
git commit -m "Add CI workflow"
git push
```

#### 步骤 5：查看工作流运行情况

提交后，转到你的 GitHub 仓库页面，点击 "Actions" 选项卡。你应该可以看到刚刚创建的工作流开始运行。

### 深入了解

#### 1. **环境变量**

你可以在工作流文件中使用环境变量：

```yaml
env:
  NODE_ENV: production
```

#### 2. **触发器**

除了 `push`，你还可以使用其他事件触发工作流，例如 `pull_request`、`schedule`、`workflow_dispatch` 等：

```yaml
on:
  pull_request:
    branches:
      - main

  schedule:
    - cron: '0 0 * * *'
```

#### 3. **自定义 Action**

你可以创建自己的 Action，并在工作流中使用。创建一个新的仓库或目录，添加 `action.yml` 文件：

```yaml
name: 'My Custom Action'
description: 'An example custom action'
inputs:
  exampleInput:
    description: 'An example input'
    required: true
    default: 'Hello, World!'

runs:
  using: 'node12'
  main: 'index.js'
```

然后，在你的工作流中使用这个 Action：

```yaml
steps:
- name: Use custom action
  uses: ./path-to-your-action
  with:
    exampleInput: 'Custom input'
```

### 资源

- **官方文档**: [GitHub Actions Documentation](https://docs.github.com/en/actions)
- **教程和指南**:
  - [GitHub Actions 简介](https://docs.github.com/cn/actions/learn-github-actions/introduction-to-github-actions)
  - [深入了解 GitHub Actions](https://docs.github.com/cn/actions/learn-github-actions/understanding-github-actions)
- **社区 Actions**: [GitHub Marketplace](https://github.com/marketplace?type=actions)

通过这些资源和步骤，你可以快速上手并充分利用 GitHub Actions 来自动化你的开发工作流。