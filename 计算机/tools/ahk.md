## 向右切换虚拟桌面
代码还是有 bug
``` ahk 
; AutoHotkey 1.x script to switch virtual desktops
#Persistent

; Switch to next virtual desktop with Win + Ctrl + ;
#^;::
{
    Send, ^#{Right}
    return
}

; Switch to previous virtual desktop with Win + Ctrl + '
#^'::
{
    Send, ^#{Left}
    return
}

```


## 跳转窗口

```ahk
; 定义函数
ToggleQuakeWindowT(windowT)
{
    ; 查找窗口
    WinGet, windowID, ID,  %windowT%
    
    ; 如果窗口存在，则隐藏/显示
    if (windowID)
    {
        WinGet, windowState, MinMax, ahk_id %windowID%
        if (windowState)
	{
            WinRestore ahk_id %windowID%
            WinWait,%windowT%
            WinActivate
	}
        else
            WinMinimize ahk_id %windowID%
    }
}


```

#z::ToggleQuakeWindowT("Telegram ")
