rmdir /s /q build
:: python setup.py build
:: python setup.py build_exe
.\venv\Scripts\pyinstaller --onefile --windowed main.py