@echo off
::установка библиотек если такие появились
pip install -r requirements.txt
::python3 --version
echo Activating virtual environment...
call venv\Scripts\activate
echo Starting the bot...
python main.py
pause
