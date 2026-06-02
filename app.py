import time

import requests
import streamlit as st

API_URL = st.secrets["API_URL"]
TOKEN_API_KEY = st.secrets["TOKEN_API_KEY"]

MAX_REQUESTS = 5
WINDOW_SECONDS = 60

st.title("rec_o")
st.write("Frontend Streamlit connecté au backend FastAPI")

artist_name = st.text_input("Nom de l'artiste", "Eminem")
genre = st.text_input("Genre musical", "Rap")

if st.button("Obtenir une recommandation"):
    now = time.time()
    if "request_timestamps" not in st.session_state:
        st.session_state.request_timestamps = []

    st.session_state.request_timestamps = [
        t for t in st.session_state.request_timestamps
        if now - t < WINDOW_SECONDS
    ]

    if len(st.session_state.request_timestamps) >= MAX_REQUESTS:
        st.warning("Trop de requêtes. Réessayez dans une minute.")
    else:
        st.session_state.request_timestamps.append(now)

        payload = {
            "ArtistName": artist_name,
            "Genre": genre,
        }

        headers = {"X-API-Key": TOKEN_API_KEY}
        response = requests.post(f"{API_URL}/predict", json=payload, headers=headers)

        if response.status_code == 200:
            result = response.json()

            st.success("Recommandation trouvée")
            st.write("Artiste recommandé :", result["ArtistName"])
            st.write("Genre :", result["Genre"])

        elif response.status_code == 429:
            st.warning("Trop de requêtes. Patientez un moment.")

        else:
            st.error("Erreur API")
            st.write(response.text)
