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
WHERE medicalPlanCode = 'DBS_Flex Focus P2000i8027_456119'
  AND rxPlanCode = 'RX7 ADVB';
