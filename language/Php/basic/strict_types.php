<?php

// 如果声明严格模式，那下面的返回类型会报错，要注释掉
declare(strict_types=1);

function foo():int{
    return 1.11;
}

echo foo();