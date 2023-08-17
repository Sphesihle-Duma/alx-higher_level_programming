-- Lists all shows from the imported database
SELECT s.title, g.genre_id
FROM tv_shows As s
LEFT JOIN tv_show_genres As g
ON s.id = g.genre_id
ORDER BY s.title, g.genre_id
