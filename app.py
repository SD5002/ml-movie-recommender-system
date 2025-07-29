import streamlit as st
import pickle 
import numpy as np


movies=pickle.load(open("movies_list.pkl","rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))
similarity = np.array(similarity, dtype='float')
 

movies_list=movies['title'].values


st.header("Movie Recommender System")
select_value=st.selectbox("Select Movies from dropdown",movies_list)

def recommend(movie):
    if movie not in movies['title'].values:
        return ["Movie not found."]

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    return [movies.iloc[i[0]].title for i in movie_list]


    
if st.button("Show Recommend"):
    movie_names=recommend(select_value)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(movie_names[0])
    with col2:
        st.text(movie_names[1])
    with col3:
        st.text(movie_names[2])
    with col4:
        st.text(movie_names[3])
    with col5:
        st.text(movie_names[4])
