SELECT 'joinbeneexternalid' AS sourceTable,
       planID,
       benefitPlanVersionID,
       externalPlanID
FROM rso_01.joinbeneexternalid
WHERE externalPlanID = 'MNS0301833';

UNION ALL

SELECT 'benefitplanextractviewv4' AS sourceTable,
       planID,
       benefitPlanVersionID,
       externalPlanID
FROM rso_01.benefitplanextractviewv4
WHERE externalPlanID = 'MNS0301833';

UNION ALL

SELECT 'memgroupphmiputilplanextractvw' AS sourceTable,
       utilizationPlanID AS planID,
       NULL AS benefitPlanVersionID,
       externalPlanID
FROM rso_01.memgroupphmiputilplanextractvw
WHERE externalPlanID = 'MNS0301833';

UNION ALL

SELECT 'netcontractplan' AS sourceTable,
       planID,
       NULL AS benefitPlanVersionID,
       externalPlanID
FROM rso_01.netcontractplan
WHERE externalPlanID = 'MNS0301833';






SELECT DISTINCT
    p.memGroupID,
    mg.memGroupName,
    p.planID
FROM membergroup.memgroupcontractplanoption p
LEFT JOIN membergroup.memgroup mg
    ON mg.memGroupID = p.memGroupID
WHERE p.planID = 'MNS0301833'
ORDER BY p.memGroupID;




SELECT DISTINCT
    memGroupID,
    planID
FROM membergroup.memgroupcontractplanoption
WHERE planID = 'MNS0301833'
ORDER BY memGroupID;





SELECT *
FROM membergroup.memgroupcontractplanoption
WHERE planID = 'MNS0301833';





SELECT DISTINCT
    ncp.planID,
    ncmg.memGroupID,
    ncp.netContractHeaderID,
    ncp.netContractVersionID,
    ncmg.netContractVersionID
FROM rso_01.netcontractplan ncp
JOIN rso_01.netcontractmembergroup ncmg
    ON ncmg.netContractHeaderID = ncp.netContractHeaderID
WHERE ncp.planID = 'MNS0301833'
ORDER BY ncmg.memGroupID;




SELECT DISTINCT
    ncp.planID,
    ncmg.memGroupID,
    ncp.netContractHeaderID,
    ncp.netContractVersionID
FROM rso_01.netcontractplan ncp
JOIN rso_01.netcontractmembergroup ncmg
    ON ncmg.netContractHeaderID = ncp.netContractHeaderID
   AND ncmg.netContractVersionID = ncp.netContractVersionID
WHERE ncp.planID = 'MNS0301833'
ORDER BY ncmg.memGroupID;
