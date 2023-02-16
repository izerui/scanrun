#!/bin/bash
echo '开始编译资源文件...'
pyside6-rcc images_rc/images.qrc -o images_rc/images_rc.py
echo '资源文件编译完成!'
echo '开始编译ui文件...'
pyside6-uic ui/login.ui -o ui/ui_login.py
pyside6-uic ui/home.ui -o ui/ui_home.py
echo 'ui文件编译完成!'