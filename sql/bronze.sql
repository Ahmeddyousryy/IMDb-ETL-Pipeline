/*
========================================================================
DDL Scripts : Create the Tables of Bronze Layer
========================================================================

Script Purpose :
	This script creates tables in the bronze schema, first it checks
	if they already exists, if so they are dropped

	Run this script to re-define the DDL of the 'Bronze' Tables

*/

DROP TABLE IF EXISTS bronze.imdb_movie_titles;
CREATE TABLE bronze.imdb_movie_titles (
	tconst VARCHAR(50),
	primaryTitle VARCHAR(50),
	isAdult INT,
	genres VARCHAR(50),
	startYear INT
);


DROP TABLE IF EXISTS bronze.imdb_movie_ratings;
CREATE TABLE bronze.imdb_movie_ratings (
	tconst VARCHAR(50),
	averageRating FLOAT,
	numVotes INT
);



DROP TABLE IF EXISTS bronze.imdb_name_basics;
CREATE TABLE bronze.imdb_name_basics (
	nconst VARCHAR(50),
	primaryName VARCHAR(50),
	birthYear INT,
	deathYear VARCHAR(20),
	primaryProfession VARCHAR(70),
	knownForTitles VARCHAR(70)
);


DROP TABLE IF EXISTS bronze.imdb_movie_crew;
CREATE TABLE bronze.imdb_movie_crew (
	tconst VARCHAR(50),
	directors VARCHAR(50),
	writers VARCHAR(50)
);


DROP TABLE IF EXISTS bronze.tmdb_movies;
CREATE TABLE bronze.tmdb_movies (
	imdb_id VARCHAR(50),
	release_date VARCHAR(50),
	revenue BIGINT,
	runtime INT,
	budget BIGINT
);



