Get-ChildItem "C:\Users\jchowdha\Desktop\Accelq_Janesh\ACCELQAgent" -Recurse -File -ErrorAction SilentlyContinue | Where-Object { $_.Name -match "activemq" } | Select-Object -ExpandProperty FullName
