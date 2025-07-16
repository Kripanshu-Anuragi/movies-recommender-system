from flask import Flask, render_template, request, jsonify
from models.recommender import recommend, load_movies
import random

app = Flask(__name__)
movies = load_movies()

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    posters = []
    selected_movie = ''

    if request.method == 'POST':
        selected_movie = request.form.get('movie_name')
        recommendations, posters = recommend(selected_movie)
    else:
        # Random 10 movies on first load
        random_movies = random.sample(list(movies['title']), 10)

        for movie in random_movies:
            recs, imgs = recommend(movie)
            # Recommend returns recs for similar movies but we want the input movie + its poster
            if imgs:  # make sure poster exists
                recommendations.append(movie)
                posters.append(imgs[0])  # pick the first poster (assuming input movie ka hi ho)

    return render_template(
        'index.html',
        selected_movie=selected_movie,
        has_results=len(recommendations) > 0,
        movie_posters=zip(recommendations, posters)
    )

# 🔹 Autocomplete for movie input field
@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    term = request.args.get('term')
    suggestions = [title for title in movies['title'].values if term.lower() in title.lower()]
    return jsonify(suggestions[:10])  # Top 10 suggestions only

if __name__ == '__main__':
    app.run(debug=True)
