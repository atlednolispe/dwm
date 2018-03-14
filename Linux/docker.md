Docker
======

## 安装Docker

## 使用docker id不是email登陆docker

```bash
$ docker login

$ docker login registry.cn-hangzhou.aliyuncs.com
```

## 检查是否正确安装

```bash
$ docker --version
Docker version 17.12.0-ce, build c97c6d6

$ docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
ca4f61b1923c: Pull complete
Digest: sha256:083de497cff944f969d8499ab94f07134c50bcf5e6b9559b27182d3fa80ce3f7
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://cloud.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/engine/userguide/
```

## 查看当前存在的镜像

```bash
$ docker image ls
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
hello-world         latest              f2a91732366c        3 months ago        1.85kB
```

## 查看当前存在的容器

```bash
$ docker container ls
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES

$ docker container ls --all
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                      PORTS               NAMES
ac34a08f8b4f        hello-world         "/hello"            22 minutes ago      Exited (0) 22 minutes ago                       compassionate_swanson
```

## 配置阿里云加速

[阿里云配置镜像加速器](https://cr.console.aliyun.com/#/accelerator)

## 从docker hub拉取镜像

```bash
$ docker pull ubuntu:16.04
16.04: Pulling from library/ubuntu
22dc81ace0ea: Pull complete
1a8b3c87dba3: Pull complete
91390a1c435a: Pull complete
07844b14977e: Pull complete
b78396653dae: Pull complete
Digest: sha256:e348fbbea0e0a0e73ab0370de151e7800684445c509d46195aef73e090a49bd6
Status: Downloaded newer image for ubuntu:16.04
```

## 测试ubuntu镜像

```bash
$ docker run ubuntu:16.04 /bin/echo "hello ubuntu"
hello ubuntu

$ docker run -it ubuntu:16.04 /bin/bash
root@1ddcaa3fa90f:/# cat /etc/issue
Ubuntu 16.04.4 LTS \n \l

root@1ddcaa3fa90f:/# uname
Linux
root@1ddcaa3fa90f:/# uname -a
Linux 1ddcaa3fa90f 4.9.60-linuxkit-aufs #1 SMP Mon Nov 6 16:00:12 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
root@1ddcaa3fa90f:/# apt update
root@1ddcaa3fa90f:/# exit
exit

$ docker container ls -all
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                       PORTS               NAMES
1ddcaa3fa90f        ubuntu:16.04        "/bin/bash"         12 minutes ago      Exited (130) 4 seconds ago                       angry_wiles

$ docker start 1ddcaa3fa90f
1ddcaa3fa90f

$ docker attach 1ddcaa3fa90f
root@1ddcaa3fa90f:/#

root@1ddcaa3fa90f:/# echo > /tmp/hello_docker.txt
root@1ddcaa3fa90f:/# ls /tmp/
hello_docker.txt

$ docker start angry_wiles
angry_wiles

$ docker attach angry_wiles
root@1ddcaa3fa90f:/#
root@1ddcaa3fa90f:/# ls /tmp/
hello_docker.txt
```