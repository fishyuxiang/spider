# 说明文档

## 一.功能

    抓取百度百科相关Python词条网页的标题和简介（1000条）数据存入mysql数据库，
    并能从数据库中读取，通过系统可视化界面展示。

## 二.配置
### (1)系统

    ubuntu16.04.2
    
### (2)mysql数据库

    用户名：root
    密码：123456
    数据库名：Spiderdata
    表名：items
    
    创建数据库：
    create database Spiderdata;
    创建表：
    create table items(url varchar(255),title varchar(255) charset utf8,summary varchar(1000) charset utf8);

### (3)需要安装的第三方包

    PyMySQL
    python3-tk
    bs4
    
## 三.模块文件
### (1)模块架构
    架构图如下所示：
    ![](https://github.com/fishyuxiang/spider/raw/master/images/struct.gif)
    
### (2)执行流程
    流程图如下所示：
    ![](https://github.com/fishyuxiang/spider/raw/master/images/flow.gif)
