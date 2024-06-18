set -g prefix C-a
unbind C-b
bind C-a send-prefix

 # pane navigation
bind -r h select-pane -L  # move left
bind -r j select-pane -D  # move down
bind -r k select-pane -U  # move up
bind -r l select-pane -R  # move right
bind > swap-pane -D       # swap current pane with the next one
bind < swap-pane -U       # swap current pane with the previous one
 

## 分割窗口(窗格)

创建垂直窗格 Ctrl+b+ %
创建水平窗格 Ctrl+b+ "

## 会话 

创建新会话  tmux new -s session_name

## 保存会话

下载 tpm 插件

```bash
# 下载 tqm 到~/.tmux/plugins
# tqm是tmux插件管理工具
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm


# 进入相应位置
cd ~/.tmux/plugins 

# 下载插件
git clone https://github.com/tmux-plugins/tmux-resurrect.git # 保存tmux会话到disk
git clone https://github.com/tmux-plugins/tmux-continuum.git # 定时保存，自动加载
```

在 ~/.tmux.conf中配置

``` conf

set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-resurrect'
set -g @plugin 'tmux-plugins/tmux-continuum'

# 自动备份时间间隔60min, 默认15min
set -g @continuum-save-interval '60'
set -g @continuum-restore 'on'
set -g @resurrect-capture-pane-contents 'on'

# Other config ...

run -b '~/.tmux/plugins/tpm/tpm'
```

重载使文件生效
```bash
tmux source-file ~/.tmux.conf

```


## 手动保存及恢复

保存会话 Ctrl+b + Ctrl+s ，保存到 ~/.tmux/resurrenct 目录
加载会话 Ctrl+b + Ctrl+r 




