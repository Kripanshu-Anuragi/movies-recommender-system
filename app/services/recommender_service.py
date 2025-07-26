from app.models.recommender import recommend, load_movies

def get_recommendations(movie_name):
    return recommend(movie_name)

def get_movie_list():
    return load_movies()


























