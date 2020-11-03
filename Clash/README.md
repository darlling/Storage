## Clash For Windows
> Time：2020/11/03 12:17

place `config.yaml` in `$HOME/.config/clash/config.yaml`

`proxy-providers`里的类型为`file`，故需准备好代理文件，放置路径参考配置里的路径即可  
此示例的代理文件为`DuangCloud.yaml`，路径为`clash`用户配置根路径`./`  
代理文件具体格式参考：[https://lancellc.gitbook.io/clash/clash-config-file/proxy-provider](https://lancellc.gitbook.io/clash/clash-config-file/proxy-provider)

```yaml
proxies:
- name: "ss1"
  type: ss
  server: server
  port: 443
  cipher: chacha20-ietf-poly1305
  password: "password"
  # udp: true

# old obfs configuration format remove after prerelease
- name: "ss2"
  type: ss
  server: server
  port: 443
  cipher: chacha20-ietf-poly1305
  password: "password"
  plugin: obfs
  plugin-opts:
    mode: tls # or http
    # host: bing.com

- name: "ss3"
  type: ss
  server: server
  port: 443
  cipher: chacha20-ietf-poly1305
  password: "password"
  plugin: v2ray-plugin
  plugin-opts:
    mode: websocket # no QUIC now
    # tls: true # wss
    # skip-cert-verify: true
    # host: bing.com
    # path: "/"
    # mux: true
    # headers:
    #   custom: value
```
若将`proxy-providers`里的类型改为`http`，则须注意`url`参数值所代表的`yaml`配置文件须符合上述代理文件格式

除此之外，无其他需要注意的额外事项，一切参见示例即可

## Clash For Android
> Time：2020/11/03 12:17

尚未测试 android 使用情况，还存在以下问题待实验：
- `config.yaml`中的各种配置文件路径问题，如`./RuleSet/...`
- `proxy-providers`中的订阅链接问题
    - 若订阅链接提供的是符合上述条件的`yaml`配置文件，则直接置`type`为`http`，`url`填入订阅链接即可
    - 若订阅链接提供的是不符合上述条件的复杂`yaml`配置文件，则我在`Clash For Windows`上是将配置文件下载到本地后手动编辑使其符合条件，即`DuangCloud.yaml`，故使用的`type`为`file`。`Android`如何实现尚未可知

### 设想解决方案
在`config.yaml`中添加入`proxies`字段并将代理节点全部加入，配套修改`proxy-groups`中的相应字段即可  
至于`RuleSet`规则集文件路径问题，尚未可知是否能自动生成在手机内置存储中