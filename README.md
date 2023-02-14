# 扫码装箱程序

# 脚本
* 生成`requirements.txt`: `pip freeze > requirements.txt`
* 通过`requirements.txt`安装依赖: `pip install -r requirements.txt`

# 安装依赖
* PySide6: `pip install PySide6 -i http://pypi.douban.com/simple --trusted-host pypi.douban.com`
* pyinstaller: `pip install pyinstaller -i http://pypi.douban.com/simple --trusted-host pypi.douban.com`


# 配置第三方工具
* pyside6-designer

# 打包
* 生成exe: `pyinstaller -D -w -i Icon.ico main.py`
* 生成app: `pyinstaller -D -w -i Icon.icns main.py`
* 图标: https://www.jianshu.com/p/e74047f7cc91