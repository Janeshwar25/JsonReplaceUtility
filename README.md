SELECT
    medicalPlanCode AS External_ID,
    medicalPlanID   AS Medical_Plan_ID
FROM rso_01.rxplanxref
WHERE medicalPlanCode IN (
    'NexOAPoi10024B',
    'HE3500i10027',
    'SelNPOMAX5000i10027',
    'E040100i100LX24B',
    'CnP1000i8021B',
    'HP6000i10027CP',
    'PROP1000i8021B'
)
ORDER BY medicalPlanCode;
