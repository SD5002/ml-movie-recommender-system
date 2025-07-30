# Movie Recommendation System

## Project Overview

This project is a **content-based movie recommendation system** built using machine learning techniques. 
It recommends movies similar to the one selected by the user, based on cosine similarity of feature vectors.
The interface is powered by **Streamlit**, offering a simple yet powerful interactive user experience.

---

## Project Structure
├── app.py # Streamlit app script

├── movies_list.pkl # Pickle of processed movie DataFrame

├── similarity.pkl # Cosine similarity matrix

├── tmdb_5000_movies.csv # Original movie metadata from TMDB

├── tmdb_5000_credits.csv # Cast and crew data from TMDB

├── requirements.txt # Python dependencies

├── README.md # Project documentation

└── .gitignore


##  Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/SD5002/ml-movie-recommender-system.git
cd ml-movie-recommender-system

## 2. Install Dependencies

pip install -r requirements.txt

## 3.Run the App

streamlit run app.py



## Dataset Source 

tmdb_5000_movies.csv: Movie metadata
tmdb_5000_credits.csv: Cast and crew info

