
/*
========================================================================
DDL Scripts : Create the Tables of the Gold layer
========================================================================

 Script Purpose :
	This script creates and populates the tables in the gold schema.
	It first checks whether the tables already exist and drops them if they do,
	then recreates them and loads the transformed data from the Silver layer.

	Run this script to re-define the DDL of the 'GOLD' Tables

*/

DROP TABLE IF EXISTS gold.dim_director;
CREATE TABLE gold.dim_director AS
	SELECT
		ROW_NUMBER() OVER(ORDER BY director_id) AS director_key,
		director_id,
		director_name,
		birth_year,
		NULLIF(death_year,0) AS death_year
	FROM silver.imdb_name_basics;



DROP TABLE IF EXISTS gold.dim_date;
CREATE TABLE gold.dim_date AS
	SELECT
		imdb_id AS movie_id,
		ROW_NUMBER() OVER (ORDER BY imdb_id) AS date_key,
		release_date::DATE AS date,
		EXTRACT(MONTH FROM release_date) AS Month,
		EXTRACT(QUARTER FROM release_date) AS Quarter,
		EXTRACT(YEAR FROM release_date) AS Year	
	FROM silver.tmdb_movies;


DROP TABLE IF EXISTS gold.dim_movie;
CREATE TABLE gold.dim_movie AS
	SELECT
		ROW_NUMBER() OVER (ORDER BY movie_id) AS movie_key,
		movie_id,
		movie_name,
		is_adult
	FROM silver.imdb_movie_titles;


DROP TABLE IF EXISTS gold.dim_genre;
CREATE TABLE gold.dim_genre AS
	SELECT
		genre_id AS genre_key,
		genre
	FROM silver.imdb_genres;

DROP TABLE IF EXISTS gold.bridge_movie_genre;
CREATE TABLE gold.bridge_movie_genre AS
	SELECT
		movie_key,
		mg.genre_id AS genre_key
	FROM silver.imdb_movie_genre mg
	JOIN silver.imdb_genres g ON mg.genre_id = g.genre_id
	JOIN gold.dim_movie mv ON mv.movie_id = mg.movie_id
	ORDER BY movie_key;


DROP TABLE IF EXISTS gold.fact_movie_performance;
CREATE TABLE gold.fact_movie_performance AS
	SELECT 
		movie_key,
		director_key,
		date_key,
		revenue,
		budget,
		runtime,
		average_rating,
		votes
	FROM gold.dim_movie gv 
	JOIN silver.tmdb_movies tv ON gv.movie_id = tv.imdb_id
	JOIN silver.imdb_movie_ratings mr ON mr.movie_id = gv.movie_id
	JOIN gold.dim_date gd ON gd.movie_id = gv.movie_id
	JOIN silver.imdb_movie_crew mc ON mc.movie_id = gv.movie_id
	JOIN gold.dim_director gdir ON gdir.director_id = mc.director_id
	ORDER BY movie_key;


CREATE TABLE gold.bridge_movie_genre_ratio AS
	SELECT
		movie_key,
		genre_key,
		ROUND(1.0 / COUNT(*) OVER (PARTITION BY movie_key),2) AS allocate_factor
	FROM gold.bridge_movie_genre
	