<?php

declare(strict_types=1);

namespace Aming\Utils;

// final 防止被子类覆盖，不能继承

final class Arr
{

    // remove duplicate item
    //还是不理解
    public static function unique(array $array, bool $keepKeys = false): array
    {
        if ($keepKeys) {
            //这个函数 key，和值 都会比较
            $array = array_unique($array);
        } else {
            //这个函数会忽略key，只比较值
            $arr = array_keys(array_flip($array));
        }
        return $array;
    }

    // Test:
    // $arr1= ['hello', 'world', 'this', 'is', 'a', 'test', 'hello', 'is', 'a', 'word'];
    // print_r(Arr::unique($arr1));
    // print_r(Arr::unique($arr1,true));


    //   $arr2= [
    //             'asd_1' => 'asd',
    //             'asd_2' => 'asd',
    //         ];

    // print_r(Arr::unique($arr2));
    // print_r(Arr::unique($arr2,true));


    // Check if key exists 检查是数组否存在某 key
    // 不赞成，反对使用 array_key_exists
    // @deprecated Use array_key_exists or ?: or ??
    // mixed 类型，是混合类型，要 php 8.00开始支持
    public static function key(mixed $key, array $array, bool $returnValue = false): mixed
    {
        $isExists = array_key_exists((string)$key, $array);

        if ($returnValue) {
            if ($isExists) {
                return $array[$key];
            }
        }
        return null;
    }
    // $arr=[];
    // $arr['name']='aming';
    // $arr['age']=36;
    // $key='name';
    // print_r(arr::key($key,$arr,true));


}
