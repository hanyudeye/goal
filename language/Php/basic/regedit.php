<?php

// 正则表达式排查

$source = "从前有座山，山上有座庙，庙里有个和尚";

if (mb_ereg("有座a|从前", $source)) {
    echo "匹配";
}else{
    echo "不匹配";
}
