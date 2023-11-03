## speak-ng

多语言语音合成器 multi-lingual speech synthesizer

选项

 -a  振幅，0 到 200，默认值为 100。

-g  字间隙。在单词之间暂停，以默认速度为 10 毫秒为单位。

-s  速度（以每分钟字数为单位），默认值为 175。

-p  音高调整，0 到 99，默认值为 50。

speak-ng --voices : List all voices supported by eSpeak.

5  cmn             --/M      Chinese_(Mandarin) sit/cmn

朗读中文

speak-ng -v cmn "你好，朋友" -s 300


Read bash -c "espeak-ng -s260 -g0 -p40 -v en-us \"$(xsel | sed -e :a -e 'N;s/\n/ /;ta')\""

Stop Reading bash -c "killall espeak-ng"

bash -c "espeak -s260 -g0 -p40 -v english-us \"$(xsel | sed -e :a -e 'N;s/\n/ /;ta')\""

在 i3wm 中进行配置 
bindsym $mod+x exec "espeak-ng -s260  -v cmn \\"$(xsel)\\""

或者使用
ekho 
