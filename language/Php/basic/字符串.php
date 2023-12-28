<?php

$url="aming.xyz";

echo "I'm learning PHP at $url \n";

$arr=[1,3,5,7];

echo "数组长度是 ".count($arr);

const PI=3.1415926;

$banjin=2;
$yuanzhou=2*PI*$banjin;
echo "\n 半径为 $banjin 的圆周是 $yuanzhou";

class Student{
    public function __construct($name){
        $this->name=$name;
    }

    public function getname(){
        return $this->name;
    }
}

$student=new Student("阿明");
echo "名字是 ". $student->getname();
