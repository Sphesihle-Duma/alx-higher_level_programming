-- Lists all shows by their ratings from database
-- group by show title
SELECT s.title, SUM(sr.rate) AS rating
FROM tv_shows AS s
INNER JOIN tv_show_ratings AS sr
ON s.id = sr.show_id
GROUP BY s.title
ORDER BY rating DESC;
