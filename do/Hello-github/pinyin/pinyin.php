<?php

/**
 * 中文转拼音函数
 * 
 * @param string $chinese 输入的中文字符串
 * @param array $pinyin_dict 词库数组
 * @param bool $with_tone 是否保留声调（默认为false，不保留）
 * @return string 转换后的拼音
 */
function chinese_to_pinyin($chinese, $pinyin_dict, $with_tone = false) {
    $result = '';

    // 将字符串拆分为单个字符
    $chars = preg_split('//u', $chinese, -1, PREG_SPLIT_NO_EMPTY);

    // 逐个字符查找拼音
    foreach ($chars as $char) {
        if (isset($pinyin_dict[$char])) {
            $result .= $pinyin_dict[$char] . ' ';
        } else {
            // 如果找不到对应的拼音，保留原字符
            $result .= $char . ' ';
        }
    }

    // 去掉末尾多余的空格并返回结果
    return trim($result);
}

// 示例词库
$pinyin_dict = [
    '我' => 'wo',
    '是' => 'shi',
    '中' => 'zhong',
    '国' => 'guo',
    '人' => 'ren',
    '天' => 'tian',
    '气' => 'qi',
    '很' => 'hen',
    '好' => 'hao',
    // 这里可以添加更多汉字及其拼音
];

// 示例使用
$chinese_text = "我是中国人";
$pinyin = chinese_to_pinyin($chinese_text, $pinyin_dict);
echo $pinyin;  // 输出：wo shi zhong guo ren
