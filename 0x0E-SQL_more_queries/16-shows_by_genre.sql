-- Lists all shows and all genres linked to that show
SELECT s.title, tg.name
FROM tv_shows AS s
LEFT JOIN tv_show_genres g
ON s.id = g.show_id
LEFT JOIN tv_genres AS tg
ON g.genre_id = tg.id
ORDER BY s.title, tg.name
