- [提前准备](#提前准备)
- [安装阶段](#安装阶段)
- [centos虚拟机安装后的网络配置](#centos虚拟机安装后的网络配置)
  - [NAT（网络转换模式）下的网络配置](#nat网络转换模式下的网络配置)
  - [桥接模式下的网络配置](#桥接模式下的网络配置)
- [网络配置后的基础配置](#网络配置后的基础配置)
  - [关闭selinux](#关闭selinux)
  - [关闭虚拟机的防火墙](#关闭虚拟机的防火墙)
  - [安装net-tools和openssh](#安装net-tools和openssh)
  - [在xshell中安装centos常用工具包](#在xshell中安装centos常用工具包)
  - [安装docker-ce社区版](#安装docker-ce社区版)
  - [配置docker镜像加速](#配置docker镜像加速)
  - [docker配置宿主机转发](#docker配置宿主机转发)
  - [安装一下常见的包](#安装一下常见的包)
- [卸载安装的Centos](#卸载安装的centos)

# 提前准备
先进入bios，将虚拟功能开启，如图
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/532fc6b36fce42dab2e5b4d85e40fabf.png)
然后，依次进入，控制面板>程序>启动或关闭windows功能，开启相关功能，如图：
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/e4e2bd64646b4f70afbc6c8ed194dd1b.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/4b2ff23cef4c4702ac2646b36383b007.png)
如果你的启动或关闭windows功能没有**hyper-v**，这是因为你的windows是家庭版的缘故，专业版的windows是有的。如果你的系统是家庭版的，需要运行一个bat文件。

```
pushd "%~dp0"
dir /b %SystemRoot%\servicing\Packages\*Hyper-V*.mum >hyper-v.txt
for /f %%i in ('findstr /i . hyper-v.txt 2^>nul') do dism /online /norestart /add-package:"%SystemRoot%\servicing\Packages\%%i"
del hyper-v.txt
Dism /online /enable-feature /featurename:Microsoft-Hyper-V -All /LimitAccess /ALL
pause
```
将上述代码复制到**文本文件**中，然后将其后缀名改为.bat，以管理员的方式运行即可，如图：![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/c55c6818cfeb44d8b3ec1e78c5efa150.png)
接下来就可以安装VMware了
==阿里云盘存有VMware软件==

# 安装阶段
VMware的安装十分简单，就不介绍了，直接安装就好。
VMware的破解密钥也十分好找，为了避嫌，就不明写了，实在找不到的朋友，私信我吧。

接下来介绍虚拟机的安装（以centOS 为例）：
**首先要准备好centos的镜像文件**
==阿里云盘存有centos的镜像文件==
如图操作即可：
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/a8a9c14a814a40e8af98ff6fd2bf438a.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/ca37008a5f0a49dfb5066ba0ca47c924.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/a7740dfbd73046058dba76833e239b5e.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/67942bbce48a41b09616252e20ece0b3.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/6e16dc32be504555865e6271276cd13e.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/195a358e24184d6ca3d76dfa0cbaac2d.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/a999c9aea83d495ba656d92b3904847a.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/1044ff0f08d54e6fb07e389c41df34d5.png)
> 网络类型介绍
> **桥接网络**：在这种模式下，VMWare虚拟出来的操作系统就像是局域网中的一台独立的主机，它**可以访问网内任何一台机器**。在桥接模式下，你需要手工为虚拟系统配置IP地址、子网掩码，而且还要和宿主机器处于同一网段，这样虚拟系统才能和宿主机器进行通信。同时，由于这个虚拟系统是局域网中的一个独立的主机系统，那么就可以手工配置它的TCP/IP配置信息，以实现通过局域网的网关或路由器访问互联网。
> 

> **NAT(网络地址转换模式)**：使用NAT模式，就是让虚拟系统借助NAT(网络地址转换)功能，通过宿主机器所在的网络来访问公网。也就是说，使用NAT模式可以实现在虚拟系统里访问互联网。NAT模式下的虚拟系统的TCP/IP配置信息是由VMnet8(NAT)虚拟网络的DHCP服务器提供的，无法进行手工修改，**因此使用NAT模式虚拟系统也就无法和本地局域网中的其他真实主机进行通讯**。
> 

> **host-only(主机模式)**：在某些特殊的网络调试环境中，如果要求将真实环境和虚拟环境隔离开，这时你就可采用host-only模式。在host-only模式中，所有的虚拟系统是可以相互通信的，但虚拟系统和真实的网络是被隔离开的，VMWare虚拟机不能访问互联网
**后面会讲到如何配置桥接网络或者NAT网络**

![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/36adb0053d5046e6b3659a296c8c9207.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/779745f19d2e48b28c57cd1d2aeb7efb.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/05426cbd17b243039980e94dbc21a7ed.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/9b2d987b0b2348b9b00e7746defcc1b4.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/822baf9040c543b49c4bf167be448500.png)
**磁盘位置一般和linux文件位置在一起，我一般会创建一个名为disk的文件存放。**

![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/813b5484453f4e2d8e08733c1107eeb6.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/b259ee68b6754009b2634baf2b12a373.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/354fbb3cbb444062aa3fefbc60457e2d.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/ee64f81efe574103b7a6132d599851b5.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/a5d654f40ead4535a25c117595864231.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/bfeeecf49d164415b7430738024dad59.png)
**自定义磁盘分配，一般分为boot、swap、home和根目录**

![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/7ef0a597dcc840668816801b0aab7717.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/d4bcbfcd9b954fde9648ec37fda905c8.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/9caf74b4d29046c0b127afe6cddd5bff.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/7df99dddb55d4a01b1c8f75249bbc7df.png)
# centos虚拟机安装后的网络配置
## NAT（网络转换模式）下的网络配置
在windows的CMD中输入：ipconfig。查看VMnet8(对应nat)下的ip信息：
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/372dbc8976c2423c9893e20bc3eb3f23.png)![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/3514ae663b3b420991866a10967b27ae.png)
```
在centos中进行网络配置
cd /etc/sysconfig/network-scripts/
vi ifcfg-ens33  （电脑不同，略有不同）
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/e6191c3d85d4425b915460017c54d9e3.png)
修改完成后，使用命令重启网络，虚拟机就可以联网(**注意：网关不能和VMnet8的IP一样**）
网关GATEWAY 设置为 xxx.xxx.xxx.2

```
service network restart
or
systemctl restart network

可以使用命令ping测试是否可以联网
```
## 桥接模式下的网络配置
1、在本机的命令行窗口输入：ipconfig -all，查看网络信息，要根据主机的ip信息来配置虚拟机的IP信息。
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/507894f8427a425da4d1f92bd60b870b.png)2、进入 /etc/sysconfig/network-scripts/路径，编辑ifcfg-en开头的文件。
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/28821c8f43b24a939919554365772359.png)

```
TYPE=Ethernet
PROXY_METHOD=none 
BROWSER_ONLY=no
BOOTPROTO=static  #由默认的dhcp修改为static
DEFROUTE=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_FAILURE_FATAL=no
IPV6_ADDR_GEN_MODE=stable-privacy
NAME=ens33
UUID=05477503-d4b1-4fc1-a64f-5034c2099723
DEVICE=ens33
ONBOOT=yes #由默认的no修改为yes
IPADDR=192.168.50.200 #新增此项，自定义虚拟机的ip地址（主机是192.168.50.187），必须与主机在同一网段
NETMASK=255.255.255.0 #新增此项，设置子网掩码，跟宿主一样
GATEWAY=192.168.50.1 #新增此项，默认网关，跟宿主一样
DNS1=192.168.50.1 #新增此项，DNS，跟宿主一样
```
3、添加网关地址，修改机器名

```
vi /etc/resolv.conf

# 添加以下内容
NETWORKING=yes
HOSTNAME=hadoop200  #机器名
GATEWAY=192.168.50.1  #默认网关与宿主机相同
```
4、添加DNS

```
vi /etc/resolv.conf

# 添加以下内容
nameserver 192.168.50.1 #DNS，跟宿主一样
```
5、增加IP和机器名称的映射关系

```
vi /etc/hosts

# 添加以下内容
192.168.50.200 hadoop200
```
6、虚拟网络编辑器增加桥接模式
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/65e574e81aff4fa39bce9ed99599d9af.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/a6cc259e4d2848909957e9915b42fcb9.png)
[参考：VMware虚拟机中CentOS7的桥接方式网络配置解决方案](https://blog.csdn.net/spicedbeef/article/details/106892736)
# 网络配置后的基础配置
## 关闭selinux

```
临时关闭
  setenforce 0

  永久关闭
  vi /etc/selinux/config
  设置SELINUX=disabled
```
## 关闭虚拟机的防火墙

```
查看防火墙状态
systemctl status firewalld
关闭
systemctl stop firewalld
关闭开机启动防火墙
systemctl disable firewalld
```
## 安装net-tools和openssh

```
yum update (更新一下）
yum install -y net-tools
yum install -y openssh-server

设置开机启动
systemctl start sshd.service
systemctl enable sshd.service

安装xshell，远程连接虚拟机
```
## 在xshell中安装centos常用工具包
```
yum install -y wget
yum install -y bash-completion vim lrzsz wget expect net-tools nc nmap tree dos2unix htop iftop iotop unzip telnet sl psmisc nethogs glances bc ntpdate openldap-devel
```
## 安装docker-ce社区版

```
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

```
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

```
cat <<EOF > /etc/sysctl.d/docker.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.conf.default.rp_filter = 0
net.ipv4.conf.all.rp_filter = 0
net.ipv4.ip_forward=1
EOF
```
## 安装一下常见的包

```python

yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make libffi-devel autoconf -y

```

# 卸载安装的Centos
选中所要删除的centos，按照路径 虚拟机>管理>从磁盘中删除，即可

