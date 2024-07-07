---
layout: default
toc: false
title: Linux常用命令
date:  2024-04-11T07:49:28+08:00
categories: ['linux']
---

### 系统信息

| 命令                 | 说明                              |
|----------------------|-----------------------------------|
| arch                 | 显示机器的处理器架构(1)           |
| uname -m             | 显示机器的处理器架构(2)           |
| uname -r             | 显示正在使用的内核版本            |
| dmidecode -q         | 显示硬件系统部件 - (SMBIOS / DMI) |
| hdparm -i /dev/hda   | 罗列一个磁盘的架构特性            |
| hdparm -tT /dev/sda  | 在磁盘上执行测试性读取操作        |
| cat /proc/cpuinfo    | 显示CPU info的信息                |
| cat /proc/interrupts | 显示中断                          |
| cat /proc/meminfo    | 校验内存使用                      |
| cat /proc/swaps      | 显示哪些swap被使用                |
| cat /proc/version    | 显示内核的版本                    |
| cat /proc/net/dev    | 显示网络适配器及统计              |
| cat /proc/mounts     | 显示已加载的文件系统              |
| lspci -tv            | 罗列 PCI 设备                     |
| lsusb -tv            | 显示 USB 设备                     |
| date                 | 显示系统日期                      |
| cal 2007             | 显示2007年的日历表                |
| date 041217002007.00 | 设置日期和时间 - 月日时分年.秒    |
| clock -w             | 将时间修改保存到 BIOS             |

### 文件和目录查看

| 命令                      | 说明                                       |
|---------------------------|--------------------------------------------|
| cd /home                  | 进入 '/ home' 目录'                        |
| cd ..                     | 返回上一级目录                             |
| cd ../..                  | 返回上两级目录                             |
| cd                        | 进入个人的主目录                           |
| cd ~user1                 | 进入个人的主目录                           |
| cd -                      | 返回上次所在的目录                         |
| pwd                       | 显示工作路径                               |
| ls                        | 查看目录中的文件                           |
| ls -F                     | 查看目录中的文件                           |
| ls -l                     | 显示文件和目录的详细资料                   |
| ls -a                     | 显示隐藏文件                               |
| ls _\[0-9\]_              | 显示包含数字的文件名和目录名               |
| tree                      | 显示文件和目录由根目录开始的树形结构(1)    |
| lstree                    | 显示文件和目录由根目录开始的树形结构(2)    |
| mkdir dir1                | 创建一个叫做 'dir1' 的目录'                |
| mkdir dir1 dir2           | 同时创建两个目录                           |
| mkdir -p /tmp/dir1/dir2   | 创建一个目录树                             |
| rm -f file1               | 删除一个叫做 'file1' 的文件'               |
| rmdir dir1                | 删除一个叫做 'dir1' 的目录'                |
| rm -rf dir1               | 删除一个叫做 'dir1' 的目录并同时删除其内容 |
| rm -rf dir1 dir2          | 同时删除两个目录及它们的内容               |
| mv dir1 new\_dir          | 重命名/移动 一个目录                       |
| cp file1 file2            | 复制一个文件                               |
| cp dir/\* .               | 复制一个目录下的所有文件到当前工作目录     |
| cp -a /tmp/dir1 .         | 复制一个目录到当前工作目录                 |
| cp -a dir1 dir2           | 复制一个目录                               |
| ln -s file1 lnk1          | 创建一个指向文件或目录的软链接             |
| ln file1 lnk1             | 创建一个指向文件或目录的物理链接           |
| touch -t 0712250000 file1 | 修改一个文件或目录的时间戳 - (YYMMDDhhmm)  |
| iconv -l                  | 列出已知的编码                             |

### 文件搜索

| 命令                                       | 说明                                                 |
|--------------------------------------------|------------------------------------------------------|
| find / -name file1                         | 从 '/' 开始进入根文件系统搜索文件和目录              |
| find / -user user1                         | 搜索属于用户 'user1' 的文件和目录                    |
| find /home/user1 -name \*.bin              | 在目录 '/ home/user1' 中搜索带有'.bin' 结尾的文件    |
| find /usr/bin -type f -atime +100          | 搜索在过去100天内未被使用过的执行文件                |
| find /usr/bin -type f -mtime -10           | 搜索在10天内被创建或者修改过的文件                   |
| find / -name \*.rpm -exec chmod 755 '{}' ; | 搜索以 '.rpm' 结尾的文件并定义其权限                 |
| find / -xdev -name \*.rpm                  | 搜索以 '.rpm' 结尾的文件，忽略光驱、捷盘等可移动设备 |
| locate \*.ps 寻找以 '.ps'                  | 结尾的文件 - 先运行 'updatedb' 命令                  |
| whereis halt                               | 显示一个二进制文件、源码或man的位置                  |
| which halt                                 | 显示一个二进制文件或可执行文件的完整路径             |

### 挂载一个文件系统

| 命令                                                                       | 说明                                                                    |
|----------------------------------------------------------------------------|-------------------------------------------------------------------------|
| mount /dev/hda2 /mnt/hda2                                                  | 挂载一个叫做hda2的盘 - 确定目录 '/ mnt/hda2' 已经存在                   |
| umount /dev/hda2                                                           | 卸载一个叫做hda2的盘 - 先从挂载点 '/ mnt/hda2' 退出                     |
| fuser -km /mnt/hda2                                                        | 当设备繁忙时强制卸载                                                    |
| umount -n /mnt/hda2                                                        | 运行卸载操作而不写入 /etc/mtab 文件- 当文件为只读或当磁盘写满时非常有用 |
| mount /dev/fd0 /mnt/floppy                                                 | 挂载一个软盘                                                            |
| mount /dev/cdrom /mnt/cdrom                                                | 挂载一个cdrom或dvdrom                                                   |
| mount /dev/hdc /mnt/cdrecorder                                             | 挂载一个cdrw或dvdrom                                                    |
| mount /dev/hdb /mnt/cdrecorder                                             | 挂载一个cdrw或dvdrom                                                    |
| mount -o loop file.iso /mnt/cdrom                                          | 挂载一个文件或ISO镜像文件                                               |
| mount -t vfat /dev/hda5 /mnt/hda5                                          | 挂载一个Windows FAT32文件系统                                           |
| mount /dev/sda1 /mnt/usbdisk                                               | 挂载一个usb 捷盘或闪存设备                                              |
| mount -t smbfs -o username=user,password=pass //WinClient/share /mnt/share | 挂载一个windows网络共享                                                 |

### 打包和压缩文件

| 命令                                  | 说明                                                  |
|---------------------------------------|-------------------------------------------------------|
| bunzip2 file1.bz2                     | 解压一个叫做 'file1.bz2'的文件                        |
| bzip2 file1                           | 压缩一个叫做 'file1' 的文件                           |
| gunzip file1.gz                       | 解压一个叫做 'file1.gz'的文件                         |
| gzip file1                            | 压缩一个叫做 'file1'的文件                            |
| gzip -9 file1                         | 最大程度压缩                                          |
| rar a file1.rar test\_file            | 创建一个叫做 'file1.rar' 的包                         |
| rar a file1.rar file1 file2 dir1      | 同时压缩 'file1', 'file2' 以及目录 'dir1'             |
| rar x file1.rar                       | 解压rar包                                             |
| unrar x file1.rar                     | 解压rar包                                             |
| tar -cvf archive.tar file1            | 创建一个非压缩的 tarball                              |
| tar -cvf archive.tar file1 file2 dir1 | 创建一个包含了 'file1', 'file2' 以及 'dir1'的档案文件 |
| tar -tf archive.tar                   | 显示一个包中的内容                                    |
| tar -xvf archive.tar                  | 释放一个包                                            |
| tar -xvf archive.tar -C /tmp          | 将压缩包释放到 /tmp目录下                             |
| tar -cvfj archive.tar.bz2 dir1        | 创建一个bzip2格式的压缩包                             |
| tar -jxvf archive.tar.bz2             | 解压一个bzip2格式的压缩包                             |
| tar -cvfz archive.tar.gz dir1         | 创建一个gzip格式的压缩包                              |
| tar -zxvf archive.tar.gz              | 解压一个gzip格式的压缩包                              |
| zip file1.zip file1                   | 创建一个zip格式的压缩包                               |
| zip -r file1.zip file1 file2 dir1     | 将几个文件和目录同时压缩成一个zip格式的压缩包         |
| unzip file1.zip                       | 解压一个zip格式压缩包                                 |

### YUM 软件包升级器 - （Fedora, RedHat及类似系统）

| 命令                               | 说明                                                      |
|------------------------------------|-----------------------------------------------------------|
| yum install package\_name          | 下载并安装一个rpm包                                       |
| yum localinstall package\_name.rpm | 将安装一个rpm包，使用你自己的软件仓库为你解决所有依赖关系 |
| yum update package\_name.rpm       | 更新当前系统中所有安装的rpm包                             |
| yum update package\_name           | 更新一个rpm包                                             |
| yum remove package\_name           | 删除一个rpm包                                             |
| yum list                           | 列出当前系统中安装的所有包                                |
| yum search package\_name           | 在rpm仓库中搜寻软件包                                     |
| yum clean packages                 | 清理rpm缓存删除下载的包                                   |
| yum clean headers                  | 删除所有头文件                                            |
| yum clean all                      | 删除所有缓存的包和头文件                                  |

### APT 软件工具 (Debian, Ubuntu 以及类似系统)

| 命令                              | 说明                               |
|-----------------------------------|------------------------------------|
| apt-get install package\_name     | 安装/更新一个 deb 包               |
| apt-cdrom install package\_name   | 从光盘安装/更新一个 deb 包         |
| apt-get update                    | 升级列表中的软件包                 |
| apt-get upgrade                   | 升级所有已安装的软件               |
| apt-get remove package\_name      | 从系统删除一个deb包                |
| apt-get check                     | 确认依赖的软件仓库正确             |
| apt-get clean                     | 从下载的软件包中清理缓存           |
| apt-cache search searched-package | 返回包含所要搜索字符串的软件包名称 |

### 字符设置和文件格式转换

| 命令                                 | 说明                                  |
|--------------------------------------|---------------------------------------|
| dos2unix filedos.txt fileunix.txt    | 将一个文本文件的格式从MSDOS转换成UNIX |
| unix2dos fileunix.txt filedos.txt    | 将一个文本文件的格式从UNIX转换成MSDOS |
| recode ..HTML < page.txt > page.html | 将一个文本文件转换成html              |

### 初始化一个文件系统

| 命令                         | 说明                                           |
|------------------------------|------------------------------------------------|
| mkfs /dev/hda1               | 在hda1分区创建一个文件系统                     |
| mke2fs /dev/hda1             | 在hda1分区创建一个linux ext2的文件系统         |
| mke2fs -j /dev/hda1          | 在hda1分区创建一个linux ext3(日志型)的文件系统 |
| mkfs -t vfat 32 -F /dev/hda1 | 创建一个 FAT32 文件系统                        |
| fdformat -n /dev/fd0         | 格式化一个软盘                                 |
| mkswap /dev/hda3             | 创建一个swap文件系统                           |

### SWAP文件系统

| 命令                       | 说明                     |
|----------------------------|--------------------------|
| mkswap /dev/hda3           | 创建一个swap文件系统     |
| swapon /dev/hda3           | 启用一个新的swap文件系统 |
| swapon /dev/hda2 /dev/hdb3 | 启用两个swap分区         |

