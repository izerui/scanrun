#!/bin/bash
echo '开始编译ui文件...'
pyside6-uic login.ui -o ui_login.py
pyside6-uic home.ui -o ui_home.py
echo 'ui文件编译完成!'