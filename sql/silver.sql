
DROP TABLE IF EXISTS silver.tmdb_movies;
CREATE TABLE silver.tmdb_movies (
	imdb_id VARCHAR(50),
	release_date DATE,
	revenue BIGINT,
	runtime INT,
	budget BIGINT
);

DROP TABLE IF EXISTS silver.imdb_genres;
CREATE TABLE silver.imdb_genres (
	genre_id INT,
	genre VARCHAR(20)
);


DROP TABLE IF EXISTS silver.imdb_movie_genre;
CREATE TABLE silver.imdb_movie_genre (
	movie_id VARCHAR(50),
	genre_id INT
);

DROP TABLE IF EXISTS silver.imdb_movie_titles;
CREATE TABLE silver.imdb_movie_titles (
	movie_id VARCHAR(50),
	movie_name VARCHAR(70),
	is_adult BOOLEAN,
	runtime INT,
	release_year INT
);





