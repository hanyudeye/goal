1. 可用镜像站   https://hub.geekery.cn


 在 Windows 下安装 Docker 并配置中国的镜像可以通过以下步骤进行：

### 1. 安装 Docker Desktop

1. **下载 Docker Desktop**：
   - 访问 [Docker Desktop 官网](https://www.docker.com/products/docker-desktop) 下载适合 Windows 的安装包。

2. **安装 Docker Desktop**：
   - 运行下载的安装程序，按照提示完成安装。
   - 安装完成后，启动 Docker Desktop。根据提示启用 WSL 2（Windows Subsystem for Linux 2）。

3. **检查 Docker 是否安装成功**：
   - 打开命令提示符（CMD）或 PowerShell，运行以下命令：
     ```bash
     docker --version
     ```
   - 如果成功安装，会显示 Docker 的版本信息。

### 2. 配置国内镜像

由于 Docker Hub 在中国的访问速度较慢，可以配置使用国内的镜像源。

#### 2.1 使用 Docker Desktop GUI 配置镜像

1. **打开 Docker Desktop**。
2. **点击设置（Settings）**：
   - 在 Docker Desktop 的右上角，点击齿轮图标进入设置页面。
3. **选择 "Docker Engine"**：
   - 在左侧菜单中选择 "Docker Engine"。
4. **修改配置**：
   - 在 JSON 配置中，将 `registry-mirrors` 添加国内镜像地址。以下是一些常用的国内 Docker 镜像源：
     - **阿里云**：`https://<你的阿里云账号>.mirror.aliyuncs.com`
     - **网易**：`https://hub-mirror.c.163.com`
     - **腾讯云**：`https://mirror.ccs.tencentyun.com`
   - 修改后的配置示例：
     ```json
     {
       "registry-mirrors": [
         "https://hub-mirror.c.163.com"
       ]
     }
     ```
5. **点击 "Apply & Restart"** 以应用更改并重启 Docker。

#### 2.2 手动配置镜像（适用于 Windows 10 Pro 和 Enterprise 版本）

如果你使用的是 Windows 10 Pro 或 Enterprise，可以手动编辑配置文件。

1. **打开 PowerShell 作为管理员**，并创建或编辑 `daemon.json` 文件：
   ```bash
   notepad.exe C:\ProgramData\Docker\config\daemon.json
   ```
2. **添加或修改镜像源**：
   ```json
   {
     "registry-mirrors": [
       "https://hub-mirror.c.163.com"
     ]
   }
   ```
3. **保存并关闭文件**。

4. **重启 Docker 服务**：
   ```bash
   Restart-Service docker
   ```

### 3. 测试镜像配置

1. **拉取一个镜像**：
   - 在命令提示符或 PowerShell 中运行以下命令测试是否能够使用国内镜像源快速拉取镜像：
     ```bash
     docker pull hello-world
     ```

2. **运行镜像**：
   ```bash
   docker run hello-world
   ```

如果看到 Docker 的欢迎信息，说明配置成功。

### 总结

通过以上步骤，你可以在 Windows 下安装 Docker 并配置国内镜像，加速 Docker 镜像的下载速度。这样在日常开发中，你可以更高效地使用 Docker。