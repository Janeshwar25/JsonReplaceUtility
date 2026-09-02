SELECT
    zip,
    city,
    countyName,
    countyFIPS,
    state,
    stateName
FROM rso_01.zipcode
WHERE state = 'CA'
ORDER BY zip;






SET SESSION group_concat_max_len = 10000000;

SELECT @@group_concat_max_len;

SELECT GROUP_CONCAT(
    CONCAT(
        'SELECT ''', TABLE_NAME, ''' AS sourceTable, ',
        '''', COLUMN_NAME, ''' AS sourceColumn, ',
        'CAST(`', COLUMN_NAME, '` AS CHAR) AS value ',
        'FROM `rso_01`.`', TABLE_NAME, '` ',
        'WHERE CAST(`', COLUMN_NAME, '` AS CHAR) LIKE ''%MNS0301833%'''
    )
    SEPARATOR ' UNION ALL '
)
INTO @sql
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = 'rso_01'
  AND COLUMN_NAME IN ('planID', 'externalPlanID');


SELECT LENGTH(@sql) AS sql_length;


PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
  




SELECT TABLE_NAME, COLUMN_NAME
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = 'rso_01'
  AND COLUMN_NAME IN ('planID', 'externalPlanID')
ORDER BY COLUMN_NAME, TABLE_NAME;




SELECT @@group_concat_max_len AS max_len,
       LENGTH(@sql) AS sql_length;





SELECT GROUP_CONCAT(
    CONCAT(
        'SELECT ''', TABLE_NAME, ''' AS sourceTable, ',
        '''', COLUMN_NAME, ''' AS sourceColumn, ',
        'CAST(`', COLUMN_NAME, '` AS CHAR) AS value ',
        'FROM `rso_01`.`', TABLE_NAME, '` ',
        'WHERE CAST(`', COLUMN_NAME, '` AS CHAR) LIKE ''%MNS0301833%'''
    )
    SEPARATOR ' UNION ALL '
)
INTO @sql
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = 'rso_01'
  AND DATA_TYPE IN (
      'char','varchar','text',
      'tinytext','mediumtext','longtext'
  );








SET SESSION group_concat_max_len = 1000000;


SELECT GROUP_CONCAT(
    CONCAT(
        'SELECT ''', TABLE_NAME, ''' AS sourceTable, ',
        '''', COLUMN_NAME, ''' AS sourceColumn, ',
        'CAST(`', COLUMN_NAME, '` AS CHAR) AS value ',
        'FROM `rso_01`.`', TABLE_NAME, '` ',
        'WHERE CAST(`', COLUMN_NAME, '` AS CHAR) LIKE ''%MNS0301833%'''
    )
    SEPARATOR ' UNION ALL '
)
INTO @sql
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = 'rso_01'
  AND DATA_TYPE IN (
      'char',
      'varchar',
      'text',
      'tinytext',
      'mediumtext',
      'longtext'
  );

PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

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
