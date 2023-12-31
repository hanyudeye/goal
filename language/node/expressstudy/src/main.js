// 用法 : 使用  node monitor  
//$ nodemon  main.js

var express = require("express");
// express 直接是一个服务器
const app = express();
const fs = require("fs");

const cors = require("cors");
app.use(cors()); //使用cors中间件
 

// 路由
app.get('/', function (req, res) {
    // res.send('Get request to message');
    // res.send(req.query);
    // res.send(req.url);
    res.send(req.baseUrl);
});

app.get('/user', function (req, res) {
    res.send('Get  user list request to message');
});



app.get('/user/:id', function (req, res) {
    res.send('Get  user:id request to message');
});

// 代办清单
app.get('/todos', function (req, res) {
    fs.readFile("./db.json", "utf-8", (err, data) => {
        if (err) {
            return res.status(500).json({
                error: err.message
            })
        }

        const db = JSON.parse(data);
        res.status(200).json(db.todos);
    })
});

app.get('/todos/:id', function (req, res) {
    fs.readFile("./db.json", "utf-8", (err, data) => {
        if (err) {
            return res.status(500).json({
                error: err.message
            })
        }

        const db = JSON.parse(data);
        // const todo = db.todos.find(todo => todo.id == req.params.id)
        // 请求的参数都是字符串，要进行转换
        const todo = db.todos.find(todo => todo.id === Number.parseInt(req.params.id))

        if (!todo) {
            return res.status(404).end()
        }
        res.status(200).json(todo)
    })
});

app.post('/', function (req, res) {
    res.send('Post request to message');
});




app.listen(3000, () => {
    console.log('Server running at http://localhost::3000/')
})