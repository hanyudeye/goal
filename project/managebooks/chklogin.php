<?php
session_start();
$name = $_POST['name'];
$pwd = $_POST['pwd'];            //接收表单提交的密码

class chkinput
{
    var $name;
    var $pwd;

    function chkinput($x, $y)
    {
        $this->name = $x;
        $this->pwd = $y;
    }

    function checkinput()
    {

        include("conn/conn.php");
        // $sql = mysqli_query("select * from tb_manager where name='" . $this->name . "' and pwd='" . $this->pwd . "'", $conn);
        $sql = mysqli_query($conn, "select * from tb_manager where name='" . $this->name . "' and pwd='" . $this->pwd . "'");
        $info = mysqli_fetch_array($sql);       //检索管理员名称和密码是否正确
        if ($info == false) {                    //如果管理员名称或密码不正确，则弹出相关提示信息
            echo "<script language='javascript'>alert('您输入的管理员名称错误，请重新输入！');history.back();</script>";
            exit;
        } else {                              //如果管理员名称或密码正确，则弹出相关提示信息
            echo "<script>alert('管理员登录成功!');window.location='index.php';</script>";
            $_SESSION['admin_name'] = $info['name'];
            $_SESSION['pwd'] = $info['pwd'];
        }
    }
}

$obj = new chkinput(trim($name), trim($pwd));
$obj->checkinput();
