@echo off
SET var = %cd%
set PYTHONPATH = %var%
cd src/py
python main.py
pause