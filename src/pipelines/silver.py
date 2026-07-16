
import etl.imdb_movie_title as imdb_movie_title
import etl.tmdb_movies as tmdb_movies
import etl.imdb_name_basics as imdb_name_basics
import etl.imdb_movie_ratings as imdb_movie_ratings
import etl.imdb_movie_crew as imdb_moive_crew


def run_silver_layer():
     
     
     df = imdb_movie_title.extract()
     movies_df, genre_df, imdb_bridge_df = imdb_movie_title.transform(df)
     imdb_movie_title.load(movies_df, genre_df, imdb_bridge_df)


     df = tmdb_movies.extract()
     df = tmdb_movies.transform(df)
     tmdb_movies.load(df)



     df = imdb_name_basics.extract()
     df = imdb_name_basics.transform(df)
     imdb_name_basics.load(df)

     df = imdb_movie_ratings.extract()
     df = imdb_movie_ratings.transform(df)
     imdb_movie_ratings.load(df)


     df = imdb_moive_crew.extract()
     df = imdb_moive_crew.transform(df)
     imdb_moive_crew.load(df)




     





  



    


    
    
