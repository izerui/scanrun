rmdir /s /q build dist
:: https://pyinstaller.org/en/stable/usage.html
.\venv\Scripts\pyinstaller -n scanrun --windowed -i resources\Icon.ico main.py