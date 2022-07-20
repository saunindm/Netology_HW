INSERT INTO genre(genre_name)
VALUES
	('jazz'),
	('hip-hop'),
	('rock'),
	('electronic'),
	('rap');

INSERT INTO artist(artist_name)
VALUES
	('Judge'),
	('Lucas Knight'),
	('Allan Freedom'),
	('Will Nash'),
	('Fade'),
	('Damian Cameron'),
	('Trevor Cooper'),
	('Raymond Stevens');
	
INSERT INTO album(album_name, release_year)
VALUES
	('Bloodlust', 2018),
	('From insult to injury', 2019),
	('Speak of the god', 2020),
	('Crime of the century', 2018),
	('Love life', 2021),
	('Dinner for one', 2016),
	('Animal kingdom', 2018),
	('Ghost stories', 2003);

INSERT INTO collection(collection_name, release_year)
VALUES
	('My goodness', 2020),
	('Rain check', 2018),
	('The slim lady sings', 2005),
	('Final hour', 2021),
	('Cat eat cat world', 2008),
	('Bursting bubbles', 2003),
	('Lets do this', 2013),
	('Beyond infinity', 2019);

INSERT INTO song(album_id, song_name, duration_sec)
VALUES
	(4, 'Imagine Place', 235),
	(5, 'I Hope She is Walking Away', 144),
	(3, 'She Loves He Will Not Come Back', 275),
	(4, 'Baby, I Love The Road', 216),
	(3, 'Give Back His Way', 194),
	(2, 'Baby, I am A Cowgirl', 304),
	(3, 'Lost And Father', 284),
	(7, 'Scent Of My Affection', 213),
	(1, 'Forgot My Name', 176),
	(1, 'Set Me Free', 255),
	(6, 'I Need To Ride', 266),
	(5, 'Lazy And Call', 224),
	(2, 'Sweetie, Remember The Good Times', 261),
	(8, 'Everything Of Everything', 330),
	(6, 'I am Not Sorry', 219),
	(5, 'Green World', 295),
	(2, 'Dirty Harry', 222);
	
INSERT INTO artist_genre(artist_id, genre_id)
VALUES
	(1, 1),
	(1, 2),
	(2, 2),
	(2, 3),
	(3, 3),
	(3, 4),
	(4, 4),
	(4, 5),
	(5, 5),
	(5, 1),
	(6, 1),
	(6, 2),
	(7, 2),
	(7, 3),
	(8, 3),
	(8, 4);

INSERT INTO artist_album(artist_id, album_id)
VALUES
	(1, 1),
	(1, 2),
	(2, 3),
	(2, 4),
	(3, 5),
	(3, 6),
	(4, 7),
	(4, 8),
	(5, 8),
	(5, 7),
	(6, 6),
	(6, 5),
	(7, 4),
	(7, 3),
	(8, 2),
	(8, 1);

INSERT INTO song_collecion(song_id, collection_id)
VALUES
	(1, 1),
	(1, 2),
	(2, 3),
	(2, 4),
	(3, 5),
	(3, 6),
	(4, 7),
	(4, 8),
	(5, 7),
	(5, 6),
	(6, 5),
	(6, 4),
	(7, 3),
	(7, 2),
	(8, 1),
	(8, 2),
	(9, 3),
	(9, 4),
	(10, 5),
	(10, 6),
	(11, 7),
	(11, 8),
	(12, 7),
	(12, 6),
	(13, 5),
	(13, 4),
	(14, 3),
	(14, 2),
	(15, 1),
	(15, 2);