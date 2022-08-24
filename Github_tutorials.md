# 下载并安装Git包
安装参考：https://git-scm.com/download/win

常见操作：https://zhuanlan.zhihu.com/p/441028705（仅参考本地库管理部分，远程GitHub库管理参考下述步骤）

# 安装git安装包之后，执行如下命令生成GitHub密钥
参考：https://docs.github.com/cn/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

```bash
HP@DESKTOP-1RIVFM3 MINGW64 /d/PythonCodeLib (master)
$ ssh-keygen -t ed25519 -C "tongqin@outlook.com"
Generating public/private ed25519 key pair.
Enter file in which to save the key (/c/Users/HP/.ssh/id_ed25519):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /c/Users/HP/.ssh/id_ed25519
Your public key has been saved in /c/Users/HP/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:fbLh1+BJptR4C4pZx7GgPxHJkyOSJ2hUNV9eYrWwIvY tongqin@outlook.com
The key's randomart image is:
+--[ED25519 256]--+
|  ....o   =.o    |
| . . . + * = .   |
|  o + = @ + .    |
| .   = = O =     |
|      . E @ B    |
|       = * % =   |
|      o + + = .  |
|         . .     |
|                 |
+----[SHA256]-----+
```

# 登录GitHub将上述密钥灌入后，再执行下述代码，测试连通性
密钥灌注参考：https://docs.github.com/cn/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account

连通测试参考：https://docs.github.com/cn/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection
HP@DESKTOP-1RIVFM3 MINGW64 /d/PythonCodeLib (master)

```bash
$ ssh -T git@github.com
Hi tongqin2002! You've successfully authenticated, but GitHub does not provide shell access.
```

# 查看当前配置有哪些远程仓库（当前为空）

```bash
HP@DESKTOP-1RIVFM3 MINGW64 /d/PythonCodeLib (master)
$ git remote -v
```

# 登录GitHub新建" New repository "，创建远程仓库" sample "

# 远程仓库新建成功之后，新建本地仓库（按提示执行如下命令）

## 创建文件

```bash
HP@DESKTOP-1RIVFM3 MINGW64 /d/PythonCodeLib (master)
$ echo "# sample" >> README.md
```

## 初始化本地仓库

```bash
HP@DESKTOP-1RIVFM3 MINGW64 /d/PythonCodeLib (master)
$ git init
Reinitialized existing Git repository in D:/PythonCodeLib/.git/
```

## 添加文件至本地仓库

```bash
HP@DESKTOP-1RIVFM3 MINGW64 /d/PythonCodeLib (master)
$ git add README.md
warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it
```

## 查看本地仓库状态

```bash
HP@DESKTOP-1RIVFM3 MINGW64 /d/PythonCodeLib (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   README.md
```

## 提交文件至本地仓库并备注信息

```bash
HP@DESKTOP-1RIVFM3 MINGW64 /d/PythonCodeLib (master)
$ git commit -m "commt README.md"
[master 3e7bc30] commt README.md
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
```

## 查看当前所在分支

```bash
HP@DESKTOP-1RIVFM3 MINGW64 /d/PythonCodeLib (master)
$ git branch
  dev
* master
```

# 添加GitHub远程版本库（别名origin）

```bash
HP@DESKTOP-1RIVFM3 MINGW64 /d/PythonCodeLib (master)
$ git remote add origin https://github.com/tongqin2002/sample.git
```

# 查看当前配置远程仓库的具体信息

```bash
HP@DESKTOP-1RIVFM3 MINGW64 /d/PythonCodeLib (master)
$ git remote -v
origin  https://github.com/tongqin2002/sample.git (fetch)
origin  https://github.com/tongqin2002/sample.git (push)
```

# 提交本地库到远程Github仓库

```bash
HP@DESKTOP-1RIVFM3 MINGW64 /d/PythonCodeLib (master)
$ git push -u origin master
Enumerating objects: 4841, done.
Counting objects: 100% (4841/4841), done.
Delta compression using up to 12 threads
Compressing objects: 100% (4791/4791), done.
Writing objects: 100% (4841/4841), 35.88 MiB | 1.85 MiB/s, done.
Total 4841 (delta 383), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (383/383), done.
To https://github.com/tongqin2002/sample.git
 * [new branch]      master -> master
branch 'master' set up to track 'origin/master'.
```
---------------------

# Gitee环境类似配置密钥（可以与GitHub公用pub密钥，灌入gitee网站）

# 添加Gitee远程版本库（别名gitee_origin）
```bash
tongq@PSBCTQ MINGW64 /d/PythonCodeLib (master)
$ git remote add gitee_origin https://gitee.com/tongqin2002/samples.git
```
# 测试远程仓库连通性

```bash
tongq@PSBCTQ MINGW64 /d/PythonCodeLib (master)
$ ssh -T git@gitee.com
The authenticity of host 'gitee.com (212.64.63.215)' can't be established.
ED25519 key fingerprint is SHA256:+ULzij2u99B9eWYFTw1Q4ErYG/aepHLbu96PAUCoV88.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'gitee.com' (ED25519) to the list of known hosts.
git@gitee.com: Permission denied (publickey).
```

# 查看当前配置远程仓库的具体信息

```bash
tongq@PSBCTQ MINGW64 /d/PythonCodeLib (master)
$ git remote -v
gitee_origin    https://gitee.com/tongqin2002/samples.git (fetch)
gitee_origin    https://gitee.com/tongqin2002/samples.git (push)
origin  https://github.com/tongqin2002/sample.git (fetch)
origin  https://github.com/tongqin2002/sample.git (push)
```

# 提交本地库到远程Gitee仓库

```bash 
tongq@PSBCTQ MINGW64 /d/PythonCodeLib (master)
$ git push gitee_origin master
Enumerating objects: 4838, done.
Counting objects: 100% (4838/4838), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4790/4790), done.
Writing objects: 100% (4838/4838), 35.88 MiB | 1.49 MiB/s, done.
Total 4838 (delta 383), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (383/383), done.
remote: Powered by GITEE.COM [GNK-6.4]
To https://gitee.com/tongqin2002/samples.git
 * [new branch]      master -> master
```

---------------------

# 克隆git库（GitHub与gitee语法相同）

```bash
tongq@PSBCTQ MINGW64 /d/PythonCodeLib (master|MERGING)
$ git clone https://gitee.com/tongqin2002/samples sample_gitee

tongq@PSBCTQ MINGW64 /d/PythonCodeLib (master|MERGING)
$ cd sample_gitee/

tongq@PSBCTQ MINGW64 /d/PythonCodeLib/sample_gitee (master)
$ git remote -v
origin  https://gitee.com/tongqin2002/samples (fetch)
origin  https://gitee.com/tongqin2002/samples (push)

tongq@PSBCTQ MINGW64 /d/PythonCodeLib/sample_gitee (master)
$ git add .

tongq@PSBCTQ MINGW64 /d/PythonCodeLib/sample_gitee (master)
$ git commit -m "首次提交gitee库"

tongq@PSBCTQ MINGW64 /d/PythonCodeLib/sample_gitee (master)
$ git push -u origin master
```
---------------------

# 其他相关命令

```bash
git remote rm name  # 删除远程仓库
git remote rename old_name new_name  # 修改仓库名
git rm <file> #将文件从暂存区和工作区中删除
git pull origin master:brantest #将远程主机 origin 的 master 分支拉取过来，与本地的 brantest 分支合并
git pull origin master #如果远程分支是与当前分支合并，则冒号后面的部分可以省略
git push <远程主机名> <本地分支名>:<远程分支名> #将本地的分支版本上传到远程并合并
git push <远程主机名> <本地分支名> #如果本地分支名与远程分支名相同，则可以省略冒号：
```
