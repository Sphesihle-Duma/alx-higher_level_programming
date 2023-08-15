-- Lists all record of the second table
-- Does not display rows without a name value
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC
