Get-ChildItem "$env:USERPROFILE\Desktop\Accelq_Janesh" -Recurse -File -Filter "*activemq*.jar" -ErrorAction SilentlyContinue | Select-Object -ExpandProperty FullName
