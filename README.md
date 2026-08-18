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
