Get-ChildItem "C:\Users\jchowdha\Desktop\Accelq_Janesh\ACCELQAgent\AgentInstances" -Filter "*plactivemq-all-5.17.0.jar" -Recurse -ErrorAction SilentlyContinue | Select-Object -ExpandProperty FullName
