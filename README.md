# rec_o-front

Frontend Streamlit du système de recommandation musicale **rec_o**.

Cette application permet d'interroger l'API FastAPI et d'afficher les recommandations retournées par le moteur de recommandation.

## Prérequis

* Python 3.12+
* Backend rec_o lancé localement
* Dépendances installées via `requirements.txt`

## Installation

```bash
git clone <repository_url>
cd rec_o-front
pip install -r requirements.txt
```

## Configuration

Créer un fichier `.env` à la racine du projet :

```env
API_URL=http://127.0.0.1:8000/predict
TOLEN_API_KEY=a378863f2be0908e9073161ea39d46a1577db74060bd1be9a61a0895773e142c
```

## Lancement du frontend

```bash
streamlit run app.py
```

L'application sera disponible à l'adresse :

```text
http://localhost:8501
```

## Backend

Le backend FastAPI doit être démarré avant le frontend.

Exemple :

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

## Fonctionnalités

* Interface utilisateur Streamlit
* Communication avec l'API FastAPI
* Gestion des variables d'environnement via `.env`
* Affichage des recommandations musicales
