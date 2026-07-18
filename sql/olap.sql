SELECT
	 director_name,
	 SUM(revenue)
FROM gold.fact_movie_performance
JOIN gold.dim_director USING (director_key)
GROUP BY director_name
HAVING SUM(revenue) IS NOT NULL