SELECT
    rxPlanXrefID,
    medicalPlanID,
    medicalPlanCode,
    rxPlanID,
    rxPlanCode,
    rxPlanExtID,
    effectiveDate,
    expirationDate
FROM rso_01.rxplanxref
WHERE medicalPlanCode LIKE '%456119%';
