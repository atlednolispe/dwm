修改键盘按键映射
=============

```bash
# 修改键盘配置文件
$ sudo vi /etc/default/keyboard
XKBOPTIONS="ctrl:swapcaps"

$ sudo dpkg-reconfigure keyboard-configuration
```