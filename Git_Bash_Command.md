# 1. 目录和文件操作

## 1.1 基本bash命令

```bash
pwd ( print working directory ) #查看当前所在路径--绝对路径

cd ( change directory ) #切换目标

cd .. #返回到上一个目录

ls ( list ) #查看当前目录下的内容

ll #列出的内容更为详细ll 列出的内容更为详细

ls -al #包括隐藏文件和以 . 开头的文件

mkdir ( make directory ) #创建目录

touch #创建文件

cat #查看文件内容（一次性将内容全部显示）

less #查看文件内容（显示部分信息）--再次输入‘回车’一行一行显示，‘空格’一页一页显示 ，‘b’一次向上走一页

rm ( remove ) #删除文件，-rm -rf 文件夹（循环递进删除文件夹,不需要二次确认）

rmdir ( remove directory ) #删除文件夹（只能删除空文件夹，不常用）

clear #清屏

q #退出

mv ( move ) #移动文件或重命名

cp ( copy ) #复制文件    如复制  A 文件夹下的所有子文件、目录到 B 文件夹  cp -r A/* B

echo "something"  >> 文件名       #把内容追加到某个文件

echo ‘内容’ > 文件名 #输出内容到文件中，每次输入都是覆盖原来的文件

echo ‘内容’ >>文件名 #输出内容到文件中，每次输入都是追加新内容
```

## 1.2 vim打开、修改、保存文件

### vim两种工作模式：

- **命令模式**：接受、执行 vim操作命令的模式，打开文件后的默认模式；

- **编辑模式**：对打开的文件内容进行 增、删、改 操作的模式；

在编辑模式下按下`ESC`键，回退到命令模式；在命令模式下按`i`，进入编辑模式

### 创建、打开文件：

输入`touch`文件名 ，可创建文件。

使用 vim 加文件路径（或文件名）的模式打开文件，如果文件存在则打开现有文件，如果文件不存在则新建文件。

键盘输入字母`i`进入插入编辑模式。

### 保存文件：

在编辑模式下编辑文件，按下`ESC`键，退出编辑模式，切换到命令模式，在命令模式下键入`ZZ`或者`:wq`保存修改并且退出 vim。

> 如果只想保存文件，则键入`:w`，回车后底行会提示写入操作结果，并保持停留在命令模式。

### 放弃修改：

放弃所有文件修改：按下`ESC`键进入命令模式，键入`:q!`回车后放弃修改并退出vim。

> 放弃所有文件修改，但不退出 vi，即回退到文件打开后最后一次保存操作的状态，继续进行文件操作：按下`ESC`键进入命令模式，键入`:e!`，回车后回到命令模式。

# 2. git仓库管理基本bash

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"  #(邮箱和github注册邮箱保持一致)  创建SSH key（创建完成后将生成的id_ed25519.pub 添加到github中）

ssh -T git@github.com    #判断是否连通成功       

git init  #初始化仓库

git config --list  #查看git所有配置信息

git clone [url]  #拷贝一份远程仓库，也就是下载一个项目

git status   #查看当前仓库状态

git add  #文件名（.表示添加所有更改到暂存区） 把更新添加到暂存区

git commit -m "描述文字"  #把文件提交到本地仓库

git merge 分支名  #把分支名上的代码合并到当前所在分支

git branch -d 分支名  #删除分支

git remote add origin 远程仓库url  #添加远程仓库

git remote rm name  #删除远程仓库

git remote rename old_name new_name  #修改仓库名

git add README.md  #添加reademe文件

git push -u origin master  #推送到远程master分支（关联本地与远程的master分支）

git pull -u origin master  #将远程主机origin的master分支拉取过来，与本地的master分支合并
```

# 3. git工作流

```bash
git reset HEAD 文件名  #把暂存区的修改回归到工作区

git checkout -- 文件名  #把工作区文件清理干净

git reset --hard commitID  #回滚到某一次commit前

git fsck --lost-found  #恢复git add 过的文件

find .git/objects -type f | xargs ls -lt | sed 60q  #找到最近add到本地仓库的60个文件

rm --cached  #从暂存区删除文件

checkout HEAD 文件名  #HEAD指向的文件替换到工作区的文件
```

# 4. git仓库标签管理

```bash
git tag  #查看所有标签

git tag name  #创建标签

git tag -a name -m "comment"  #指定提交信息

git tag -d name  #删除标签

git push origin name  #标签发布
```

# 5. git分支管理

```bash
git branch  分支名  #创建分支

git branch  #查看分支（当前分支*）

git checkout 分支名  #切换分支

git checkout -b dev origin/dev  #checkout远程的dev分支，在本地起名为dev分支，并切换到本地的dev分支

git checkout -t origin/dev  #使用-t参数，它默认会在本地建立一个和远程分支名字一样的分支
```

# 6. 常见问题

## git clone报错：error RPC failed; curl 56 OpenSSL SSL_read: SSL_ERROR_SYSCALL, errno 10054
```bash 
$ git config http.sslVerify "false" 
$ git config http.postBuffer 524288000  # http.postBuffer默认上限为1M，调大上限设为500M

HP@DESKTOP-1RIVFM3 MINGW64 /d/PythonCodeLib (master)
$ git clone https://github.com/tongqin2002/Games
Cloning into 'Games'...
remote: Enumerating objects: 2869, done.
remote: Counting objects: 100% (7/7), done.
remote: Compressing objects: 100% (7/7), done.
remote: Total 2869 (delta 0), reused 2 (delta 0), pack-reused 2862
Receiving objects: 100% (2869/2869), 469.94 MiB | 297.00 KiB/s, done.
Resolving deltas: 100% (1079/1079), done.
Updating files: 100% (883/883), done.
```

## You've successfully authenticated, but GitHub does not provide shell access.
git push 的时候提示输入账号密码，现在 git 也不允许 http 连接，所以提供账号密码也没办法 push。
虽然是用 git 命令push，但本质上仍然是 https，所以不允许提交。

```bash
查看远程 url 地址：
git remote -v
origin  https://github.com/tongqin2002/sample.git (fetch)
origin  https://github.com/tongqin2002/sample.git (push)

修改url链接
git remote set-url origin git@github.com:tongqin2002/sample.git

git remote -v
origin  git@github.com:tongqin2002/sample.git (fetch)
origin  git@github.com:tongqin2002/sample.git (push)
```
可以正常git push了
