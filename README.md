cd /Users/janeshwarchowdhary/Desktop/f
python3 -m uvicorn app.routes:app --host 127.0.0.1 --port 8000 --reload

python -m streamlit run app/app.py
