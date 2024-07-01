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
    
