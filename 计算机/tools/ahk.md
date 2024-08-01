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
    WinGet, windowID, ID,  ahk_exe %windowT%
   ; 使用 ahk_class 也可以 

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
#s::ToggleQuakeWindowT("ahk_exe chrome.exe")
## script
    
``` ahk
CapsLock::Ctrl
!j:: Send {Down}
!k:: Send {Up}

;切换虚拟桌面
#^;::Send #^{Right}
#^h::Send #^{Left}

Active(t){
;     IfWinActive,%t%
;   {
;     WinMinimize
;     return
;   }

;    IfWinExist,%t%
;   {
;     WinShow
;     WinActivate           
;     return 1
;   }
 WinActivate,ahk_exe %t%
 return
}

Match(){
; 使用正则表达式匹配窗口标题并激活
RegexPattern := ".*Microsoft.*"
 
; 检查是否存在匹配窗口标题的窗口
if WinExist("ahk_class Chrome_WidgetWin_1 ahk_exe msedge.exe ahk_title " RegexPattern)
{
    ; 如果存在，则激活窗口
    WinActivate
}

return
 }



;激活资源管理器
#e::WinActivate,ahk_class CabinetWClass
#a::WinActivate, EasyChat
;#w::Active("msedge.exe")
#w::Match()
#m::Active("Code.exe")
#i::Active("WindowsTerminal.exe")
#o::Active("okular.exe")
#s::Active("chrome.exe")
#y::Active("copytranslator.exe")
#n::Active("emacs.exe")
#x::WinActivate,Telegram

;激活Code Shijian
#+s::
WinTitle=ahk_class Chrome_WidgetWin_1
main:
WinGet, winList,List,%WinTitle%
wins:=[]
Loop,%winList%
{
    this_id=% winList%A_Index%
    WinGetTitle,this_title,ahk_id %this_id%
    wins.Insert({index:A_Index,title:this_title,id:this_id})
    ;MsgBox  %this_id%
}

main_flag:=box_flag:=message_flag:=0
for each,win in wins
{

   if InStr(win.title,"Shijian")
		{
			main_id:=win.id
			WinActivate,ahk_id %main_id%
			
		}
}

return


;激活Code Lilun
#+l::
WinTitle=ahk_class Chrome_WidgetWin_1
WinGet, winList,List,%WinTitle%
wins:=[]
Loop,%winList%
{
    this_id=% winList%A_Index%
    WinGetTitle,this_title,ahk_id %this_id%
    wins.Insert({index:A_Index,title:this_title,id:this_id})
    ;MsgBox  %this_id%
}

main_flag:=box_flag:=message_flag:=0
for each,win in wins
{

   if InStr(win.title,"blog")
		{
			main_id:=win.id
			WinActivate,ahk_id %main_id%
			
		}
}

return
```

## 激活或隐藏某个窗口

; 设置快捷键 Ctrl+Alt+H

^!h::
{
    ; 窗口标题，可以修改为你想要控制的窗口标题
    WindowTitle := "Untitled - Notepad"

    ; 检查窗口是否存在
    IfWinExist, %WindowTitle%
    {
        ; 如果窗口存在，检查窗口是否可见
        IfWinActive, %WindowTitle%
        {
            ; 如果窗口是活动的，则隐藏窗口
            WinHide, %WindowTitle%
        }
        else
        {
            ; 如果窗口存在但未激活，则激活窗口
            WinActivate, %WindowTitle%
        }
    }
    else
    {
        ; 如果窗口不存在，显示提示信息
        MsgBox, 窗口 "%WindowTitle%" 未找到.
    }
}
return

如果目标窗口的标题不唯一，可以使用 ahk_class 或 ahk_exe 来更精确地指定窗口。例如：

; 使用窗口类名
WindowTitle := "ahk_class Notepad"

; 使用可执行文件名
WindowTitle := "ahk_exe notepad.exe"



; 定义一个全局变量来跟踪窗口的可见状态
WindowVisible := false

; 设置快捷键 Ctrl+Alt+H
^!h::
{
    WindowTitle := "Untitled - Notepad"

    IfWinExist, %WindowTitle%
    {
        ; 根据 WindowVisible 变量的状态来隐藏或显示窗口
        if (WindowVisible)
        {
            WinHide, %WindowTitle%
            WindowVisible := false
        }
        else
        {
            WinShow, %WindowTitle%
            WinActivate, %WindowTitle%
            WindowVisible := true
        }
    }
    else
    {
        MsgBox, 窗口 "%WindowTitle%" 未找到.
    }
}
return


;切换窗口
ToggleWindow(WindowTitle){

 IfWinExist, %WindowTitle%
    {
        ; 根据 WindowVisible 变量的状态来隐藏或显示窗口
        if (WindowVisible)
        {
            WinHide, %WindowTitle%
            WindowVisible := false
        }
        else
        {
            WinShow, %WindowTitle%
            WinActivate, %WindowTitle%
            WindowVisible := true
        }
    }
    else
    {
        MsgBox, 窗口 "%WindowTitle%" 未找到.
    }

return
}