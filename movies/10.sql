select name from people p join directors d on d.person_id = p.id join movies m on m.id=d.movie_id join ratings r on m.id = r.movie_id where rating >= 9.0;
