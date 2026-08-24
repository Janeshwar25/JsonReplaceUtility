
python -c "import mysql.connector; c=mysql.connector.connect(host='172.19.96.26', database='errq01', user='YOUR_USER', password='YOUR_PASSWORD', port=3306); print('DB CONNECTED:', c.is_connected()); c.close()"









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
