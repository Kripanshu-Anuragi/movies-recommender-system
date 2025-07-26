# 🎬 Movie Recommender System — Flask & ML Similarity Based Web App

**A clean, responsive, and efficient content-based movie recommender built with Flask and similarity algorithms.**  
Uses TMDB API to fetch real movie posters for an engaging user experience.

---

## 💡 Overview

This app suggests movies similar to the one you like, by comparing movie content features through machine learning similarity techniques.  
It provides dynamic poster images and a smooth, easy-to-use web interface—all in a professional and modular Python Flask project.

---

## ✨ Features

- Content-based recommendations using similarity algorithms  
- **Dynamic movie posters fetched in real-time from TMDB API**  
- Responsive and clean UI with autocomplete search  
- Scalable and modular project structure  
- Ready for deployment on modern cloud platforms like Render or Heroku

---

## 🎥 Example Poster Display

When you search or select a movie, you’ll see real posters for recommended movies—dynamic from TMDB API:

![Recommended movies example](https://www.themoviedb.org/t/p/w600_and_h900_bestv2/4qTdy39nwY6NziJ6j9e0gktfozd.jpg)

> _Posters in your app UI will look like this—every recommendation has a real, official movie poster!_

_(You can also add your **own UI screenshot** here: take a screenshot of your app running locally, save it as `static/app_demo.png`, and use below:)_

## 🧠 How It Works

1. User inputs or selects a movie using a smart autocomplete search box.  
2. The system calculates similarity between the selected movie and others using machine learning content-based filtering techniques.  
3. Based on similarity scores, the top recommended movies are identified.  
4. Official movie posters for these recommendations are fetched dynamically from the TMDB API in real-time.  
5. The results and posters are displayed in a clean, responsive, mobile-friendly grid layout for an engaging user experience.

🗂️ Project Structure

movies-recommender-system/
│
├── app/
│   ├── __init__.py             # Flask app factory
│   ├── config.py               # Configuration (API keys, constants)
│   ├── models/
│   │   ├── recommender.py      # Recommendation logic
│   │   ├── movie_dict.pkl      # Movies data pickle (NOT on GitHub if >100MB)
│   │   └── similarity.pkl      # Similarity matrix pickle (NOT on GitHub if >100MB)
│   ├── routes/
│   │   └── main.py             # Flask route handlers/blueprints
│   ├── services/
│   │   └── recommender_service.py # Business logic layer
│   ├── templates/
│   │   └── index.html          # Frontend HTML template
│   └── static/
│       └── [optional] mrs.png  # Branding or fallback image
├── run.py                     # App entry point
├── requirements.txt           # Python dependencies
├── Procfile.txt               # Deployment command for Render/Heroku
├── .env.example               # Example environment config file
├── README.md                  # Project documentation (this file)
└── .gitignore

Note: Movie posters are fetched dynamically from TMDB at runtime; the static/posters folder is optional for branding or fallback only.

## ⚙️ Tech Stack

| Library/Tool   | Purpose                   |
|----------------|---------------------------|
| Python 3.12+   | Core language             |
| Flask          | Web framework             |
| pandas         | Data handling             |
| scikit-learn   | Similarity calculations   |
| requests       | HTTP requests for posters |
| Gunicorn       | Production WSGI server    |
| HTML/CSS/JS    | Responsive frontend UI    |


## 🚦 How to Run Locally

git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender-system
python -m venv venv
venv\Scripts\activate           # Windows (use `source venv/bin/activate` on Mac/Linux)
pip install -r requirements.txt

# Add your TMDB API key in app/config.py or set as environment variable
python run.py

Open http://localhost:5000 in your browser.

## 🌐 Deployment

- Push your code to GitHub  
- Connect your repo with Render or Heroku  
- Use `gunicorn run:app` as the start command  
- Add necessary environment variables (e.g., `TMDB_API_KEY`)  
- Deploy and enjoy live recommendations!

---

## 🔒 Best Practices

- Store secrets like API keys securely in environment variables  
- Modular and scalable code for easy future enhancements  
- Cache API responses in production to improve performance

---

## 🙌 Contributing

Issues and pull requests are welcome! Feel free to improve UI, add features, or optimize performance.

Made with care using Flask, ML similarity, and TMDB API. Happy movie hunting! 🎥✨
