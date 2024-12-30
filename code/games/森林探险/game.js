const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext('2d');

//设置画布大小
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
    height:10,
    color: 'red',
    speed: 7,
    active: false,
    x: 0,
    y: 0,
    dx: 0,
    dy: -1
}

const animals = [
    { x: 400, y: 300, width: 40, height: 40, color: 'brown' },
    { x: 600, y: 150, width: 40, height: 40, color: 'orange' },
];

//控制主角的键盘输入
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