Get-ChildItem "C:\Users\jchowdha\Desktop\Accelq_Janesh\ACCELQAgent" -Recurse -File -Filter "*activemq*.jar" -ErrorAction SilentlyContinue | Select-Object FullName
