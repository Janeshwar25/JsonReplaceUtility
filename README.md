SELECT TABLE_NAME, COLUMN_NAME
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = 'rso_01'
  AND COLUMN_NAME IN ('planID', 'memGroupID')
ORDER BY TABLE_NAME, COLUMN_NAME;


SELECT DISTINCT
    memGroupID,
    planID
FROM rso_01.caprunnemetailcapview
WHERE planID = 'MNS0301833';



SELECT DISTINCT
    memGroupID,
    planID
FROM rso_01.caprunnem
WHERE planID = 'MNS0301833';

SELECT DISTINCT
    memGroupID,
    planID
FROM rso_01.capadj
WHERE planID = 'MNS0301833';


SELECT DISTINCT
    memGroupID,
    planID
FROM rso_01.benefitplansearchview
WHERE planID = 'MNS0301833';



SELECT TABLE_NAME
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = 'rso_01'
  AND COLUMN_NAME IN ('planID', 'memGroupID')
GROUP BY TABLE_NAME
HAVING COUNT(DISTINCT COLUMN_NAME) = 2
ORDER BY TABLE_NAME;



SELECT TABLE_NAME, COLUMN_NAME
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = 'rso_01'
  AND (
      COLUMN_NAME LIKE '%plan%'
      OR COLUMN_NAME LIKE '%memGroup%'
  )
ORDER BY TABLE_NAME, COLUMN_NAME;


SELECT TABLE_NAME, COLUMN_NAME
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = 'rso_01'
  AND COLUMN_NAME IN ('planID', 'memGroupID')
ORDER BY TABLE_NAME, COLUMN_NAME;



SELECT DISTINCT memGroupID, planID
FROM membergroup.memgroupcontractplanoption
WHERE planID LIKE '%MNS0301833%';




SELECT DISTINCT
    m.memGroupID,
    m.memGroupName,
    m.createDateTime,
    m.createUserID
FROM membergroup.memgroupcontractplanoption p
JOIN membergroup.memgroup m
    ON m.memGroupID = p.memGroupID
WHERE p.planID = 'MNS0301833'
ORDER BY m.memGroupID;



SELECT
    memGroupID,
    memGroupName,
    createDateTime,
    createUserID
FROM membergroup.memgroup
WHERE memGroupName LIKE '%INSTALLONLY%'
ORDER BY createDateTime DESC;





SELECT *
FROM membergroup.memgroup
WHERE memGroupName LIKE '%INSTALLONLY%'
  AND DATE(createDateTime) = '2026-07-01';


SELECT COLUMN_NAME
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = 'membergroup'
  AND TABLE_NAME = 'memgroup'
  AND (
      COLUMN_NAME LIKE '%date%'
      OR COLUMN_NAME LIKE '%created%'
      OR COLUMN_NAME LIKE '%create%'
  );




SELECT *
FROM membergroup.memgroup
WHERE memGroupName LIKE '%INSTALLONLY%'
  AND MONTH(creationDate) = 7
  AND DAY(creationDate) = 1;



SELECT *
FROM membergroup.memgroup
WHERE memGroupName LIKE '%INSTALLONLY%'
  AND DATE(creationDate) = '2026-07-01';



SELECT *
FROM membergroup.memgroup
WHERE memGroupName LIKE '%INSTALLONLY%';


SELECT DISTINCT
    memGroupID,
    planID
FROM membergroup.memgroupcontractplanoptv2view
WHERE planID LIKE '%MNS0301833%';



SELECT DISTINCT
    memGroupID,
    planID
FROM membergroup.memgroupcontractoptextractview
WHERE planID = 'MNS0301833';



SELECT DISTINCT
    memGroupID,
    planID
FROM membergroup.memgroupcontractplanoption
WHERE planID = 'MNS0301833';





SELECT TABLE_NAME
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = 'membergroup'
  AND COLUMN_NAME IN ('planID', 'memGroupID')
GROUP BY TABLE_NAME
HAVING COUNT(DISTINCT COLUMN_NAME) = 2
ORDER BY TABLE_NAME;





SELECT TABLE_NAME, COLUMN_NAME
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = 'membergroup'
  AND COLUMN_NAME IN ('planID', 'memGroupID')
ORDER BY TABLE_NAME;




SELECT TABLE_NAME, COLUMN_NAME
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = 'membergroup'
  AND (COLUMN_NAME LIKE '%plan%'
       OR COLUMN_NAME LIKE '%memGroup%')
ORDER BY TABLE_NAME, COLUMN_NAME;





SELECT DISTINCT planID
FROM membergroup.memgroupcontractplanoption
WHERE planID LIKE '%MNS0301833%';




DESCRIBE membergroup.memgroupcontractplanoption;


SELECT planID, planName, allStateInd
FROM rso_01.benefitplan
WHERE planID = 'MNS0301833';





SELECT DISTINCT planID
FROM membergroup.memgroupcontractplanoption
WHERE planID = 'MNS0301833';



SELECT DISTINCT
    m.memGroupID,
    m.memGroupName
FROM membergroup.memgroupcontractplanoption p
JOIN membergroup.memgroup m
    ON m.memGroupID = p.memGroupID
WHERE p.planID = 'MNS0301833'
ORDER BY m.memGroupID;






SELECT memGroupID, memGroupName, changeDateTime, changeUserID
FROM membergroup.memgroup
WHERE memGroupID = 123456;





Test-NetConnection 172.19.96.239 -Port 3306



python -c "import mysql.connector; c=mysql.connector.connect(host='172.19.96.239',port=3306,database='tent01',user='YOUR_USER',password='YOUR_PASSWORD'); print('DB CONNECTED'); c.close()"





Get-ChildItem "C:\Users\paggarwa" -Recurse -Filter "AccelQ_Input_Output_File.xlsx" -ErrorAction SilentlyContinue | Select-Object FullName






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
