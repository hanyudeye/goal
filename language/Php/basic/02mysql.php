<?php

$link = mysqli_connect("localhost", "wuming", "wuming", "test");
if ($link) {
    echo "连接成功";
    mysqli_close($link);
} else {

    echo "连接失败";
}
