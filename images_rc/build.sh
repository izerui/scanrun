#!/bin/bash
echo '开始编译资源文件...'
pyside6-rcc images.qrc -o images_rc.py
echo '资源文件编译完成!'