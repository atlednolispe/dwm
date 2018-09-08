阿里云秘钥对连接
================

[aliyun阿里云秘钥对连接](https://blog.csdn.net/musuny/article/details/78507954)

```
# 本质上就是ssh-keygen生成秘钥对,然后上传公钥到server的authorized_keys

# 创建用户
# groupadd aliyun
# useradd -m user -g aliyun

# 生成私钥,并且重命名authorized_keys
# su - user
$ ssh-keygen -t rsa
$ mv .ssh/id_rsa.pub .ssh/authorized_keys
$ mv .ssh/id_rsa .ssh/hk_user.pem

# 取回新生成私钥
$ scp -i hk.pem root@ip:/home/user/.ssh/hk_user.pem .

$ ssh -i hk_atled.pem user@ip
```

## Linux 免密登录

```
# 生成公钥,一路回车
$ ssh-keygen -t rsa

# 复制公钥到远程主机
$ ssh-copy-id user@host_ip

# 可以成功免密登录
$ ssh user@host_ip
```
