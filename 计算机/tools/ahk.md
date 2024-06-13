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
