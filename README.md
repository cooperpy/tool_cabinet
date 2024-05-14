- [电脑常用安装工具](#电脑常用安装工具)
  - [1、PC电脑和手机之间互传文件——LANDrop](#1pc电脑和手机之间互传文件landrop)
  - [MARKDOWN编辑器——Marktext](#markdown编辑器marktext)
  - [PDF阅读器——Koodo Reader](#pdf阅读器koodo-reader)
  - [音乐播放器——MusicPlayer2](#音乐播放器musicplayer2)
  - [视频播放器——PotPlayer](#视频播放器potplayer)
  - [思维导图——Xmind](#思维导图xmind)
  - [万兴音视频格式转换](#万兴音视频格式转换)
- [各类包的安装方法](#各类包的安装方法)
  - [git升级或编译](#git升级或编译)
    - [编译安装- 电脑常用安装工具](#编译安装--电脑常用安装工具)
    - [在线安装](#在线安装)

# 电脑常用安装工具
## 1、PC电脑和手机之间互传文件——LANDrop
[LANDrop的GitHub网址](https://github.com/LANDrop/LANDrop)
[LANDrop工具下载网址](https://landrop.app/#downloads)
==阿里云盘>资源盘存有下载文件==
**使用方法**
1. 电脑端和手机端安装程序（点击允许搜索局域网上的设备）
2. [操作图](https://github.com/cooperpy/tool_cabinet/assets/107781344/7c8e9e31-0656-44ed-8b91-e01bc620cbd6)
## MARKDOWN编辑器——Marktext
[Marktext的GitHub网址](https://github.com/marktext/marktext)
==阿里云盘>资源盘存有下载文件==
## PDF阅读器——Koodo Reader
[Koodo Reader的GitHub网址](https://github.com/koodo-reader/koodo-reader)
[Koodo Reader工具下载网址](https://www.koodoreader.com/zh)
==阿里云盘>资源盘存有下载文件==
## 音乐播放器——MusicPlayer2
[MusicPlayer2的GitHub网址](https://github.com/zhongyang219/MusicPlayer2/)
==阿里云盘>资源盘存有下载文件==
## 视频播放器——PotPlayer
==阿里云盘>资源盘存有下载文件==
## 思维导图——Xmind
==阿里云盘>资源盘存有下载文件==
## 万兴音视频格式转换
==阿里云盘>资源盘存有下载文件==
# 各类包的安装方法
## git升级或编译
### 编译安装- [电脑常用安装工具](#电脑常用安装工具)
```bash
# 需要 root 权限
# 安装依赖
sudo yum install curl-devel expat-devel gettext-devel openssl-devel zlib-devel
sudo yum install gcc perl-ExtUtils-MakeMaker
sudo yum -y install wget

# 进入下载文件保存目录，根据实际情况替换
cd ~/downloads
wget https://mirrors.edge.kernel.org/pub/software/scm/git/git-2.8.5.tar.gz  (==阿里云盘>资源盘存有下载文件==)

tar -xvf git-2.8.5.tar.gz
rm -f git-2.8.5.tar.gz
cd git-2.8.5

make configure
sudo ./configure --prefix=/usr
sudo make
sudo make install

git --version
git version 2.8.5

```
### 在线安装
```bash
git --version
[git version 1.8.3.1]

sudo yum remove git
sudo yum remove git-*
sudo yum install https://packages.endpointdev.com/rhel/7/os/x86_64/endpoint-repo.x86_64.rpm
sudo yum install git
git --version
[git version 2.34.1]

