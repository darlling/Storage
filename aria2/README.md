**<https://github.com/P3TERX/aria2.conf>**  

---
## Win10开机自启
### 用户自启文件夹
**`win+r`**后输入**`shell:startup`**，将 vbs 快捷方式放入其中即可

### 系统自启文件夹
**`win+r`**后输入**`%programdata%\Microsoft\Windows\Start Menu\Programs\Startup`**，将 vbs 快捷方式放入其中即可

---
**“用户启动文件夹”和“系统启动文件夹”的区别**

两者起到的功能不一样。举例说明：如果系统有admin和guest两个系统用户，admin使用方法一（用户启动文件夹）添加开机启动项，那么只有使用admin登录系统时，开机启动项才会起作用，guest用户登录系统不会自动启动；而使用方法二（系统启动文件夹）设置的开机启动项，在admin和guest登录系统时都会启动。
