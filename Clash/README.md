## Clash For Windows
> Time：2020/11/06 12:17

Place `config.yaml` in `$HOME/.config/clash/config.yaml`

~~`proxy-providers`里的类型为`file`，故需准备好代理文件，放置路径参考配置里的路径即可~~

**`proxy-providers`使用`http`类型，`url`里使用 [pastebin](https://pastebin.com) 托管代码片段即可（`unlisted`）**

**`gist.github.com`更好，可惜国内无法直连**

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
> Time：2020/11/06 23:26

~~在`config.yaml`中添加入`proxies`字段并将代理节点全部按规范加入，配套修改`proxy-groups`中的相应字段即可~~

~~据试验，CFA 2.1.6 版本尚未有效支持`proxy-providers`下的`path`参数（在`file`类型下），软件无法正确读取外部存储路径，功能待开发者完善~~
