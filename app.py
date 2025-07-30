import streamlit as st
import pickle 
import numpy as np
import requests
import time


movies = pickle.load(open("movies_list.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))
similarity = np.array(similarity, dtype='float')

movie_list = movies['title'].values

st.header("Movie Recommender System")
select_value = st.selectbox("Select a movie", movie_list)


def fetch_poster(movie_id):
    try:
        response = requests.get(
            f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=d84ec9aa682d51dcd8c45d0239305da2&language=en-US"
        )
        data = response.json()
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    except:
       
        return "https://via.placeholder.com/500x750.png?text=No+Image"


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movie_list_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []  
    recommended_posters = []

    for i in movie_list_indices:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
        

    return recommended_movies, recommended_posters

if st.button("Recommend"):
    names, posters = recommend(select_value)
    cols = st.columns(5)
    
    for i in range(5):
        with cols[i]:
            st.image(posters[i])
            st.text(names[i])    
  
