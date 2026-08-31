Invoke-RestMethod -Uri "http://127.0.0.1:5000/run-group-validator" -Method POST -ContentType "application/json" -Body '{"group_ids":["3118035"]}'




python "%~dp0replace_json.py" %*
set "EXITCODE=%ERRORLEVEL%"

copy /Y "%~dp0updated.json" "C:\Users\jchowdha\ACCELQAgent_1\AgentInstances\agent\user_data\updated.json"

echo.
if "%EXITCODE%"=="0" (
    echo SUCCESS - Utility completed.
) else (
    echo FAILED - Exit code %EXITCODE%.
)
echo.

endlocal & exit /b %EXITCODE%









SELECT DISTINCT
    bp.planID AS Medical_Plan_ID,
    bp.planVersion,
    bns.networkScheduleID,
    nsh.networkScheduleDesc,
    bns.serviceAreaID,
    bns.beneNetworkSchedEffDate,
    bns.beneNetworkSchedExpDate
FROM rso_01.benefitplan bp
JOIN rso_01.benenetworksched bns
    ON bns.benefitPlanVersionID = bp.benefitPlanVersionID
LEFT JOIN rso_01.netscheduleheader nsh
    ON nsh.networkScheduleID = bns.networkScheduleID
WHERE bp.planID IN (
    'M010003574',
    'M010009228',
    'M010000273'
)
ORDER BY bp.planID, bp.planVersion, bns.beneNetworkSchedEffDate;








SELECT
    be.externalPlanID AS Medical_External_ID,
    bp.planID AS Medical_Plan_ID,
    bp.planName,
    bp.planVersion,
    bp.benPlanEffDate,
    bp.benPlanExpDate
FROM rso_01.beneexternalid be
JOIN rso_01.benefitplan bp
    ON bp.benefitPlanVersionID = be.benefitPlanVersionID
WHERE be.externalPlanID = 'NexOAPoi10024B';


SELECT
    zip,
    city,
    countyName,
    countyFIPS,
    state,
    stateName
FROM rso_01.zipcode
WHERE state = 'CA'
ORDER BY zip;



SELECT DISTINCT
    medicalPlanID AS Medical_Plan_ID,
    rxPlanID      AS RX_Plan_ID,
    rxPlanCode    AS RX_Plan_Code,
    rxPlanExtID   AS RX_External_ID
FROM rso_01.rxplanxref
WHERE medicalPlanID = 'M010003574';
