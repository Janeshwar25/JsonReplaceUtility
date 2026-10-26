Get-ChildItem "C:\Users\jchowdha\Desktop\Accelq_Janesh\ACCELQAgent" -Recurse -File -Filter "*plactivemq*.jar" -ErrorAction SilentlyContinue | Select-Object -ExpandProperty FullName
