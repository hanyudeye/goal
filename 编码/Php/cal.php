<?php

// 这种语法不容易看懂
$b=6+($a=5);

echo $a;
echo "\n";
echo $b;

echo "\n";
echo 9&7;
echo "\n";
echo 3|4;
echo "\n";
echo 3<<3;  // 3*2^3
echo "\n";


//类型判断函数
echo is_array(3); //返回null
echo "\n";
echo is_array([3,4,6]); //返回1