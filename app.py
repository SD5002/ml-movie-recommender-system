import streamlit as st
import pickle 
import numpy as np
import requests


movies=pickle.load(open("movies_list.pkl","rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))
similarity = np.array(similarity, dtype='float')
 

movies_list=movies['title'].values


st.header("Movie Recommender System")
select_value=st.selectbox("Select Movies from dropdown",movies_list)

def fetch_poster(movie_id):
    response=requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=d84ec9aa682d51dcd8c45d0239305da2&language=en-US")
    data=response.json()
    poster_path=data['poster_path'] 
    full_path="https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path

def recommend(movie):
    if movie not in movies['title'].values:
        return ["Movie not found."]

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_poster=[]
    recommend_movie=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movie_id))
    
    return recommend_movie,recommend_poster

    
if st.button("Show Recommend"):
    movie_names,movie_posters=recommend(select_value)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(movie_names[0])
        st.image(movie_posters[0])
    with col2:
        st.text(movie_names[1])
        st.image(movie_posters[1])
    with col3:
        st.text(movie_names[2])
        st.image(movie_posters[2])
    with col4:
        st.text(movie_names[3])
        st.image(movie_posters[3])
    with col5:
        st.text(movie_names[4])
        st.image(movie_posters[4])
