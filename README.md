SELECT DISTINCT
    medicalPlanID AS Medical_Plan_ID,
    rxPlanID      AS RX_Plan_ID,
    rxPlanCode    AS RX_Plan_Code,
    rxPlanExtID   AS RX_External_ID
FROM rso_01.rxplanxref
WHERE medicalPlanID = 'M010003574';
