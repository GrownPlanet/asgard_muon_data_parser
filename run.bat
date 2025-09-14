@echo off

IF NOT EXIST .venv (
    python -m venv .venv
    call .venv\Scripts\activate.bat
    pip install numpy matplotlib
) ELSE (
    call .venv\Scripts\activate.bat
)

start python organize_100m.py
start python organize_100m_s.py
