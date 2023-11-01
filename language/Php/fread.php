<?php

// 读取任意长度的文件

// echo get_current_user();
//在命令行可能执行不成功，是因为当前目录 可能在上级，不一定
// file_exists() 可以提前判断
//unlink 删除文件
echo getcwd();

$path = getcwd() . "\\test.txt";

if (file_exists($path)) {

    $fd = fopen($path, "r");

    // 这些可以省略
    // if (!$fd) {
    //     echo "文件不存在";
    //     exit();
    // }

    //读任意字符
    echo fread($fd, 99);
}
