## 切换
```ahk
;切换窗口
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
#a::ToggleQuakeWindowT("ahk_exe Code.exe")

## 向右切换虚拟桌面
``` ahk 
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

