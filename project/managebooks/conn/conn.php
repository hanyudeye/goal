<?php

// $hostname = null,
// ?string $username = null,
// ?string $password = null,
// ?string $database = null,
// ?int $port = null,
// ?string $socket = null
$hostname="localhost";
$username="root";
$password="root";
$database="db_library";

$conn=mysqli_connect($hostname,$username,$password) or die("数据库服务器连接错误".mysqli_error());

mysqli_select_db($conn,$database) or die("数据库访问错误".mysqli_error());

// mysqli_query("set names gb2312");


