import sqlalchemy

DATA_SETS = [
    'IMDb_movie_titles',
    'IMDb_movie_ratings',
    'IMDb_name_basics',
    'IMDb_movie_crew',
    'TMDb_movie_info'
]


DATA_SOURCES =  {

    'IMDb_movie_titles'  : 'datasets/movie_titles.csv',
    'IMDb_movie_ratings' : 'datasets/movie_ratings.csv',
    'IMDb_name_basics'   : 'datasets/name_basics.csv',
    'IMDb_movie_crew'    : 'datasets/title_crew.csv',
    'TMDb_movie_info'    : 'datasets/TMDB_movies.csv'
}

BRONZE_LAYER_TABLES = {

    'IMDb_movie_titles'  : 'imdb_movie_titles',
    'IMDb_movie_ratings' : 'imdb_movie_ratings',
    'IMDb_name_basics'   : 'imdb_name_basics',
    'IMDb_movie_crew'    : 'imdb_movie_crew',
    'TMDb_movie_info'    : 'tmdb_movies'

}
DATA_BASE_CONNECTION_URL = "postgresql+psycopg://postgres:Mema@localhost:5432/movies_data_warehouse"

sql_engine = sqlalchemy.create_engine(DATA_BASE_CONNECTION_URL)

