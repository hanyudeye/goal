<?php

$root = $_SERVER['DOCUMENT_ROOT'];
echo $root;
$fd = fopen("$root/test.csv", "r");

if (!$fd) {
    echo "打不开文件";
    exit();
}

while (!feof($fd)) {
    //打开csv 数据文件
    print_r(fgetcsv($fd, 100,","));
}

fclose($fd);