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
- Dynamic movie posters fetched from TMDB API  
- Responsive and clean UI with autocomplete search  
- Scalable and modular project structure  
- Ready for deployment on modern cloud platforms like Render or Heroku

---

## 🧠 How It Works

1. User inputs/selects a movie  
2. The system finds similar movies based on content similarity  
3. It fetches official posters dynamically from TMDB  
4. Results display in a neat, mobile-friendly layout

---

## 🗂️ Project Structure

movies-recommender-system/
│
├── app/
│ ├── init.py # Flask app factory
│ ├── config.py # Configuration (API keys, constants)
│ ├── models/
│ │ ├── recommender.py # Recommendation logic
│ │ ├── movie_dict.pkl # Movies data pickle
│ │ └── similarity.pkl # Similarity matrix pickle
│ ├── routes/
│ │ └── main.py # Flask route handlers/blueprints
│ ├── services/
│ │ └── recommender_service.py # Business logic layer
│ ├── templates/
│ │ └── index.html # Frontend HTML template
│ └── static/
│ └── posters/ # Movie posters folder
│ └── mrs.png
├── run.py # App entry point
├── requirements.txt # Python dependencies
├── Procfile.txt # Deployment command for Render/Heroku
├── .env.example # Example environment config file
├── README.md # Project documentation
└── .gitignore


---

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

---

## 🚦 How to Run Locally

git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender-system
python -m venv venv
venv\Scripts\activate # Windows (use source venv/bin/activate on Mac/Linux)
pip install -r requirements.txt

Add your TMDB API key in app/config.py or use environment variables
python run.py


Open [http://localhost:5000](http://localhost:5000) in your browser.

---

## 🌐 Deployment

- Push your code to GitHub
- Connect your repo with Render or Heroku
- Use `gunicorn run:app` as start command
- Add necessary environment variables (`TMDB_API_KEY`)
- Deploy and enjoy live recommendations!

---

## 🔒 Best Practices

- Store secrets like API keys securely in environment variables  
- Use modular and scalable code for easy future enhancements  
- Cache API responses in production to improve performance

---

## 🙌 Contributing

Issues and pull requests are welcome! Feel free to improve UI, add features, or optimize performance.

---

> Made with care using Flask, ML similarity, and TMDB API. Happy movie hunting! 🎥✨
