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
