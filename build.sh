#!/bin/bash
rm -rf build dist
# https://pyinstaller.org/en/stable/usage.html
pyinstaller -n scanrun -w -i resources/Icon.icns --add-data="media:./media" main.py