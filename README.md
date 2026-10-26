Get-ChildItem "C:\Users\jchowdha\Desktop" -Recurse -File -Filter "*activemq*.jar" -ErrorAction SilentlyContinue | Select-Object -ExpandProperty FullName
