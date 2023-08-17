-- Lists all shows from the imported database with no genre
SELECT  s.title, g.genre_id
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS g
ON s.id = g.genre_id
WHERE g.genre_id IS NULL;
