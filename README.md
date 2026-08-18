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
