const http = require("http");
const server = http.createServer();

// const server = http.createServer(
//     (req, res) => {
//         res.setHeader('Content-Type', 'text/plain;charset=utf-8');
//         res.end("hello,你好");
//     }
// );

// 这里没执行
server.on('request', (req, res) => {


        res.setHeader('Content-Type', 'text/plain;charset=utf-8');
    // 路由判断
    if (req.url == "/index.html" || req.url=="/") {
        //响应的内容
        res.end('欢迎来到我的网站');
    }else if(req.url=="/news.html"){
        res.end('这里时新闻news 页面');
    }
    else{
        res.end('此页面不允许访问');
 
    }

})


//服务器监听端口
server.listen(4000, () => {
    console.log("nodejs 服务器启动");
})