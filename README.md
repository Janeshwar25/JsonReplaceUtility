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
