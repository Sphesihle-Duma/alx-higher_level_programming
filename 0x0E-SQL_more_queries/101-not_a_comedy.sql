-- Lists all shows that are not of genre Comedy
SELECT s.title
FROM tv_shows AS s
LEFT JOIN(
	SELECT * 
	FROM tv_genres AS g
	JOIN tv_show_genres AS tg
	ON g.id = tg.genre_id
	WHERE g.name = "Comedy"
) AS vt
ON s.id = vt.show_id
WHERE vt.genre_id IS NULL
ORDER BY s.title;
