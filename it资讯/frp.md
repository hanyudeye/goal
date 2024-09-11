使用 **FRP（Fast Reverse Proxy）** 进行内网穿透是一个不错的选择，尤其适合你这种低流量、个人使用的小博客场景。FRP 是一款高效的反向代理应用程序，能够让你将内网服务（如Web服务器、博客等）暴露给外网用户访问。

### 如何使用 FRP 进行内网穿透

1. **准备服务器**：你需要在公网上拥有一台可以访问的服务器（比如云服务器），用于运行 FRP 服务端。该服务器可以是租用的云服务器，也可以是一个有公网 IP 的主机。

2. **下载 FRP**：从 [FRP的GitHub仓库](https://github.com/fatedier/frp/releases) 下载适合你服务器和本地计算机的 FRP 可执行文件。

3. **配置 FRP 服务端（frps）**：
   - 在你的云服务器上，解压下载的 FRP 文件，找到 `frps.ini` 文件或自己创建一个配置文件。
   - 添加或修改如下内容（具体端口可根据你的需要调整）：
     ```ini
     [common]
     bind_port = 7000  # FRP 服务端的监听端口
     dashboard_port = 7500  #（可选）FRP 仪表盘的访问端口
     dashboard_user = your_username  #（可选）FRP 仪表盘用户名
     dashboard_pwd = your_password  #（可选）FRP 仪表盘密码
     ```

4. **启动 FRP 服务端**：
   - 在服务器上运行以下命令启动服务端：
     ```bash
     ./frps -c frps.ini
     ```
   
5. **配置 FRP 客户端（frpc）**：
   - 在你的本地机器（例如你要将其暴露给外网访问的博客服务器上），同样解压下载的 FRP 文件，找到 `frpc.ini` 文件或创建一个新的配置文件。
   - 添加或修改如下内容：
     ```ini
     [common]
     server_addr = your_server_ip  # 服务器的公网IP或域名
     server_port = 7000  # 与服务端配置中绑定的端口一致

     [web]
     type = http
     local_port = 80  # 本地博客服务的端口（如80、8080）
     custom_domains = your_domain.com  # 自定义的域名或IP
     ```

6. **启动 FRP 客户端**：
   - 在本地运行以下命令启动客户端：
     ```bash
     ./frpc -c frpc.ini
     ```

7. **域名解析**（可选）：如果你使用的是域名访问博客，记得将域名的 DNS 解析指向你的云服务器的公网 IP 地址。

### 使用 FRP 方案的成本分析

- **FRP 方案**的成本主要来自你需要的公网服务器。如果你选择租用一个最低配置的云服务器，比如阿里云、腾讯云或其他提供商，一般可以找到每月几美元或几十元人民币的轻量应用服务器。
- **自购服务器方案**的成本通常会更高，特别是对于小流量博客来说。你不仅需要支付一次性的硬件成本，还需负担较高的带宽费用、电力消耗和维护成本。

### 结论

使用 FRP 是一个**比自购服务器更实惠的选择**，特别是对于小博客或低流量的服务。在有公网 IP 的服务器上运行 FRP 服务端，可以通过低成本的云服务器实现内网穿透，而无需投入大量资金购买和维护物理服务器。

如果你需要通过 FRP 配置多个不同域名的博客，可以在 FRP 客户端的配置文件中添加多个服务条目，每个条目对应一个不同的域名和本地服务。以下是如何设置的详细步骤：

### 1. FRP 服务端配置（`frps.ini`）

首先，在你的云服务器上确保 `frps.ini` 文件已正确配置，可以使用以下内容：

```ini
[common]
bind_port = 7000  # FRP 服务端监听的端口
vhost_http_port = 80  # 用于 HTTP 服务的端口
vhost_https_port = 443  # 用于 HTTPS 服务的端口（可选）
dashboard_port = 7500  # 仪表盘端口（可选）
dashboard_user = your_username  # 仪表盘用户名（可选）
dashboard_pwd = your_password  # 仪表盘密码（可选）
```

启动 FRP 服务端：

```bash
./frps -c frps.ini
```

### 2. FRP 客户端配置（`frpc.ini`）

在本地服务器（运行博客的服务器）上，创建或修改 `frpc.ini` 文件，配置多个域名的博客：

```ini
[common]
server_addr = your_server_ip  # FRP 服务端的公网 IP 地址
server_port = 7000  # FRP 服务端的监听端口

# 第一个博客服务
[blog1]
type = http
local_port = 8080  # 本地第一个博客服务的端口
custom_domains = blog1.example.com  # 第一个博客的域名

# 第二个博客服务
[blog2]
type = http
local_port = 8081  # 本地第二个博客服务的端口
custom_domains = blog2.example.com  # 第二个博客的域名

# 第三个博客服务
[blog3]
type = http
local_port = 8082  # 本地第三个博客服务的端口
custom_domains = blog3.example.com  # 第三个博客的域名
```

- 每个 `[blogX]` 段定义了一个服务。
- `type = http` 表示这是一个 HTTP 服务。
- `local_port` 指定本地博客服务的端口（如 8080、8081 等）。
- `custom_domains` 是你要通过公网访问的域名。

### 3. 启动 FRP 客户端

在本地服务器上启动 FRP 客户端：

```bash
./frpc -c frpc.ini
```

### 4. 域名解析

确保你拥有的每个域名（如 `blog1.example.com`，`blog2.example.com`）都指向 FRP 服务端的公网 IP 地址。你需要在域名提供商的管理面板中配置 DNS 记录：

- 添加 A 记录，指向你的 FRP 服务端的公网 IP 地址。

### 5. 使用 HTTPS（可选）

如果你希望你的博客使用 HTTPS 访问，可以在每个 `[blogX]` 配置段中添加以下内容：

```ini
type = https
local_port = 443  # 本地服务的 HTTPS 端口
custom_domains = blog1.example.com  # 使用 HTTPS 的域名
```

同时，你需要在 FRP 服务端（`frps.ini`）中开启 HTTPS 支持，并配置 SSL 证书：

```ini
vhost_https_port = 443  # 启用 HTTPS 支持
```

确保你的云服务器上有有效的 SSL 证书（如 Let's Encrypt）配置。

### 结论

通过这种配置方法，你可以轻松将多个不同域名的博客暴露给外网访问。每个域名对应一个本地服务，FRP 客户端将请求转发到相应的博客服务。这样设置既灵活又易于管理，非常适合多域名、小流量的个人博客或项目。
