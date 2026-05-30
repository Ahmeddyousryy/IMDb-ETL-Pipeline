
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


DROP TABLE IF EXISTS silver.imdb_name_basics;
CREATE TABLE silver.imdb_name_basics(
	director_id VARCHAR(50),
	director_name VARCHAR(50),
	birth_year INT,
	death_year INT
);

DROP TABLE IF EXISTS silver.imdb_movie_ratings;
CREATE TABLE silver.imdb_movie_ratings (
	movie_id VARCHAR(50),
	average_rating FLOAT,
	votes INT
);



DROP TABLE IF EXISTS silver.imdb_movie_crew;
CREATE TABLE silver.imdb_movie_crew (
	movie_id VARCHAR(50),
	director_id VARCHAR(50)
);

SELECT * FROM silver.imdb_movie_crew


