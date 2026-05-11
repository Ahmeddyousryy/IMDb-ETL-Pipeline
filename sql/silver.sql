
DROP TABLE IF EXISTS silver.tmdb_movies;
CREATE TABLE silver.tmdb_movies (
	imdb_id VARCHAR(50),
	release_date DATE,
	revenue BIGINT,
	runtime INT,
	budget BIGINT
);

