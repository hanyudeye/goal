<?php

//创建数字数组
$arr = [1, 3, 5];
print_r($arr);
//插入单个数据
array_push($arr, 7);
print_r($arr);

// 数组覆盖
$arr[0] = 'a';
print_r($arr);

//遍历数组
foreach ($arr as $k => $val) {
    echo "key is ".$k;
    echo "\tvalue is ".$val;
    echo "\n";
}

//对象索引
//鼠标对象
$mouse=[
"sturct"=>['左键',"中键","右键"],
"brand"=>"罗技",
"weight"=>"400g"
];

foreach ($mouse as $k => $val) {
    echo "key is ".$k;
    echo "\tvalue is ".$val;
    echo "\n";
}

//each 和 list 的用法，好象废弃了
while(list($key,$value)=each($mouse)){
    echo "key is $key  value is $value ";
}

// array_count_values() 统计数组中 键(东西) 出现的次数
$arr=[1,1,2,5,5,7];
print_r(array_count_values($arr));
