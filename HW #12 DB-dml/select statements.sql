SELECT album_name, release_year 
  FROM album
 WHERE release_year = 2018;

SELECT song_name, duration_sec
  FROM song
 WHERE duration_sec = (SELECT MAX(duration_sec) FROM song);

SELECT song_name
  FROM song
 WHERE duration_sec >= 210;

 SELECT collection_name
   FROM collection
  WHERE release_year 
BETWEEN 2018
    AND 2020;
    
  SELECT artist_name
    FROM artist
   WHERE artist_name
NOT LIKE '% %';

SELECT song_name
  FROM song
 WHERE song_name
  LIKE '%My%';