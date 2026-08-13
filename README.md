cd "C:\Users\jchowdha\Desktop\AccelQ_AI_Framework\scripts"
python member_validator.py


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


Get-ChildItem "C:\Users\jchowdha\Desktop\AccelQ_AI_Framework\reports" -Filter "*.xlsx" |
Sort-Object LastWriteTime -Descending |
Select-Object -First 10 FullName,LastWriteTime
