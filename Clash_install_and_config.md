# Download Clash
URL:https://github.com/Dreamacro/clash/releases

# Install Clash
```bash
# 打开终端进入下载的文件夹 
cd /home/username/下载
# 解压
gunzip -d clash-linux-amd64-v1.7.1.gz
# 改名 
mv clash-linux-amd64-v1.7.1 clash
# 创建文件夹(一般将应用安装到opt目录) 
mkdir /opt/clash
# 移动解压后的clash文件到/opt/clash文件夹 
mv clash /opt/clash
```

# 配置clash
```bash
# 下载clash配置文件config.yaml 在代理商那里复制订阅链接，替代 [订阅链接]
wget -O config.yaml [订阅链接]
# 下载Country.mmdb 
wget -O Country.mmdb https://www.sub-speeder.com/client-download/Country.mmdb
```
> 注意：
如果提示yaml文件格式错误，则需要用工具转换成Clash类型的地址，flyjiang.cn/，先生成订阅链接，再通过订阅链接生成短链。这个短链就是Clash的订阅地址，短链可以直接打开，yaml是很整洁的格式，空的和乱码都是错的

# 配置操作系统网络代理
UOS路径：控制中心 -> 网络 -> 系统代理 -> 手动（标签页）

HTTP 和 HTTPS 代理为 127.0.0.1:7890

Socks 代理为 127.0.0.1:7891

配置完毕之后保存，启动代理

# 启动clash
```bash
# 授权可执行权限 
chmod +x clash 
# 可启动 Clash，同时启动 HTTP 代理和 Socks5 代理
./clash -d . 
```
至此就可以科学上网了

# 切换节点、测延迟（可选）

```bash
打开配置文件config.yaml ，另起一行，设置密码：
# secret: '123456'
```

访问 http://clash.razord.top/ 可以进行切换节点、测延迟等操作。