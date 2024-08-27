如果不使用框架来创建 Node.js 服务器，可以直接使用原生的 http 模块。下面是一个简单的例子，用原生 Node.js 创建一个服务器并处理 5 个 API 请求。

1. 创建 server.js
const http = require('http');

// 解析请求体的辅助函数
function parseBody(req, callback) {
    let body = '';
    req.on('data', chunk => {
        body += chunk.toString();
    });
    req.on('end', () => {
        callback(body ? JSON.parse(body) : {});
    });
}

// 创建服务器
const server = http.createServer((req, res) => {
    // 设置返回的响应头，允许发送 JSON 格式的数据
    res.setHeader('Content-Type', 'application/json');

    // 1. GET /api/welcome
    if (req.method === 'GET' && req.url === '/api/welcome') {
        res.writeHead(200);
        res.end(JSON.stringify({ message: 'Welcome to the Node.js server!' }));
    }
    
    // 2. POST /api/user
    else if (req.method === 'POST' && req.url === '/api/user') {
        parseBody(req, (user) => {
            res.writeHead(200);
            res.end(JSON.stringify({
                message: 'User data received',
                user: user
            }));
        });
    }

    // 3. PUT /api/user/:id
    else if (req.method === 'PUT' && req.url.startsWith('/api/user/')) {
        const userId = req.url.split('/')[3];
        parseBody(req, (updatedUser) => {
            res.writeHead(200);
            res.end(JSON.stringify({
                message: `User with ID ${userId} updated`,
                updatedUser: updatedUser
            }));
        });
    }

    // 4. DELETE /api/user/:id
    else if (req.method === 'DELETE' && req.url.startsWith('/api/user/')) {
        const userId = req.url.split('/')[3];
        res.writeHead(200);
        res.end(JSON.stringify({
            message: `User with ID ${userId} deleted`
        }));
    }

    // 5. GET /api/users
    else if (req.method === 'GET' && req.url === '/api/users') {
        const users = [
            { id: 1, name: 'Alice' },
            { id: 2, name: 'Bob' },
            { id: 3, name: 'Charlie' }
        ];
        res.writeHead(200);
        res.end(JSON.stringify(users));
    }

    // 404 处理
    else {
        res.writeHead(404);
        res.end(JSON.stringify({ message: 'Route not found' }));
    }
});

// 服务器监听端口 3000
server.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});
2. 运行服务器
在终端中运行以下命令来启动服务器：

node server.js
3. 发送API请求
服务器启动后，你可以使用工具（如 Postman 或 curl）向以下 API 发送请求：

GET /api/welcome

描述: 返回欢迎信息。
示例: http://localhost:3000/api/welcome
POST /api/user

描述: 接收并返回用户数据。
示例: http://localhost:3000/api/user
请求体:
{
    "name": "John Doe",
    "email": "john@example.com"
}
PUT /api/user/:id

描述: 更新用户数据，基于ID。
示例: http://localhost:3000/api/user/1
请求体:
{
    "name": "Jane Doe",
    "email": "jane@example.com"
}
DELETE /api/user/:id

描述: 删除用户，基于ID。
示例: http://localhost:3000/api/user/1
GET /api/users

描述: 获取所有用户的模拟数据。
示例: http://localhost:3000/api/users
这个示例完全不依赖任何框架，使用 Node.js 的原生 http 模块构建简单的 API 服务器。你可以根据需求进一步扩展和修改。