--1. ���������� ������������ � ������ �����
SELECT g.genre_name, COUNT(a.artist_name) AS anc
  FROM artist a
       JOIN artist_genre AS ag 
       ON a.id = ag.artist_id 
       JOIN genre AS g 
       ON g.id = ag.genre_id
 GROUP BY genre_name
 ORDER BY anc DESC;

--2. ���������� ������, �������� � ������� 2019-2020 �����
 SELECT COUNT(s.song_name) AS snc
   FROM song AS s
        JOIN album AS a 
        ON a.id = s.album_id
  WHERE a.release_year 
BETWEEN 2019 
    AND 2020;
    
--3. ������� ����������������� ������ �� ������� �������
SELECT a.album_name AS an, AVG(s.duration_sec) AS avg_dur 
  FROM song AS s
       JOIN album AS a ON a.id = s.album_id 
 GROUP BY an
 ORDER BY avg_dur;

--4. ��� �����������, ������� �� ��������� ������� � 2020 ����
SELECT artist_name
  FROM artist
 WHERE artist_name NOT IN 
       (SELECT DISTINCT ar.artist_name AS an
       FROM artist AS ar
            JOIN artist_album AS aa 
            ON aa.artist_id = ar.id 
            JOIN album AS al 
            ON al.id = aa.album_id
       WHERE al.release_year = 2020);

--5. �������� ���������, � ������� ������������ ���������� ����������� (�������� ����)
SELECT DISTINCT collection_name AS cn
  FROM collection AS c
       JOIN song_collecion AS sc 
       ON sc.collection_id = c.id 
       JOIN song AS s
       ON s.id = sc.song_id
       JOIN album AS al
       ON al.id = s.album_id
       JOIN artist_album AS aa
       ON aa.album_id = al.id
       JOIN artist AS ar
       ON ar.id = aa.artist_id
 WHERE ar.artist_name = 'Will Nash';
 
--6. �������� ��������, � ������� ������������ ����������� ����� 1 �����
SELECT al.album_name
  FROM album AS al
       JOIN artist_album AS aa
       ON aa.album_id = al.id
       JOIN artist AS ar
       ON ar.id = aa.artist_id
       JOIN artist_genre AS ag 
       ON ar.id = ag.artist_id 
       JOIN genre AS g 
       ON g.id = ag.genre_id
 GROUP BY al.album_name
HAVING COUNT(DISTINCT g.genre_name) > 1;

--7. ������������ ������, ������� �� ������ � ��������
SELECT song_name AS sn
FROM song AS s
LEFT JOIN song_collecion AS sc
ON sc.song_id = s.id
WHERE sc.collection_id IS NULL;

--8. �����������(-��), ����������� ����� �������� �� ����������������� ���� (������������ ����� ������ ����� ���� ���������)
SELECT ar.artist_name AS an, s.duration_sec
  FROM artist AS ar
       JOIN artist_album AS aa 
       ON aa.artist_id = ar.id 
       JOIN album AS al
       ON al.id = aa.album_id 
       JOIN song AS s 
       ON s.album_id = al.id
 GROUP BY an, s.duration_sec
HAVING s.duration_sec = 
       (SELECT MIN(duration_sec) 
          FROM song);

--9. �������� ��������, ���������� ���������� ���������� ������
SELECT album_name AS an, COUNT(album_name)
  FROM album AS a
       JOIN song AS s 
       ON s.album_id = a.id
 GROUP BY an
HAVING COUNT(album_name) = 
            (SELECT min(an) FROM (SELECT album_name, COUNT(album_name) AS an
               FROM album AS a
                    JOIN song AS s 
                    ON s.album_id = a.id
              GROUP BY album_name) AS anc);