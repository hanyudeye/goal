要用 ssh 无密码登录，要把本地公钥 ~/.ssh/id_rsa.pub 配置到服务器 的 ~/.ssh/authorized_keys 认证文件中，服务器才能接受您的认证。

防火墙设置
1. 启动防火墙 sudo ufw enable
2. 屏蔽端口  sudo ufw deny 22
3. 删除屏蔽端口  sudo ufw delete deny 22
3. 允许端口访问 sudo ufw allow 22

netstat 相似的命令是 ss (Socket Statistics)

1. 查看TCP连接状态 ss -t
2. 查看UDP 连接状态  ss -u

SSH（Secure Shell）的故事要追溯到 1995 年。当时，网络安全成为一个日益严重的问题，尤其是在远程登录和文件传输方面。传统的 Telnet 和 rlogin 等协议虽然可以进行远程通信，但它们的数据传输是明文的，容易被黑客窃取。

于是，Tatu Ylönen，一位芬兰的研究人员，开发了 SSH 来解决这个问题。SSH 提供了一种加密的通信方式，确保数据在传输过程中是安全的，不会被中间人监听或篡改。它不仅支持远程登录，还支持文件传输，成为了网络安全领域的一个重要里程碑。

SSH 很快被广泛应用，尤其在 Linux 和 Unix 系统中，逐渐取代了不安全的传统协议。今天，SSH 成为全球范围内，尤其是在开发、系统管理和云计算领域中最常用的远程连接工具之一。