from cx_Freeze import setup, Executable

build_exe_options = {'packages': [], 'excludes': []}

setup(name='scanrun',
      version='1.0.0',
      description='scanrun',
      options={'build_exe': build_exe_options},
      executables=[Executable('main.py')])
