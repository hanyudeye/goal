
> 思考人性，从自己的需求考虑问题

# blog
## 2024
### 08.02

大胆尝试新媒体，找合适的资讯，进行二次开发，发布。使用 gpt 工具二次创作。

使用数字媒体，可以把信息数字化，就不用纸了，方便传输和保存。
比如音频，视频，把信息转化成数字格式后可以交易


[Rebase](https://rebase.co),移民即服务，让您在想要吸引高科技远程工作者的国家/地区获得合法和税务居留权以及工作许可。它推出的第一个国家是葡萄牙。

制作伪装成 vscode 编辑器外观的网页资讯站，可以方便程序员摸鱼。


写博客的时候，可以使用一些 属性来增强博客的可读性
1. 旁注: 给特定内容添加补充
2. 目录: 方便浏览博客内容
3. 进度条： 顶部进度条可以方便知道博客长度
4. 

在行业技术论坛可以吐槽，也可以学点知识

当前银行利率很低了，进入了低利率时代。回报变少了，使人们重视长期效益，细水长流。
长期投入研究以后得趋势，在以后就能先产出。

### 08.03

找一个 canvas 一样的免费的插画网站

### 08.04

阅读一本书 就像 阅读一个人的思想。


on run {input, parameters}
-- 声明一个变量来存储先前的剪贴板内容
set previousClipboard to ""

-- 无限循环来持续监视剪贴板
repeat
    -- 获取当前剪贴板内容
    set currentClipboard to (the clipboard as text)
   -- 
    -- 如果剪贴板内容发生变化且非空
    if currentClipboard is not equal to previousClipboard and currentClipboard is not "" then
        -- 使用 say 命令朗读剪贴板内容
        do shell script "say " & quoted form of currentClipboard
        -- 更新先前的剪贴板内容
        set previousClipboard to currentClipboard
    end if
    
    -- 每0.5秒检查一次
    delay 0.5
end repeat
end run