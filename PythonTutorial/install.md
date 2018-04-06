Installation
============

## repository install

```bash
$ sudo apt-get install software-properties-common

$ sudo add-apt-repository ppa:XXX/ppa

$ sudo apt-get update

$ sudo apt-get install python3.7
```

## official

## source

```bash
$ cd ~/Downloads

$ wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0b3.tar.xz

$ tar Jxvf Python-3.7.0b3.tar.xz

$ cd Python-3.7.0b3

# Python3可能都需要的依赖
$ sudo apt-get install zlib1g-dev build-essential checkinstall -y

# Python3可能都需要的依赖
$ sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev -y

# Python3.7需要libffi
# https://bugs.python.org/issue31652
$ sudo apt install libffi-dev

$ ./configure --prefix=/usr/python370b3 --enable-optimizations && make && sudo make install

$ sudo ln -s /usr/python370b3/bin/python3 /usr/bin/python3.7

$ sudo ln -s /usr/python370b3/bin/pip3 /usr/bin/pip3.7
```