import time
import requests
import streamlit as st

st.set_page_config(
    page_title="rec_o",
    page_icon="🎵",
    layout="wide",
)

API_URL = st.secrets["API_URL"]
TOKEN_API_KEY = st.secrets["TOKEN_API_KEY"]

MAX_REQUESTS = 5
WINDOW_SECONDS = 60

headers = {"X-API-Key": TOKEN_API_KEY}

if "selected_artists" not in st.session_state:
    st.session_state["selected_artists"] = {}

if "request_timestamps" not in st.session_state:
    st.session_state["request_timestamps"] = []

st.markdown(
    """
    <style>
    .block-container {
        max-width: 1100px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .hero-card,
    .panel-card,
    .result-card {
        background: var(--secondary-background-color);
        border: 1px solid color-mix(in srgb, var(--text-color) 10%, transparent);
        border-radius: 18px;
        padding: 1.1rem 1.2rem;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04);
    }

    .hero-card,
    .panel-card,
    .result-card {
        margin-bottom: 1rem;
    }

    .hero-title {
        font-size: 2rem;
        font-weight: 700;
        line-height: 1.1;
        color: var(--text-color);
        margin-bottom: 0.2rem;
    }

    .hero-subtitle {
        font-size: 1rem;
        color: color-mix(in srgb, var(--text-color) 68%, transparent);
    }

    .section-title {
        font-size: 1rem;
        font-weight: 700;
        color: var(--text-color);
        margin-bottom: 0.75rem;
    }

    .helper-text {
        font-size: 0.92rem;
        color: color-mix(in srgb, var(--text-color) 68%, transparent);
        margin-bottom: 0.85rem;
    }

    .empty-state {
        padding: 0.95rem 1rem;
        border-radius: 14px;
        background: color-mix(in srgb, var(--secondary-background-color) 82%, var(--background-color));
        border: 1px dashed color-mix(in srgb, var(--text-color) 10%, transparent);
        color: color-mix(in srgb, var(--text-color) 68%, transparent);
    }

    .selected-artist-row {
        padding: 0.65rem 0.8rem;
        border-radius: 14px;
        background: color-mix(in srgb, var(--primary-color) 8%, var(--secondary-background-color));
        border: 1px solid color-mix(in srgb, var(--primary-color) 20%, transparent);
        color: var(--text-color);
        font-weight: 500;
    }

    .result-name {
        font-size: 1.1rem;
        font-weight: 700;
        color: var(--text-color);
        margin-bottom: 0.45rem;
    }

    .genre-wrap {
        margin-top: 0.2rem;
        margin-bottom: 0.8rem;
    }

    .genre-chip {
        display: inline-block;
        padding: 0.18rem 0.55rem;
        margin: 0 0.35rem 0.35rem 0;
        border-radius: 999px;
        background: color-mix(in srgb, var(--primary-color) 10%, var(--secondary-background-color));
        border: 1px solid color-mix(in srgb, var(--text-color) 10%, transparent);
        color: var(--text-color);
        font-size: 0.8rem;
    }

    div.stButton > button {
        border-radius: 10px;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-card">
        <div class="hero-title">rec_o</div>
        <div class="hero-subtitle">
            Cherche des artistes, ajoute-les à ta sélection, puis découvre des recommandations.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

left_col, right_col = st.columns([1, 1], gap="large")

with left_col:
    if "selected_artists" not in st.session_state:
        st.session_state["selected_artists"] = {}

    if "search_results" not in st.session_state:
        st.session_state["search_results"] = []

    if "search_option_labels" not in st.session_state:
        st.session_state["search_option_labels"] = []

    if "search_option_lookup" not in st.session_state:
        st.session_state["search_option_lookup"] = {}

    if "selected_search_label" not in st.session_state:
        st.session_state["selected_search_label"] = None

    def run_artist_search():
        query = st.session_state["artist_query_input"].strip()

        st.session_state["search_results"] = []
        st.session_state["search_option_labels"] = []
        st.session_state["search_option_lookup"] = {}
        st.session_state["selected_search_label"] = None

        if not query:
            return

        search_response = requests.post(
            f"{API_URL}/search/artist",
            json={"name": query},
            headers=headers,
        )

        if search_response.status_code == 200:
            artist_results = search_response.json()
            st.session_state["search_results"] = artist_results

            option_labels = []
            option_lookup = {}

            for i, artist in enumerate(artist_results):
                artist_id = artist["artist_id"]

                display_name = (
                    f"{artist['name']} ({artist['disambiguation']})"
                    if artist.get("disambiguation")
                    else artist["name"]
                )

                unique_label = display_name + ("\u200b" * i)

                option_labels.append(unique_label)
                option_lookup[unique_label] = {
                    "artist_id": artist_id,
                    "name": artist["name"],
                }

            st.session_state["search_option_labels"] = option_labels
            st.session_state["search_option_lookup"] = option_lookup

            if option_labels:
                st.session_state["selected_search_label"] = option_labels[0]

        else:
            st.session_state["search_error"] = search_response.text

    st.markdown('<div class="panel-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Recherche artiste</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="helper-text">Tape un nom puis appuie sur Entrée pour rechercher. Clique ensuite sur le bouton pour ajouter l’artiste.</div>',
        unsafe_allow_html=True,
    )

    st.text_input(
        "Rechercher un artiste",
        placeholder="Tape un nom d'artiste...",
        label_visibility="collapsed",
        key="artist_query_input",
        on_change=run_artist_search,
    )

    if st.session_state["search_option_labels"]:
        current_index = 0
        if st.session_state["selected_search_label"] in st.session_state["search_option_labels"]:
            current_index = st.session_state["search_option_labels"].index(
                st.session_state["selected_search_label"]
            )

        selected_label = st.selectbox(
            "Résultats de recherche",
            options=st.session_state["search_option_labels"],
            index=current_index,
            label_visibility="collapsed",
            key="artist_search_selectbox",
        )

        st.session_state["selected_search_label"] = selected_label

        if st.button("Ajouter l'artiste", use_container_width=True, key="add_artist_button"):
            selected_artist = st.session_state["search_option_lookup"][selected_label]
            st.session_state["selected_artists"][selected_artist["artist_id"]] = {
                "name": selected_artist["name"]
            }

    elif st.session_state["artist_query_input"].strip():
        st.markdown(
            '<div class="empty-state">Aucun artiste trouvé pour cette recherche.</div>',
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="panel-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Artistes sélectionnés</div>', unsafe_allow_html=True)

    if not st.session_state["selected_artists"]:
        st.markdown(
            '<div class="empty-state">Aucun artiste sélectionné.</div>',
            unsafe_allow_html=True,
        )
    else:
        ids_to_remove = []

        for artist_id, artist_data in st.session_state["selected_artists"].items():
            col_name, col_remove = st.columns([5, 1], vertical_alignment="center")

            with col_name:
                st.markdown(
                    f'<div class="selected-artist-row">{artist_data["name"]}</div>',
                    unsafe_allow_html=True,
                )

            with col_remove:
                if st.button("✕", key=f"remove_{artist_id}", use_container_width=True):
                    ids_to_remove.append(artist_id)

        for artist_id in ids_to_remove:
            del st.session_state["selected_artists"][artist_id]

    top_n = st.number_input(
        "Nombre de recommandations",
        min_value=1,
        max_value=50,
        value=5,
        key="top_n_input",
    )

    predict_clicked = st.button(
        "Obtenir une recommandation",
        use_container_width=True,
        key="predict_button",
    )

    st.markdown("</div>", unsafe_allow_html=True)

with right_col:
    st.markdown('<div class="panel-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Recommandations</div>', unsafe_allow_html=True)

    if predict_clicked:
        now = time.time()

        st.session_state["request_timestamps"] = [
            timestamp
            for timestamp in st.session_state["request_timestamps"]
            if now - timestamp < WINDOW_SECONDS
        ]

        if len(st.session_state["request_timestamps"]) >= MAX_REQUESTS:
            st.warning("Trop de requêtes. Réessayez dans une minute.")
            st.stop()

        artist_ids = list(st.session_state["selected_artists"].keys())

        if not artist_ids:
            st.error("Sélectionne au moins un artiste.")
            st.stop()

        st.session_state["request_timestamps"].append(now)

        payload = {
            "ArtistIds": artist_ids,
            "TopN": top_n,
        }

        response = requests.post(
            f"{API_URL}/predict/artist",
            json=payload,
            headers=headers,
        )

        if response.status_code == 200:
            result = response.json()
            artists = result.get("artists", [])

            if not artists:
                st.markdown(
                    '<div class="empty-state">Aucun artiste recommandé.</div>',
                    unsafe_allow_html=True,
                )
            else:
                for artist in artists:
                    website = next(
                        (
                            item.get("url") or item.get("urls")
                            for item in artist.get("urls", [])
                            if item.get("type") == 183
                        ),
                        None,
                    )

                    genres = artist.get("genre", [])

                    st.markdown('<div class="result-card">', unsafe_allow_html=True)
                    st.markdown(
                        f'<div class="result-name">{artist.get("name", "Artiste inconnu")}</div>',
                        unsafe_allow_html=True,
                    )

                    if genres:
                        chips_html = "".join(
                            f'<span class="genre-chip">{genre}</span>'
                            for genre in genres[:8]
                        )
                        st.markdown(
                            f'<div class="genre-wrap">{chips_html}</div>',
                            unsafe_allow_html=True,
                        )

                    if website:
                        st.markdown(f"[Site officiel]({website})")

                    st.markdown("</div>", unsafe_allow_html=True)

        elif response.status_code == 429:
            st.warning("Trop de requêtes. Patientez un moment.")
        else:
            st.error("Erreur API")
            st.write(response.text)

    else:
        st.markdown(
            '<div class="empty-state">Les recommandations apparaîtront ici après lancement.</div>',
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)