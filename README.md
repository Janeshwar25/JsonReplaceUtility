SELECT
    medicalPlanCode AS External_ID,
    medicalPlanID   AS Medical_Plan_ID
FROM rso_01.rxplanxref
WHERE medicalPlanCode = 'NexOAPoi10024B';
