import pandas as pd
import etl.imdb_movie_title as imdb_movie_title
import etl.tmdb_movies as tmdb_movies




def run_silver_layer():
     
     
     df = imdb_movie_title.extract()
     movies_df, genre_df, imdb_bridge_df = imdb_movie_title.transform(df)
     imdb_movie_title.load(movies_df, genre_df, imdb_bridge_df)


     df = tmdb_movies.extract()
     df = tmdb_movies.transform(df)
     tmdb_movies.load(df)

     





  



    


    
    
