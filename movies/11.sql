SELECT title FROM movies m JOIN stars s ON m.id = s.movie_id JOIN people p ON p.id= s.person_id JOIN ratings r ON r.movie_id=m.id where name ="Chadwick Boseman" ORDER BY rating DESC LIMIT 5;
