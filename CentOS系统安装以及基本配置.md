- [1、电脑安装CentOS系统（相关工具在阿里云盘资源盘都有保存）](#1电脑安装centos系统相关工具在阿里云盘资源盘都有保存)
- [2、CentOS基础配置](#2centos基础配置)
  - [关闭selinux](#关闭selinux)
  - [关闭虚拟机的防火墙](#关闭虚拟机的防火墙)
  - [安装net-tools和openssh](#安装net-tools和openssh)
  - [在xshell中安装centos常用工具包](#在xshell中安装centos常用工具包)
  - [安装docker-ce社区版](#安装docker-ce社区版)
  - [配置docker镜像加速](#配置docker镜像加速)
  - [docker配置宿主机转发](#docker配置宿主机转发)
  - [安装一下常见的包](#安装一下常见的包)


# 1、电脑安装CentOS系统（相关工具在阿里云盘资源盘都有保存）
- U盘工具（rufus-4.5）
- ![U盘设置](./images/U盘设置.png)
- centos系统（CentOS-7-x86_64-DVD-2009.iso）
- [北京外国语大学开源软件镜像站——centos
](https://mirrors.bfsu.edu.cn/centos/7.9.2009/isos/x86_64/)
- [镜像站
](https://mirrors.bfsu.edu.cn/centos/7.9.2009/isos/x86_64/)

联想电脑按下 F2 进入boot，选择Boot-u盘启动，简单设置安装即可

# 2、CentOS基础配置
## 关闭selinux

```bash
临时关闭
  setenforce 0

  永久关闭
  vi /etc/selinux/config
  设置SELINUX=disabled
```
## 关闭虚拟机的防火墙

```bash
查看防火墙状态
systemctl status firewalld
关闭
systemctl stop firewalld
关闭开机启动防火墙
systemctl disable firewalld
```
## 安装net-tools和openssh

```bash
yum update (更新一下）
yum install -y net-tools
yum install -y openssh-server

设置开机启动
systemctl start sshd.service
systemctl enable sshd.service

安装xshell，远程连接虚拟机
```
## 在xshell中安装centos常用工具包
```bash
yum install -y wget
yum install -y bash-completion vim lrzsz wget expect net-tools nc nmap tree dos2unix htop iftop iotop unzip telnet sl psmisc nethogs glances bc ntpdate openldap-devel
```
## 安装docker-ce社区版

```bash
curl -o /etc/yum.repos.d/Centos-7.repo http://mirrors.aliyun.com/repo/Centos-7.repo

curl -o /etc/yum.repos.d/docker-ce.repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo

yum clean all && yum makecache

yum install -y docker-ce

安装指定版本

yum install -y docker-ce-23.0.6

设置docker开机启动

systemctl enable docker

systemctl start docker

systemctl restart docker

systemctl stop docker
```
## 配置docker镜像加速
[阿里云镜像加速器](https://cr.console.aliyun.com/cn-shanghai/instances/mirrors?spm=a2c6h.12873639.article-detail.7.358a56135tZGng)

```bash
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": [""]
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker
```
## docker配置宿主机转发

```bash
cat <<EOF > /etc/sysctl.d/docker.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.conf.default.rp_filter = 0
net.ipv4.conf.all.rp_filter = 0
net.ipv4.ip_forward=1
EOF
```
## 安装一下常见的包

```bash
yum install libffi-devel -y
yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make
sudo yum install autoconf -y

```
---

