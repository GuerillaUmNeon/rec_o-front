# rec_o-front

Frontend Streamlit du projet `rec_o`, connecte a l'API FastAPI du depot `rec_o`.

## Prerequis

Le backend doit etre lancé avant d'utiliser le frontend.

Depuis le depot `rec_o` :

```bash
uvicorn app.main:app --reload
```

L'API est alors disponible sur :

- `http://localhost:8000`
- `http://localhost:8000/docs`
- `http://localhost:8000/predict`

## Installation

Depuis le depot `rec_o-front` :

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Configuration

Le frontend lit l'URL de l'API depuis les secrets Streamlit.

Creer un fichier `.streamlit/secrets.toml` avec :

```toml
API_URL = "http://localhost:8000/predict"
```

## Lancement

Depuis le depot `rec_o-front` :

```bash
streamlit run app.py
```

## Contrat API actuel

Le frontend envoie une requete `POST` vers `/predict`.

Payload exemple :

```json
{
  "ArtistName": "Eminem",
  "Genre": "Rap"
}
```

Reponse attendue :

```json
{
  "ArtistName": "Nom de l'artiste recommande",
  "Genre": "Genre musical"
}
```
