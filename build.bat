rmdir /s /q build dist
:: https://pyinstaller.org/en/stable/usage.html
.\venv\Scripts\pyinstaller -n scanrun --add-data="media;media" --windowed -i resources\Icon.ico main.py