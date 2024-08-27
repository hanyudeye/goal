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
