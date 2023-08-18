-- Lists all genres that are not linked to the show
SELECT g.name
FROM tv_genres AS g
LEFT JOIN(
	SELECT * 
	FROM tv_shows AS s
	JOIN tv_show_genres AS tg
	ON s.id = tg.show_id
	WHERE s.title = "Dexter"
) AS vt
ON g.id = vt.genre_id
WHERE vt.title IS NULL
ORDER BY g.name;
