 
在 Ubuntu 中，要让某个软件在系统启动时自动启动，你可以使用以下几种方法：

### 1. **使用 "Startup Applications" 图形界面（适用于 GNOME 或 Ubuntu 默认桌面环境）**
   这是最简单的方法，适合大多数用户。

   - **步骤**：
     1. 打开 **"Startup Applications"**（启动应用程序）。你可以通过在应用菜单中搜索 "Startup Applications" 或通过按下 `Super` 键（通常是 Windows 键）并输入 "Startup" 来查找。
     2. 在打开的窗口中，点击 **"Add"**（添加）。
     3. 输入应用程序的名称、命令和可选的描述：
        - **名称**：可以是你想显示的名称。
        - **命令**：应用程序的启动命令，通常是程序的执行路径或命令。
        - **描述**：可以填写一些描述信息（可选）。
     4. 点击 **"Add"** 完成添加。
     5. 重新启动系统后，软件会自动启动。

   - **例如**：
     - 如果你想添加 Google Chrome 的启动项，命令可以是：`google-chrome-stable`
     - 如果是一个脚本，你可以使用脚本的完整路径（如：`/home/user/myscript.sh`）

### 2. **通过 `~/.config/autostart` 目录手动添加启动项**
   你也可以手动将启动项添加到 `~/.config/autostart/` 目录中。

   - **步骤**：
     1. 打开终端。
     2. 创建一个 `.desktop` 文件到 `~/.config/autostart` 目录。你可以使用文本编辑器（例如 `nano`）来创建此文件。例如，假设你要添加 Firefox 自动启动：
        
        ```bash
        nano ~/.config/autostart/firefox.desktop
        ```

     3. 在文件中添加以下内容（根据你要启动的程序修改）：
        
        ```bash
        [Desktop Entry]
        Type=Application
        Exec=firefox
        Name=Firefox
        Comment=Launch Firefox at startup
        X-GNOME-Autostart-enabled=true
        ```

     4. 保存并关闭文件（在 `nano` 中，按 `Ctrl+O` 保存，`Ctrl+X` 退出）。
     5. 现在，Firefox 会在每次启动时自动打开。

### 3. **通过 `crontab` 添加定时任务**
   如果你想让某个程序在每次启动时自动运行，可以使用 `cron` 定时任务来添加。

   - **步骤**：
     1. 打开终端，输入以下命令编辑当前用户的 `crontab`：
        
        ```bash
        crontab -e
        ```

     2. 在 `crontab` 文件中添加以下行（假设你想让 Firefox 启动）：
        
        ```bash
        @reboot firefox
        ```

     3. 保存并退出编辑器（在 `nano` 中，按 `Ctrl+O` 保存，`Ctrl+X` 退出）。
     4. 这样设置后，每次系统启动时，Firefox 都会自动运行。

### 4. **使用 `systemd` 创建一个服务**
   如果你希望更精细地控制程序的启动（例如，设置依赖关系、延迟启动等），你可以通过 `systemd` 创建一个启动服务。

   - **步骤**：
     1. 创建一个新的 `systemd` 服务单元文件：

        ```bash
        sudo nano /etc/systemd/system/myapp.service
        ```

     2. 在文件中添加以下内容（将 `ExecStart` 路径改为你想启动程序的路径）：

        ```ini
        [Unit]
        Description=My Application
        After=network.target

        [Service]
        ExecStart=/usr/bin/myapp
        Restart=always
        User=username

        [Install]
        WantedBy=default.target
        ```

     3. 保存并退出文件（`Ctrl+O` 保存，`Ctrl+X` 退出）。
     4. 启用并启动服务：

        ```bash
        sudo systemctl enable myapp.service
        sudo systemctl start myapp.service
        ```

     5. 这样，程序就会在每次启动时自动运行。

### 5. **通过 `~/.bashrc` 或 `~/.profile`**
   如果你希望在登录时运行某个程序（通常是命令行工具），可以将它添加到 `~/.bashrc` 或 `~/.profile` 文件中。

   - **步骤**：
     1. 打开终端，编辑 `~/.bashrc` 或 `~/.profile` 文件：

        ```bash
        nano ~/.bashrc
        ```

     2. 在文件的末尾添加启动命令。例如，如果你想让 `htop` 在每次打开终端时启动：

        ```bash
        htop &
        ```

     3. 保存并关闭文件（`Ctrl+O` 保存，`Ctrl+X` 退出）。
     4. 重新启动终端或系统，程序会自动启动。

### 总结
这些方法可以帮助你将应用程序或脚本添加到 Ubuntu 系统的开机启动项中。使用 **"Startup Applications"** 是最简单的方法，而使用 **`systemd`** 适合需要更复杂控制的高级用户。