<?php

// 当前脚本所在目录
// 文件所在的目录 ，相当于 dirname(__FILE__)
echo __DIR__;

echo "\n";

echo dirname(__FILE__);
echo __FILE__;
echo "\n";
require "lib/import_lib.php";

echo "\n";

// 合并数组
print_r(array_merge(['苍天','大地'],['青山','绿水'],['fruits'=>['苹果'],'animals'=>['牛']]));
