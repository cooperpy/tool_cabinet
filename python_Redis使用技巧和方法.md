- [python 连接redis](#python-连接redis)
  - [安装](#安装)
  - [连接](#连接)
- [redis的常用操作](#redis的常用操作)

# python 连接redis
## 安装
```bash

pip install redis
```
## 连接
- 方式一：直接连接
```python
from redis import Redis

# 连接到 Redis 服务器
redis_conn = Redis(host='localhost', port=6379, db=0)

```
- 方式二：池连接（推荐）
```python

from redis import ConnectionPool, Redis
# 连接到 Redis 服务器
redis_pool = ConnectionPool(host='localhost', 
                            db=0, port=6379,
                            decode_responses=True)  # 字节转为字符串
redis_c = Redis(connection_pool=redis_pool)
```

# redis的常用操作
- 字符串操作  
Redis 中的字符串数据类型是最简单的一种。它可以保存任意二进制数据，包括字符串、数字等。
```python
# 设置字符串值
r.set('name', 'Alice')

# 获取字符串值
name = r.get('name')
print(name)  # 输出: b'Alice'

# 追加字符串值
r.append('name', ' Smith')

# 获取追加后的值
name = r.get('name')
print(name)  # 输出: b'Alice Smith'

# 返回子串
sub_name = r.getrange('name', 0, 4)
print(sub_name)  # 输出: b'Alice'

```
- 列表操作:  
Redis 列表是一个有序的字符串列表，常用于存储最新消息、任务队列等。
```python
# 从列表左侧插入元素
r.lpush('fruits', 'apple')
r.lpush('fruits', 'banana')

# 从列表右侧插入元素
r.rpush('fruits', 'orange')

# 获取列表长度
length = r.llen('fruits')
print(length)  # 输出: 3

# 获取列表元素
elem = r.lindex('fruits', 1)
print(elem)  # 输出: b'banana'

```
- 哈希操作:  
Redis 哈希是一个字符串字段和字符串值之间的映射表。常用于存储对象、用户信息等复杂数据类型。
```python
# 设置哈希字段值
r.hset('user', 'name', 'Alice')
r.hset('user', 'age', 20)

# 获取哈希字段值
name = r.hget('user', 'name')
age = r.hget('user', 'age')
print(name, age)  # 输出: b'Alice' b'20'


# 获取所有哈希字段
fields = r.hkeys('user')
print(fields)  # 输出: [b'name', b'age']

```
- 集合操作:  
Redis 集合是一个无序、唯一的字符串集合。常用于存储标签、点赞用户等需求。
```python
# 添加集合元素
r.sadd('tags', 'python', 'java', 'javascript')

# 获取集合元素数量
count = r.scard('tags')
print(count)  # 输出: 3

# 判断元素是否存在
exists = r.sismember('tags', 'python')
print(exists)  # 输出: True

```
- 有序集合操作:  
Redis 有序集合是一个有序的字符串集合，每个成员都关联一个分数，根据分数进行排序。常用于排行榜、范围查询等。
```python
# 添加有序集合元素
r.zadd('scores', {'Alice': 80, 'Bob': 90})

# 获取元素分数
score = r.zscore('scores', 'Alice')
print(score)  # 输出: 80.0

# 获取指定范围内的元素
members = r.zrange('scores', 0, -1)
print(members)  # 输出: [b'Alice', b'Bob']

```
- 关闭连接
```python
# 关闭连接
r.close()

```
