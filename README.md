SELECT
    rxPlanXrefID,
    medicalPlanID,
    medicalPlanCode,
    rxPlanID,
    rxPlanCode,
    rxPlanExtID
FROM rso_01.rxplanxref
WHERE medicalPlanCode LIKE '%P2000%'
   OR medicalPlanCode LIKE '%8027%'
   OR medicalPlanCode LIKE '%456119%'
   OR rxPlanCode LIKE '%ADVB%';
