from flask import Blueprint, render_template, request, jsonify
from app.services.recommender_service import get_recommendations, get_movie_list
import random

main = Blueprint('main', __name__)
movies = get_movie_list()

@main.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    posters = []
    selected_movie = ''

    if request.method == 'POST':
        selected_movie = request.form.get('movie_name')
        recommendations, posters = get_recommendations(selected_movie)
    else:
        random_movies = random.sample(list(movies['title']), 37)
        for movie in random_movies:
            recs, imgs = get_recommendations(movie)
            if imgs:
                recommendations.append(movie)
                posters.append(imgs[0])

    return render_template(
        'index.html',
        selected_movie=selected_movie,
        has_results=len(recommendations) > 0,
        movie_posters=zip(recommendations, posters)
    )

@main.route('/autocomplete', methods=['GET'])
def autocomplete():
    term = request.args.get('term')
    suggestions = [title for title in movies['title'].values if term.lower() in title.lower()]
    return jsonify(suggestions[:10])
