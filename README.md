
SELECT
    TABLE_NAME,
    COLUMN_NAME
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = 'rso_01'
  AND (
       COLUMN_NAME LIKE '%contract%'
       OR COLUMN_NAME LIKE '%memGroup%'
       OR COLUMN_NAME LIKE '%plan%'
  )
ORDER BY TABLE_NAME, COLUMN_NAME;



TABLE_NAME
benefitplan
benefitplansearchview
capadj
caprunattribset
caprunmem
caprunmemdetailcapview
claimcapdeduct
memacctchangelog
memacctchangelogfp





SELECT TABLE_NAME
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = 'rso_01'
  AND COLUMN_NAME IN ('planID', 'memGroupID')
GROUP BY TABLE_NAME
HAVING COUNT(DISTINCT COLUMN_NAME) = 2
ORDER BY TABLE_NAME;
