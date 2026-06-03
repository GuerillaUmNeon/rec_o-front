# rec_o-front

Frontend Streamlit du projet `rec_o-front`, connecte à l'API FastAPI du depot `rec_o`.

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

NB: plus de détails dans le README du backend.

## Installation

Depuis le depot `rec_o-front` :

```bash
cd ~/code
mkdir GuerillaUmNeon
git clone git@github.com:GuerillaUmNeon/rec_o-front.git
cd rec_o-front

pyenv install 3.13.13
pyenv virtualenv 3.13.13 rec-o-front-env
pyenv local rec-o-front-env

pip install --upgrade pip
pip install -r requirements.txt
```

## Configuration

Le frontend lit l'URL de l'API depuis les secrets Streamlit.

Creer un fichier `.streamlit/secrets.toml` avec :

```toml
API_URL = "https://rec-o-api-779590423195.europe-west1.run.app"
TOKEN_API_KEY = "your-secret-token-here"
```

Pour tester avec un backend local, remplacez `API_URL` par exemple par :

```toml
API_URL = "http://127.0.0.1:8001"
TOKEN_API_KEY = "your-secret-token-here"
```

NB: vous pouvez aussi tester le front local qui appelle le back de prod avec l'URL de prod.

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
  "ArtistIds": [946],
  "TopN": 5
}
```

Reponse attendue :

```json
{
  "ArtistIds": [269151, 1341893, 2504, 2052342, 2091273]
}
```
