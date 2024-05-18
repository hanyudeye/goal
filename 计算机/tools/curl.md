`curl` 是一个在命令行下使用的工具，用于传输数据，支持多种协议，包括 HTTP、HTTPS、FTP 等。以下是一些常用的 `curl` 命令用法示例：

1. 发送 GET 请求并输出响应到标准输出：
```bash
curl http://www.example.com
```

2. 发送 POST 请求并传递数据：
```bash
curl -X POST http://www.example.com/api -d "param1=value1&param2=value2"
```

3. 下载文件到本地：
```bash
curl -O http://www.example.com/file.zip
```

4. 显示响应头信息：
```bash
curl -I http://www.example.com
```

5. 下载文件并重命名：
```bash
curl -o newfilename.jpg http://www.example.com/filename.jpg
```

6. 限制下载速度：
```bash
curl --limit-rate 100k -O http://www.example.com/largefile.zip
```

7. 忽略 SSL 证书检查：
```bash
curl -k https://www.example.com
```

8. 显示详细的传输信息：
```bash
curl -v http://www.example.com
```

这些是 `curl` 命令的一些基本用法示例。你可以根据具体需求，结合不同的选项来使用 `curl` 完成各种网络数据传输任务。