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
	('From insult to injury', 2002),
	('Speak of the god', 2003),
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
VALUES(4, 'Imagine Place', 235),
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
	(6, 'I am Not Sorry', 219);