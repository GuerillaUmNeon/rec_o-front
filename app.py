import time

import requests
import streamlit as st

API_URL = st.secrets["API_URL"]
TOKEN_API_KEY = st.secrets["TOKEN_API_KEY"]

MAX_REQUESTS = 5
WINDOW_SECONDS = 60

st.title("rec_o")
st.write("Frontend Streamlit connecté au backend FastAPI")

headers = {
    "X-API-Key": TOKEN_API_KEY
}

artist_query = st.text_input("Rechercher un artiste")
artist_options = {}

if artist_query.strip():
    search_response = requests.post(
        f"{API_URL}/search/artist",
        json={"name": artist_query},
        headers=headers,
    )

    if search_response.status_code == 200:
        artists = search_response.json()
        artist_options = {
            artist["artist_id"]: (
                f"{artist['name']} ({artist['disambiguation']})"
                if artist.get("disambiguation")
                else artist["name"]
            )
            for artist in artists
        }
    else:
        st.warning("Recherche artiste indisponible")
        st.write(search_response.text)

available_artist_ids = list(artist_options.keys())
selected_artist_ids = st.multiselect(
    "Artistes de départ",
    options=available_artist_ids,
    format_func=lambda artist_id: artist_options.get(artist_id, str(artist_id)),
    key="selected_artist_ids",
)

# artist_ids_text = st.text_input("IDs artistes supplémentaires", "")
top_n = st.number_input("Nombre de recommandations", min_value=1, max_value=50, value=5)

if st.button("Obtenir une recommandation"):
    now = time.time()
    if "request_timestamps" not in st.session_state:
        st.session_state.request_timestamps = []

    st.session_state.request_timestamps = [
        timestamp
        for timestamp in st.session_state.request_timestamps
        if now - timestamp < WINDOW_SECONDS
    ]

    if len(st.session_state.request_timestamps) >= MAX_REQUESTS:
        st.warning("Trop de requêtes. Réessayez dans une minute.")
        st.stop()

    # try:
    #     manual_artist_ids = [
    #         int(artist_id.strip())
    #         for artist_id in artist_ids_text.split(",")
    #         if artist_id.strip()
    #     ]
    # except ValueError:
    #     st.error("Les IDs doivent être des nombres séparés par des virgules.")
    #     st.stop()

    # artist_ids = selected_artist_ids + manual_artist_ids
    artist_ids = selected_artist_ids

    if not artist_ids:
        st.error("Sélectionne au moins un artiste ou renseigne un ID.")
        st.stop()

    st.session_state.request_timestamps.append(now)

    payload = {
        "ArtistIds": artist_ids,
        "TopN": top_n,
    }

    response = requests.post(f"{API_URL}/predict", json=payload, headers=headers)

    if response.status_code == 200:
        result = response.json()
        artists = result.get("artists", [])

        st.success("Recommandation trouvée")

        if not artists:
            st.info("Aucun artiste recommandé.")
        else:
            for artist in artists:
                st.subheader(artist.get("name", "Artiste inconnu"))
                st.write("Genres :", ", ".join(artist.get("genre", [])))

                website = next(
                    (
                        item.get("url") or item.get("urls")
                        for item in artist.get("urls", [])
                        if item.get("type") == 183
                    ),
                    None,
                )

                if website:
                    st.markdown(f"[Site officiel]({website})")

                st.divider()

    elif response.status_code == 429:
        st.warning("Trop de requêtes. Patientez un moment.")

    else:
        st.error("Erreur API")
        st.write(response.text)
