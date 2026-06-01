import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")

st.title("rec_o")
st.write("Frontend Streamlit connecté au backend FastAPI")

artist_name = st.text_input("Nom de l'artiste", "Eminem")
genre = st.text_input("Genre musical", "Rap")

if st.button("Obtenir une recommandation"):

    payload = {
        "ArtistName": artist_name,
        "Genre": genre
    }

    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        result = response.json()

        st.success("Recommandation trouvée")
        st.write("Artiste recommandé :", result["ArtistName"])
        st.write("Genre :", result["Genre"])

    else:
        st.error("Erreur API")
        st.write(response.text)
