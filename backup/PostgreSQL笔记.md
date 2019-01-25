---
Title: PostgreSQL笔记
Date: 2017-06-21
Modified: 2017-08-24
---

**数据库**
```
# 创建数据库
create database <name>;
create database <name> template <template_name>;

# 切换数据库
\c <dbname>

# 删除数据库
drop database <name>;
# or
$ psql -U postgres -c "drop database <name>;"
# or
$ dropdb <dbname>
# 如果删除时报错`cannot be executed on the currently open database`，切换到其他的数据库连接上，再进行删除

# 连接数据库
\connect <name>

# 列出数据库
\l
```

**表格**
```
# 列出所有表格
\d 
\dt

# 查看表结构
\d <table_name>
```

**其他**
```
# 退出
\q
```
