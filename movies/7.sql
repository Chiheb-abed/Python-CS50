SELECT m.title , r.rating FROM movies m JOIN ratings r ON r.movie_id=m.id where year = 2010 ORDER BY (rating) DESC,title ASC;
