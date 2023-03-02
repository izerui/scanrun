# 扫码装箱程序

# 初始化
1. 初始化 python 虚拟环境: `python -m venv venv`，并切换到当前环境。
2. 安装所有依赖项: `pip install -r requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com`
3. 运行： `python main.py` 


# 脚本
* 生成`requirements.txt`: `pip freeze > requirements.txt`
* 通过`requirements.txt`安装依赖: `pip install -r requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com`
* 执行各个目录中的`build.sh`文件来编译资源文件和ui文件

# 已安装依赖列表(不及时更新)
* PySide6: `pip install PySide6 -i http://pypi.douban.com/simple --trusted-host pypi.douban.com`
* httpx: `pip install httpx -i http://pypi.douban.com/simple --trusted-host pypi.douban.com`
* APScheduler: `pip install APScheduler -i http://pypi.douban.com/simple --trusted-host pypi.douban.com`
* simpleaudio: `pip install simpleaudio -i http://pypi.douban.com/simple --trusted-host pypi.douban.com`
* pyinstaller(打包选装): `pip install pyinstaller -i http://pypi.douban.com/simple --trusted-host pypi.douban.com`
* 如果使用mac希望发出声音: `pip install PyObjC -i http://pypi.douban.com/simple --trusted-host pypi.douban.com`

# 配置pycharm第三方工具,如果是vscode只需要安装插件: `Qt for Python`
* pyside6-designer:
  > * program: `$ProjectFileDir$/venv/bin/pyside6-designer`
  > * working directory: `$FileDir$`
* pyside6-uic:
  > * program: `$ProjectFileDir$/venv/bin/pyside6-uic`
  > * arguments: `$FileName$ -o ui_$FileNameWithoutExtension$.py`
  > * working directory: `$FileDir$`

# 打包 https://www.jianshu.com/p/e74047f7cc91
* Windows: 
  * 生成exe: `.\venv\Scripts\pyinstaller --onefile --windowed main.py`
  * 使用winrar打包: https://xinyuehtx.github.io/post/%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8winrar%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E5%AE%89%E8%A3%85%E5%8C%85.html
* Mac:
  > * pyinstaller: `pip install pyinstaller -i http://pypi.douban.com/simple --trusted-host pypi.douban.com`
  > * 全部拷贝到命令行回车执行，执行结束之后去tmp.iconset查看十张图片是否生成好
  ```
  mkdir tmp.iconset
  cd tmp.iconset
  sips -z 16 16     pic.png --out tmp.iconset/icon_16x16.png
  sips -z 32 32     pic.png --out tmp.iconset/icon_16x16@2x.png
  sips -z 32 32     pic.png --out tmp.iconset/icon_32x32.png
  sips -z 64 64     pic.png --out tmp.iconset/icon_32x32@2x.png
  sips -z 128 128   pic.png --out tmp.iconset/icon_128x128.png
  sips -z 256 256   pic.png --out tmp.iconset/icon_128x128@2x.png
  sips -z 256 256   pic.png --out tmp.iconset/icon_256x256.png
  sips -z 512 512   pic.png --out tmp.iconset/icon_256x256@2x.png
  sips -z 512 512   pic.png --out tmp.iconset/icon_512x512.png
  sips -z 1024 1024   pic.png --out tmp.iconset/icon_512x512@2x.png
  ```
  * 生成图表: `iconutil -c icns resources/tmp.iconset -o resources/Icon.icns`
  * 生成app: `pyinstaller -D -w -i resources/Icon.icns main.py`

# qt-designer 使用说明
* 资源浏览器管理qrc资源
* 动作编辑器管理toolbar等action
* 信号/槽其实是事件的发布订阅
* 选择控件提升为,则会修改ui的类定义，通过指定的类来创建对象，可以用来做组件化，避免所有ui和交互都在同一个ui文件、controller文件