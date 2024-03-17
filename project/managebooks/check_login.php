<?php

session_start();

// 清除session
// session_destroy();
if(!$_SESSION['admin_name']){
    echo "<script>alert('对不起，请通过正确途径登录图书管理系统！');window.location.href='login.php';</script>";
}
