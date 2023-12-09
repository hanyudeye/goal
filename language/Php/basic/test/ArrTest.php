<?php

namespace Aming\PHPUnit;
// 载入 composer库
require_once __DIR__.'/../vendor/autoload.php';
//载入自定义库
require_once __DIR__.'/../utils/Arr.php';
//使用自定义命名空间

use Aming\Utils\Arr;

class ArrTest extends \PHPUnit\Framework\TestCase
{
    public function testUnique()
    {

        $array = ['1', '1', 'a', 'a'];
        $arr =  Arr::unique($array);
        print_r($arr);
    }
}

$t=new ArrTest();
$t->testUnique();
