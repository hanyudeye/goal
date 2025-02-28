 
创建一个网页版游戏，主角在一个森林迷宫中走动，并通过发射子弹消灭野兽，需要结合 HTML、CSS 和 JavaScript 来实现。下面是一个简化版的游戏设计，包含了使用方向键控制移动、空格键发射子弹、以及在迷宫中与野兽互动的基本功能。你可以根据这个基础代码进行扩展和完善。

### 1. 基础 HTML 结构
首先，创建一个基础的 HTML 页面来容纳游戏画布和控制元素。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>森林冒险游戏</title>
    <style>
        body {
            margin: 0;
            overflow: hidden;
        }
        canvas {
            display: block;
            background-color: #2e8b57; /* 背景色为森林绿 */
        }
    </style>
</head>
<body>
    <canvas id="gameCanvas"></canvas>
    <script src="game.js"></script>
</body>
</html>
```

### 2. JavaScript 代码

在 `game.js` 文件中，你需要做以下几件事：
- 绘制迷宫（森林）和游戏元素（主角、野兽、子弹）。
- 监听键盘事件，控制主角的移动和子弹发射。
- 使用简单的碰撞检测来确定是否击中野兽。

```javascript
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

// 设置画布大小
canvas.width = 800;
canvas.height = 600;

// 游戏元素的参数
const player = {
    x: 50,
    y: 50,
    width: 40,
    height: 40,
    speed: 5,
    dx: 0,
    dy: 0,
    color: 'green',
};

const bullet = {
    width: 5,
    height: 10,
    color: 'red',
    speed: 7,
    active: false,
    x: 0,
    y: 0,
    dx: 0,
    dy: -1
};

const animals = [
    { x: 400, y: 300, width: 40, height: 40, color: 'brown' },
    { x: 600, y: 150, width: 40, height: 40, color: 'orange' }
];

// 控制主角的键盘输入
let keys = {};
document.addEventListener('keydown', (e) => {
    keys[e.key] = true;
});
document.addEventListener('keyup', (e) => {
    keys[e.key] = false;
});

// 游戏更新
function update() {
    // 移动主角
    if (keys['ArrowUp']) player.dy = -player.speed;
    else if (keys['ArrowDown']) player.dy = player.speed;
    else player.dy = 0;
    if (keys['ArrowLeft']) player.dx = -player.speed;
    else if (keys['ArrowRight']) player.dx = player.speed;
    else player.dx = 0;

    player.x += player.dx;
    player.y += player.dy;

    // 发射子弹
    if (keys[' '] && !bullet.active) {
        bullet.active = true;
        bullet.x = player.x + player.width / 2 - bullet.width / 2;
        bullet.y = player.y;
    }

    // 更新子弹位置
    if (bullet.active) {
        bullet.y += bullet.dy * bullet.speed;

        // 检测子弹是否击中动物
        animals.forEach(animal => {
            if (bullet.active &&
                bullet.x < animal.x + animal.width &&
                bullet.x + bullet.width > animal.x &&
                bullet.y < animal.y + animal.height &&
                bullet.y + bullet.height > animal.y) {
                bullet.active = false;  // 子弹消失
                animal.x = Math.random() * canvas.width; // 随机位置重新出现
                animal.y = Math.random() * canvas.height;
            }
        });
    }

    // 绘制游戏画面
    draw();
    requestAnimationFrame(update); // 下一帧继续调用
}

// 绘制画面
function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // 绘制主角
    ctx.fillStyle = player.color;
    ctx.fillRect(player.x, player.y, player.width, player.height);

    // 绘制子弹
    if (bullet.active) {
        ctx.fillStyle = bullet.color;
        ctx.fillRect(bullet.x, bullet.y, bullet.width, bullet.height);
    }

    // 绘制动物
    animals.forEach(animal => {
        ctx.fillStyle = animal.color;
        ctx.fillRect(animal.x, animal.y, animal.width, animal.height);
    });
}

// 开始游戏
update();
```

### 3. 游戏说明
1. **主角**：绿色方块，使用方向键（上、下、左、右）控制移动。
2. **野兽**：两只野兽（可以扩展），随机出现在画布上的位置。使用碰撞检测，当子弹击中野兽时，野兽会重新随机出现在其他地方。
3. **子弹**：按下空格键发射，子弹从主角的当前位置发射，向上飞行。如果击中野兽，野兽会“消失”并重新出现在屏幕上的随机位置。

### 4. 游戏功能说明
- **主角控制**：使用箭头键（方向键）控制主角在迷宫中的移动。
- **子弹发射**：按下空格键发射子弹，子弹向上飞行，击中野兽时会重新生成。
- **迷宫与环境**：迷宫布局可以通过增加障碍物来进一步扩展，当前的基础示例没有设置障碍。
- **游戏扩展**：你可以添加更复杂的敌人行为、生命值、分数和更多关卡。

### 5. 改进建议
- 增加迷宫或障碍物的布局，限制主角和子弹的移动。
- 增加敌人的运动行为，让它们自动向主角靠近或四处移动。
- 添加游戏计时器和得分系统，记录击败的野兽数量。
- 引入更丰富的图形和音效，提升游戏体验。

这个简单的游戏结构可以根据你的需求进一步扩展和定制。