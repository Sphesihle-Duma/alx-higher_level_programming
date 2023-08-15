-- Lists the number of records with the same score in the table
-- Displays score
-- The number of records for this score
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC
