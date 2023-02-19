#!/bin/bash
pwd
echo '开始编译资源文件...'
./venv/bin/pyside6-rcc images.qrc -o images_rc.py
echo '资源文件编译完成!'
echo '开始编译ui文件...'
./venv/bin/pyside6-uic ui/login.ui -o ui/ui_login.py
./venv/bin/pyside6-uic ui/home.ui -o ui/ui_home.py
./venv/bin/pyside6-uic ui/task_form.ui -o ui/ui_task_form.py
echo 'ui文件编译完成!'