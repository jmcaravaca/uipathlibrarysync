cd C:\PyApi\uipython
call .venv\Scripts\activate.bat
python -m uvicorn main:app --reload --host 0.0.0.0
