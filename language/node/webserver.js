var http = require('http');

http.createServer(function (request, response) {
    response.writeHead(200, {
        'Content-Type': 'text/plain'
    });
    // 中文有异常
    response.end('Hello,World! 你好，世界！');
}
).listen(8124);

console.log('Server running at http://127.0.0.1:8124');