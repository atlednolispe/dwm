安装Ubuntu后的一些初始化设置
========================

## 修改软件源

Software & Updates > Download From > Other > Select Best Server

## 修改Launcher菜单和已安装的软件

## 安装shadowsocks

[shadowsocks](https://www.mystery0.vip/2017/01/12/Ubuntu%E4%BD%BF%E7%94%A8Shadowsocks-qt5%E7%A7%91%E5%AD%A6%E4%B8%8A%E7%BD%91/)

[ss-ppa](https://launchpad.net/~hzwhuang/+archive/ubuntu/ss-qt5)

[does not have a Release file](https://www.qetee.com/linux/deepin-shadowsocks.html)

```
$ sudo add-apt-repository ppa:hzwhuang/ss-qt5
# 改里面的bionic为artful,bionic的版本还没更新
$ sudo vim /etc/apt/sources.list.d/hzwhuang-ubuntu-ss-qt5-bionic.list
$ sudo apt-get update
$ sudo apt-get install shadowsocks-qt5

# Local Server Type选择HTTP(S)
# 否则pip报错Missing dependencies for SOCKS support
```

## 安装Chrome和搜狗

下载deb包双击安装

sogou: 配置语言fcitx,注销后再fcitx configuration里增加搜狗

## 升级Python

不要动发行版自带依赖的python3(python3.5),也不要去mv默认的python,新创建一个python3.6

```bash
# atlednolispe @ atlednolispe-Ubuntu in ~/Downloads [23:25:46]
$ wget https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tgz

# atlednolispe @ atlednolispe-Ubuntu in ~/Downloads [0:02:28]
$ tar -zxvf Python-3.6.4.tgz

# atlednolispe @ atlednolispe-Ubuntu in ~/Downloads [0:02:28]
$ cd Python-3.6.4

# atlednolispe @ atlednolispe-Ubuntu in ~/Downloads/Python-3.6.4 [0:03:31]
$ sudo apt-get install zlib1g-dev

# atlednolispe @ atlednolispe-Ubuntu in ~ [19:59:13] C:1
$ sudo apt-get install build-essential checkinstall -y

# atlednolispe @ atlednolispe-Ubuntu in ~ [20:06:39]
$ sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev -y

# atlednolispe @ atlednolispe-Ubuntu in ~/Downloads/Python-3.6.4 [0:03:31]
$ ./configure --prefix=/usr/python36 --enable-optimizations

# atlednolispe @ atlednolispe-Ubuntu in ~/Downloads/Python-3.6.4 [0:03:31]
$ make && sudo make install

# atlednolispe @ atlednolispe-Ubuntu in ~/Downloads/Python-3.6.4 [0:11:02] C:127
$ sudo ln -s /usr/python36/bin/python3 /usr/bin/python3.6

# atlednolispe @ atlednolispe-Ubuntu in /usr/local/bin [0:16:18] C:1
$ sudo ln -s /usr/python36/bin/pip3 /usr/bin/pip3.6

# atlednolispe @ atlednolispe-Ubuntu in ~/Downloads/Python-3.6.4 [20:52:12]
$ pip3.6 install ipython
```

## Ubuntu18.04自带Python3

安装pip3
```
# 不要手贱更新倒pip10.0.1,会出现ImportError: cannot import name 'main'
# 9.0.1用一下就好了
$ sudo apt install python3-venv python3-pip

# 修复ImportError: cannot import name 'main'
$ sudo vim /usr/bin/pip3
from pip._internal import main

$ pip3 install ipython

# launchpadlib 1.10.6 requires testresources, which is not installed
$ pip3 install testresources --user

$ pip3 install pipenv

[pipenv: command not found](https://stackoverflow.com/questions/46391721/pipenv-command-not-found)
# 增加pipenv到PATH
$ vim .zshrc
PYTHON_BIN_PATH="$(python3 -m site --user-base)/bin"
PATH="$PATH:$PYTHON_BIN_PATH"

export PATH

```

## 安装ipython和pipenv

```bash
# atlednolispe @ atlednolispe-Ubuntu in ~ [22:16:27]
$ sudo pip3.6 install ipython

# atlednolispe @ atlednolispe-Ubuntu in ~ [21:09:48] C:127
$ python3.6 -m IPython

# atlednolispe @ atlednolispe-Ubuntu in ~ [22:16:27]
$ sudo pip3.6 install pipenv
```

## 安装oh-my-zsh和tmux

```bash
# atlednolispe @ atlednolispe-Ubuntu in ~ [22:16:27]
$ sudo apt install zsh git -y

# atlednolispe @ atlednolispe-Ubuntu in ~ [22:16:27]
$ sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"

# atlednolispe @ atlednolispe-Ubuntu in ~ [22:16:27]
$ sudo apt install tmux -y
```

## 开启ssh服务

```bash
# atlednolispe @ atlednolispe-Ubuntu in ~ [22:16:27]
$ sudo apt install openssh-server -y

# 更新ssh认证信息
$ ssh-keygen -R ip_address

$ ssh ...
```