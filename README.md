Invoke-RestMethod -Uri "http://127.0.0.1:5000/run-group-validator" -Method POST -ContentType "application/json" -Body "{}" | ConvertTo-Json -Depth 10
