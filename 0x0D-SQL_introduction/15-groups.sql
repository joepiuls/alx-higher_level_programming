-- List the number of records with the same scorein second_table
SELECT score, count(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
