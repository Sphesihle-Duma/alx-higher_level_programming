-- Lists all genres by their rating from the database
SELECT g.name, SUM(sr.rate) AS rating
FROM tv_shows AS s
INNER JOIN tv_show_ratings AS sr
ON s.id = sr.show_id
INNER JOIN tv_show_genres AS tg
ON s.id = tg.show_id
INNER JOIN tv_genres AS g
ON g.id = tg.genre_id
GROUP BY g.name
ORDER BY rating DESC;
