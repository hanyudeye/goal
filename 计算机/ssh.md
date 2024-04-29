要用 ssh 无密码登录，要把本地公钥 ~/.ssh/id_rsa.pub 配置到服务器 的 ~/.ssh/authorized_keys 认证文件中，服务器才能接受您的认证。

防火墙设置
1. 启动防火墙 sudo ufw enable
2. 屏蔽端口  sudo ufw deny 22
3. 删除屏蔽端口  sudo ufw delete deny 22
3. 允许端口访问 sudo ufw allow 22
4.  


netstat 相似的命令是 ss (Socket Statistics)

1. 查看TCP连接状态 ss -t   
2. 查看UDP 连接状态  ss -u

