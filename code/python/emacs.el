(unless (package-installed-p 'use-package)
  (package-refresh-contents)
  (package-install 'use-package))

(require 'use-package)
(setq use-package-always-ensure t)
(use-package better-defaults)

(message "hello")

(set-language-environment "UTF-8")
(prefer-coding-system 'utf-8)

