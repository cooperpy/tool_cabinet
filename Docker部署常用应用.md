- [1、Docker部署EMQX](#1docker部署emqx)
- [2、Docker 部署redis并连接](#2docker-部署redis并连接)
- [3、docker安装mysql](#3docker安装mysql)
  - [Docker初始化数据库(非必要，按需配置）](#docker初始化数据库非必要按需配置)
- [4、Docker 部署mosquitto](#4docker-部署mosquitto)
  - [如果想配置用户名密码](#如果想配置用户名密码)
- [5、Docker 部署 rabbitmq](#5docker-部署-rabbitmq)


# 1、Docker部署EMQX 
[EMQX 开源版本](https://www.emqx.com/zh/downloads-and-install?product=broker&version=5.4.1&os=Docker&oslabel=Docker)

```
获取 Docker 镜像
docker pull emqx/emqx:5.4.1

启动 Docker 容器
docker run -d --name emqx -p 1883:1883 -p 8083:8083 -p 8084:8084 -p 8883:8883 -p 18083:18083 emqx/emqx:5.4.1
```
[EMQX文档](https://www.emqx.io/docs/zh/latest/)

```
通过浏览器访问 http://localhost:18083/（localhost 可替换为您的实际 IP 地址）
以访问 EMQX Dashboard 管理控制台，进行设备连接与相关指标监控管理。
默认用户名及密码：admin       public
```
# 2、Docker 部署redis并连接

```
docker pull redis   # 拉取镜像
# 指定端口后台运行，将容器的6379端口映射到本地机器的6379端口。
# 这样，在本地机器上就可以通过6379端口连接到Redis容器了
docker run -d --name myredis -p 6379:6379 redis  

docker exec -it myredis redis-cli  # 连接到Redis容器的命令行工具

# 参考
docker run -p 6379:6379 --name redis1 --privileged=true \
-v /app/redis/redis.conf:/etc/redis/redis.conf \
-v /app/redis/data:/data -d redis:6.0.8 \
redis-server /etc/redis/redis.conf

说明：-p 6379:6379配置的端口号； redis.conf配置文件示例：redis1是我起的本容器实例名字；
使用了容器卷所以/app/redis/redis.conf和/app/redis/data是宿主机的绝对路径，
/etc/redis/redis.conf和/data是redis1容器实例的绝对路径；
redis-server /etc/redis/redis.conf使他启动时就加载此配置文件；
综上就完成了容器卷对容器实例配置和数据的持久化，即使容器被删掉，数据仍然保存在宿主机中。
```

# 3、docker安装mysql

```
docker pull mysql:5.7 
# 保存下载好的镜像成tar （非必要）
docker save imageid > mysql5.7

mkdir -p /home/app/mysql/data /home/app/mysql/logs /home/app/mysql/conf
docker run --name mysql -p 3306:3306 -v /home/app/mysql/data:/var/lib/mysql -v /home/app/mysql/conf:/etc/mysql/conf.d -v /home/app/mysql/logs:/var/log/mysql -e MYSQL_ROOT_PASSWORD=123456 -d eef0fab001e8(镜像ID）

说明：
-p 3306:3306 :端口映射，将宿主机3306端口与容器3306端口做映射
格式：-p 宿主机端口:容器端口

–name mysql : 指定容器名字为mysql，也可以不指定，不指定没有容器名字

数据容器卷挂载
-v /home/app/mysql/data:/var/lib/mysql ：对宿主机数据库目录与容器数据库目录进行映射挂载
-v /home/app/mysql/conf:/etc/mysql/conf.d：对宿主机数据库配置文件与容器数据库配置文件进行映射挂载
-v /home/app/mysql/logs:/var/log/mysql：对宿主机数据库日志与容器数据库日志进行映射挂载
-e MYSQL_ROOT_PASSWORD=123456 :配置mysql的root账号的密码为123456（可以根据需要自行修改密码）
-d:后台执行
eef0fab001e8 ：镜像id，容器第一次启动要根据镜像来启动，所以镜像id必不可少。可以通过命令docker iamges查看镜像id

```
## Docker初始化数据库(非必要，按需配置）

```
docker exec -it eef0fab001e8(容器ID） bin/bash
apt-get update
apt-get install vim
修改mysql的配置
vi /etc/my.cnf

character-set-server=utf8
max_connections = 5000
log_bin_trust_function_creators=1
lower_case_table_names = 1
sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES
transaction_isolation = READ-COMMITTED
group_concat_max_len = 102400 


docker exec -it eef0fab001e8(容器ID） bin/bash  # 进入mysql容器
mysql -uroot -p123456  # 输入用户名秘密后即可对mysql数据库操作
```
[参考：Docker 安装mysql5.7镜像(含离线安装)，启动mysql镜像并初始化数据库](https://blog.csdn.net/qq_37746855/article/details/128900898)

# 4、Docker 部署mosquitto

```python
1、拉取镜像
docker pull eclipse-mosquitto
2、建立相关目录
mkdir -p /mosquitto/config
mkdir -p /mosquitto/data
mkdir -p /mosquitto/log
3、建立配置文件
vi /mosquitto/config/mosquitto.conf
添加如下内容
persistence true
persistence_location /mosquitto/data
log_dest file /mosquitto/log/mosquitto.log
listener 9001
port 1883
allow_anonymous true
4、为目录授权（可选）
chmod -R 755 /mosquitto
chmod -R 777 /mosquitto/log #日志目录要最大权限
5、执行如下命令启动mosquitto（将如下命令放在一行内执行）
docker run -it --name=mosquitto --privileged
-p 1883:1883 -p 9001:9001 
-v /mosquitto/config/mosquitto.conf:/mosquitto/config/mosquitto.conf  
-v /mosquitto/data:/mosquitto/data 
-v /mosquitto/log:/mosquitto/log 
-d  eclipse-mosquitto 

```
## 如果想配置用户名密码

```python
1、修在上面第四步
在/mosquitto/config/mosquitto.conf文件下添加：
allow_anonymous false  #关闭匿名模式
password_file /mosquitto/config/pwfile.conf #指定密码文件
2、进入容器
docker exec -it CONTAINER ID (容器Id) sh
3、生成密码
touch /mosquitto/config/pwfile.conf
chmod -R 755 /mosquitto/config/pwfile.conf
4、使用mosquitto_passwd命令创建用户，第一个admin是用户名，第二个mosquitto是密码。
mosquitto_passwd -b /mosquitto/config/pwfile.conf admin mosquitto
5、重启mqtt服务
docker restart CONTAINER ID
```
[参考1](https://www.cnblogs.com/z_lb/p/17723435.html)
[参考2](https://blog.csdn.net/weixin_44508895/article/details/133385217)

# 5、Docker 部署 rabbitmq

```python
docker pull rabbitmq:management
docker run -dit --name rabbitmq -e RABBITMQ_DEFAULT_USER=admin -e RABBITMQ_DEFAULT_PASS=admin -p 15672:15672 -p 5672:5672 rabbitmq:managemen

# 15672是管理界面的端口，5672是服务的端口。这里顺便将管理系统的用户名和密码设置为admin admin 默认账号和密码是guest guest
```
打开浏览器访问web界面: 输入  http://IP地址:15672   账号密码admin
[参考链接](https://www.cnblogs.com/caijunchao/p/13864673.html)

