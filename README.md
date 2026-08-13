Invoke-RestMethod -Uri "http://127.0.0.1:5000/run-member-validator" -Method POST -ContentType "application/json" -Body "{}" | ConvertTo-Json -Depth 10





Get-ChildItem "C:\Users\jchowdha\Desktop\AccelQ_AI_Framework" -Recurse -File |
Where-Object { $_.Name -match "member_validation|\.xlsx$" } |
Select-Object FullName, LastWriteTime
