import sys

from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "excludes": ["tkinter", "unittest"],
    "zip_include_packages": ["encodings", "PySide6", "shiboken6", "httpx", "APScheduler", "playsound"],
}

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="scanrun",
    version="0.1",
    description="My Scanrun Application!",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)],
)
