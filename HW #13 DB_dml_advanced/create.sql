CREATE TABLE IF NOT EXISTS artist (
	id SERIAL PRIMARY KEY,
	artist_name VARCHAR(30) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS genre (
	id SERIAL PRIMARY KEY,
	genre_name VARCHAR(30) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS album (
	id SERIAL PRIMARY KEY,
	album_name 		VARCHAR(30) UNIQUE NOT NULL,
	release_year 	INTEGER  	NOT NULL,
								CONSTRAINT release_year
								CHECK(release_year BETWEEN 1950 AND 2022)
);

CREATE TABLE IF NOT EXISTS song (
	id SERIAL PRIMARY KEY,
	song_name 		VARCHAR(50) UNIQUE NOT NULL,
	duration_sec 	INTEGER 	NOT NULL,
	album_id 		INTEGER 	NOT NULL REFERENCES album(id),
								CONSTRAINT duration_sec
								CHECK(duration_sec BETWEEN 0 AND 360) 
);

CREATE TABLE IF NOT EXISTS collection (
	id SERIAL PRIMARY KEY,
	collection_name	VARCHAR(30) UNIQUE NOT NULL,
	release_year 	INTEGER 	NOT NULL,
									CONSTRAINT release_year
									CHECK(release_year BETWEEN 1950 AND 2022)
);

CREATE TABLE IF NOT EXISTS artist_genre (
	artist_id 	INTEGER REFERENCES artist(id),
	genre_id 	INTEGER	REFERENCES genre(id),
										CONSTRAINT ag PRIMARY KEY (artist_id, genre_id)
);

CREATE TABLE IF NOT EXISTS artist_album (
	artist_id 	INTEGER	REFERENCES artist(id),
	album_id 	INTEGER	REFERENCES album(id),
										CONSTRAINT aa PRIMARY KEY (artist_id, album_id)
);

CREATE TABLE IF NOT EXISTS song_collecion (
	song_id 		INTEGER	REFERENCES Song(id),
	collection_id 	INTEGER	REFERENCES Collection(id),
										CONSTRAINT sc PRIMARY KEY (song_id, collection_id)
);