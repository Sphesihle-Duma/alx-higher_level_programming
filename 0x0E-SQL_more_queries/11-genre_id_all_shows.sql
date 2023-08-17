-- Lists all shows from the imported database
SELECT shows.title, genre.genre_id
FROM tv_shows As shows
LEFT JOIN tv_show_genres As genre
ON shows.id = genre.genre_id
ORDER BY shows.title ASC, genre.genre_id ASC
