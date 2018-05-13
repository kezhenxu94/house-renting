
## 如何使用

### 安装 Docker

如果你还没有安装 Docker, 请先按照[这里的指南](https://www.docker.com/community-edition#/download)安装 Docker:

### 获取源码:

```shell
$ git clone https://github.com/kezhenxu94/house-renting
```

### 启动爬虫及 ES, Kibana 服务:

```shell
$ cd house-renting
$ docker-compose up --build -d
```

待 Docker 启动稳定后 (视电脑配置情况, 可能需要 30 秒到几分钟不等);

### 查看结果:

打开浏览器, 定位到 http://127.0.0.1:5601 

#### 设置索引模式:

![设置索引模式](screenshot/setting-index-pattern.png)

#### 切换到 Discover:

![切换到 Discover](screenshot/discover.png)

#### 添加字段:

![添加字段](screenshot/adding-fields.png)

#### 按时间排序:

![按时间排序](screenshot/sorting-by-fields.png)

#### 搜索一个关键字:

![搜索一个关键字](screenshot/searching-by-field.png)

#### 搜索多个个关键字:

![搜索多个关键字](screenshot/searching-by-fields.png)

#### 展开详细信息:

![展开详细信息](screenshot/expanding-doc.png)

### 贡献

如果你觉得有些租房网站的内容应该被收录在但这里没有收录, 可以给我[提 Issue](https://github.com/kezhenxu94/house-renting/issues), 或者直接[发 PR](https://github.com/kezhenxu94/house-renting/pulls);
