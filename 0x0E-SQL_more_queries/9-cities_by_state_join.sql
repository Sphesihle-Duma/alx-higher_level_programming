-- Lists all cities contained in the database
-- Displays cities.id - cities.name - states.name
-- Result must be sorted by cities.id
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
