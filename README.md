SELECT
    bp.planID,
    bp.planName,
    bp.allStateInd,
    be.externalPlanID,
    be.beneExternalID,
    be.externalIDEffDate,
    be.externalIDExpDate
FROM rso_01.benefitplan bp
LEFT JOIN rso_01.beneexternalid be
    ON be.benefitPlanVersionID = bp.benefitPlanVersionID
WHERE bp.planID = 'MNS0100347';
