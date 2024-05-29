(unless (package-installed-p 'use-package)
  (package-refresh-contents)
  (package-install 'use-package))

(require 'use-package)
(setq use-package-always-ensure t)
(use-package better-defaults)

(message "hello")

(set-language-environment "UTF-8")
(prefer-coding-system 'utf-8)

提高速度
dotspacemacs-scrath-mode 'text-mode

复制粘贴
  '(cua-mode t nil (cua-base))


中文卡顿
;; Setting English Font
(set-face-attribute
‘default nil :font “Courier New-14”)
;; Setting Chinese Font
(dolist (charset ‘(kana han symbol cjk-misc bopomofo))
(set-fontset-font (frame-parameter nil ‘font)
charset
(font-spec :family “Microsoft Yahei” :size 16)))