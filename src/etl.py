from etl.extract import extract_csv
from etl.load import load_sql
from config.settings import DATA_SOURCES
from config.settings import sql_engine



df_tmdb_movies = extract_csv(DATA_SOURCES['TMDb_movie_info'])
load_sql(dataframe = df_tmdb_movies,table = 'tmdb_movies',schema='bronze',connection = sql_engine,if_exists = 'replace',index=False)

# df_imdb_movie_titles = extract_csv(DATA_SOURCES['IMDb_movie_titles'])
# load_sql(dataframe=df_imdb_movie_titles,table='imdb_movie_titles',schema='bronze',connection=sql_engine,if_exists = 'replace',index=False)

# df_imdb_movie_ratings = extract_csv(DATA_SOURCES['IMDb_movie_ratings'])
# load_sql(dataframe=df_imdb_movie_ratings,table='imdb_movie_ratings',schema='bronze',connection=sql_engine,if_exists = 'replace',index=False)


# df_imdb_name_basics = extract_csv(DATA_SOURCES['IMDb_name_basics'])
# load_sql(dataframe=df_imdb_name_basics,table='imdb_name_basics',schema='bronze',connection=sql_engine,if_exists = 'replace',index=False)

# df_imdb_movie_crew = extract_csv(DATA_SOURCES['IMDb_movie_crew'])
# load_sql(dataframe=df_imdb_movie_crew,table='imdb_movie_crew',schema='bronze',connection=sql_engine,if_exists = 'replace',index=False)