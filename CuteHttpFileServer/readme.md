### 将 CHFS 添加到目录右键菜单项
---
1. 注册表路径:

    * `[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Directory\background\shell\CHFS]`
    * `[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Directory\background\shell\CHFS\command]`

2. 先导出相同路径下的 `VSCode` 注册表文件，将文件中的路径名修改为上述路径再重新导入注册表
    即可得到 `CHFS` 注册表项（当然是 `VSCode` 注册表项的副本）

3. 直接在注册表编辑器中右键修改值即可，默认键参考值如下:

    * `使用 CHFS 共享当前目录`
    * `"C:\Environment\CuteHttpFileServer\chfs.exe" --path="%V" --file="C:\Environment\CuteHttpFileServer\chfs.ini"`

    修改文件路径即可
