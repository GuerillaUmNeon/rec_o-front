# rec_o-front

Frontend Streamlit du projet rec_o.

## Installation

```bash
git clone <repository_url>
cd rec_o-front
pip install -r requirements.txt
```

## Configuration

Créer un fichier `.env` :

```env
API_URL=http://127.0.0.1:8000/predict
TOLEN_API_KEY=YOUR_API_KEY
```

## Lancement du frontend

```bash
streamlit run app.py
```

L'application sera disponible sur :

```text
http://localhost:8501
```

## Backend

Le backend FastAPI doit être lancé avant le frontend :

```bash
uvicorn app.main:app --reload
```

API disponible sur :

```text
http://127.0.0.1:8000
```

## Technologies

* Streamlit
* FastAPI
* Requests
* Python Dotenv
