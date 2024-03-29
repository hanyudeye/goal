<?php
ini_set('display_errors',1);
error_reporting(E_ALL);


//获取网站根目录
echo $_SERVER['DOCUMENT_ROOT'];

$ROOT = $_SERVER['DOCUMENT_ROOT'];

$fp = fopen("$ROOT/test.txt", 'a+');

//给文件上执行锁，防止在修改文件时出错
flock($fp, LOCK_EX);

if (!$fp) {
    echo "<p><strong>无法打开文件</strong></p>";
    exit;
}

// fwrite($fp,"hello\n");
// file_put_contents("$ROOT/test.txt","world\n","a+");

//这个读不出来
// echo  fread($fp,100);
$count=1;
while (!feof($fp)) {
    //fgets 是一行一行读的
    // echo fgets($fp, 999);

    //fgetss 函数可以过滤 allowable_tags，如 html ，php  标签，已废弃
    // echo fgetss($fp,999);
    echo "<br/>";
    // echo "num is ".$count;
    // echo "<br/>";
    $count++;
}

//关闭文件
fclose($fp);
