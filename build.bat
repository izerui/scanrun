rmdir /s /q build
:: https://pyinstaller.org/en/stable/usage.html
:: .\venv\Scripts\pyinstaller -n scanrun --windowed main.py
.\venv\Scripts\pyinstaller scanrun.spec