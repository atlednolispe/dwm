Git的基础配置
===========

## 生成ssh公钥
[github指南](https://help.github.com/articles/connecting-to-github-with-ssh/)

## git用户基础信息配置

```bash
$ vim ~/.gitconfig 

[user]
	email = atlednolispe@gmail.com
	name = atlednolispe
[core]
	editor = vim
[credential]
	helper = store
[alias]
	co = checkout
	br = branch
	ci = commit
	st = status

# 免密设置
$ git config --global credential.helper store
```

## 克隆repo

```bash
# 使用ssh协议克隆
$ git clone git@github.com:atlednolispe/dwm.git

# 若已经使用https协议克隆
# 更换克隆协议https为ssh
$ git remote set-url origin git@github.com:yourusername/yourrepositoryname.git
```