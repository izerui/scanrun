#!/bin/bash
rm -rf build dist
#python setup.py bdist_dmg
pyinstaller -D -w -i resources/Icon.icns main.py