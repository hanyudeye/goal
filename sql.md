
我们通常可以将 SQL 分为四类，分别是 DDL（数据定义语言）、DML（数据操作语言）、DQL（数据查询语言）和 DCL（数据控制语言）。DDL 主要用于创建、删除、修改数据库中的对象，比如创建、删除和修改二维表，核心的关键字包括`create`、`drop`和`alter`；DML 主要负责数据的插入、删除和更新，关键词包括`insert`、`delete`和`update`；DQL 负责数据查询，最重要的一个关键词是`select`；DCL 通常用于授予和召回权限，核心关键词是`grant`和`revoke`。

```SQL
-- 如果存在名为school的数据库就删除它
drop database if exists `school`;

-- 创建名为school的数据库并设置默认的字符集和排序方式
create database `school` default character set utf8mb4 collate utf8mb4_general_ci;

-- 切换到school数据库上下文环境
use `school`;

-- 创建学院表
create table `tb_college`
(
`col_id` int unsigned auto_increment comment '编号',
`col_name` varchar(50) not null comment '名称',
`col_intro` varchar(500) default '' comment '介绍',
primary key (`col_id`)
) engine=innodb auto_increment=1 comment '学院表';

-- 创建学生表
create table `tb_student`
(
`stu_id` int unsigned not null comment '学号',
`stu_name` varchar(20) not null comment '姓名',
`stu_sex` boolean default 1 not null comment '性别',
`stu_birth` date not null comment '出生日期',
`stu_addr` varchar(255) default '' comment '籍贯',
`col_id` int unsigned not null comment '所属学院',
primary key (`stu_id`),
constraint `fk_student_col_id` foreign key (`col_id`) references `tb_college` (`col_id`)
) engine=innodb comment '学生表';

-- 创建教师表
create table `tb_teacher`
(
`tea_id` int unsigned not null comment '工号',
`tea_name` varchar(20) not null comment '姓名',
`tea_title` varchar(10) default '助教' comment '职称',
`col_id` int unsigned not null comment '所属学院',
primary key (`tea_id`),
constraint `fk_teacher_col_id` foreign key (`col_id`) references `tb_college` (`col_id`)
) engine=innodb comment '老师表';

-- 创建课程表
create table `tb_course`
(
`cou_id` int unsigned not null comment '编号',
`cou_name` varchar(50) not null comment '名称',
`cou_credit` int not null comment '学分',
`tea_id` int unsigned not null comment '授课老师',
primary key (`cou_id`),
constraint `fk_course_tea_id` foreign key (`tea_id`) references `tb_teacher` (`tea_id`)
) engine=innodb comment '课程表';

-- 创建选课记录表
create table `tb_record`
(
`rec_id` bigint unsigned auto_increment comment '选课记录号',
`stu_id` int unsigned not null comment '学号',
`cou_id` int unsigned not null comment '课程编号',
`sel_date` date not null comment '选课日期',
`score` decimal(4,1) comment '考试成绩',
primary key (`rec_id`),
constraint `fk_record_stu_id` foreign key (`stu_id`) references `tb_student` (`stu_id`),
constraint `fk_record_cou_id` foreign key (`cou_id`) references `tb_course` (`cou_id`),
constraint `uk_record_stu_cou` unique (`stu_id`, `cou_id`)
) engine=innodb comment '选课记录表';
```


- 创建数据库时，我们通过`default character set utf8mb4`指定了数据库默认使用的字符集为`utf8mb4`（最大`4`字节的`utf-8`编码），我们推荐使用该字符集，它也是 MySQL 8.x 默认使用的字符集，因为它能够支持国际化编码，还可以存储 Emoji 字符。可以通过下面的命令查看 MySQL 支持的字符集以及默认的排序规则。
