/*
	Time Analysis : Analyze performance by Month -> Quarter -> Year (Roll up)
*/


-- Analyze total reveune, average budget and rating by Month
SELECT
	year,
	TO_CHAR(MAKE_DATE(2000, month::integer, 1), 'Mon') AS month,
	SUM(revenue) AS total_revenue,
	ROUND(AVG(budget)::numeric) AS average_budget,
    ROUND(AVG(average_rating)::numeric, 2) AS average_rating
FROM gold.fact_movie_performance
JOIN gold.dim_date USING (date_key)
WHERE year BETWEEN 2001 AND 2024
GROUP BY month,year
ORDER BY year


-- Analyze total reveune, average budget and rating by quarter
SELECT
	CONCAT(year, '-', 'Q',quarter) AS YearQuarter,
	SUM(revenue) AS total_revenue,
	ROUND(AVG(budget)::numeric) AS average_budget,
    ROUND(AVG(average_rating)::numeric, 2) AS average_rating
FROM gold.fact_movie_performance
JOIN gold.dim_date USING (date_key)
WHERE year BETWEEN 2001 AND 2024
GROUP BY year,quarter


-- Analyze total reveune, average budget and rating by year
SELECT
	year,
	SUM(revenue) AS total_revenue,
	ROUND(AVG(budget)::numeric) AS average_budget,
    ROUND(AVG(average_rating)::numeric, 2) AS average_rating
FROM gold.fact_movie_performance
JOIN gold.dim_date USING (date_key)
WHERE year BETWEEN 2001 AND 2024
GROUP BY year


/*
	Genre Analysis
*/

SELECT
	genre,
	ROUND(SUM(revenue * allocate_factor)) AS total_revenue,
	ROUND(SUM(budget * allocate_factor)) AS total_budget,
	COUNT(DISTINCT f.movie_key) AS total_movies
	
FROM gold.fact_movie_performance f
JOIN gold.bridge_movie_genre_ratio b ON f.movie_key = b.movie_key
JOIN gold.dim_genre g ON b.genre_key = g.genre_key
GROUP BY genre



SELECT
	genre,
	ROUND(AVG(average_rating)::numeric,2) AS average_rating
FROM gold.fact_movie_performance f
JOIN gold.bridge_movie_genre_ratio b ON f.movie_key = b.movie_key
JOIN gold.dim_genre g ON b.genre_key = g.genre_key
GROUP BY genre


/*
	Dice and slice Analysis
*/

SELECT 
	movie_name,
	revenue,
	budget,
	average_rating,
	year
FROM gold.fact_movie_performance
JOIN gold.dim_director USING (director_key)
JOIN gold.dim_movie USING (movie_key)
JOIN gold.dim_date USING (date_key)
WHERE director_name LIKE '%Nolan%'


SELECT 
	movie_name,
	director_name,
	runtime,
	average_rating
FROM gold.fact_movie_performance f
JOIN gold.dim_director USING (director_key)
JOIN gold.dim_movie USING (movie_key)
JOIN gold.dim_date USING (date_key)
JOIN gold.bridge_movie_genre_ratio b ON f.movie_key = b.movie_key
JOIN gold.dim_genre g ON b.genre_key = g.genre_key
WHERE year BETWEEN 2020 AND 2024
AND genre = 'Action'





