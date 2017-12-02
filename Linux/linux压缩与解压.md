Title: linux压缩与解压
Date: 2017-02-27
Modified: 2017-02-27
Category: Linux
Tags: linux, tar

## .tar

```
# 将foobar打包为/tmp/foobar.tar
tar cvf /tmp/foobar.tar foobar/

# 将/tmp/foobar.tar解包为foobar
tar xvf /tmp/foobar.tar
```

## .tar.gz | .tgz
```
# 以gzip方式压缩
tar zcvf /tmp/foobar.tar.gz foobar/

# 解压
tar zxvf /tmp/foobar.tar.gz
```

## .tar.bz2
```
# 以bzip2方式压缩
tar jcvf /tmp/foobar.tar.bz2 foobar/

# 解压
tar jxvf /tmp/foobar.tar.bz2 
```

## .zip
```
# 压缩文件夹
zip -r /tmp/foobar.zip foobar/

# 压缩文件
zip foo.zip foo

# 解压
unzip /tmp/foobar.zip
```