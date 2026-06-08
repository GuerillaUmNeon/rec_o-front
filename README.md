# rec_o — Streamlit archive

This repository contains the **archived Streamlit version** of `rec_o`, the original interface used to search artists, manage a query and blacklist, and fetch artist recommendations from the recommendation API.

The active frontend has moved to the new **Next.js** implementation. Use and maintain the new application here:

- New frontend: [rec_o Next.js](https://github.com/GuerillaUmNeon/rec_o-next)

## Status

This codebase is kept for reference, history, and comparison purposes only.

- Archived: no active feature development
- Legacy stack: Streamlit + Python
- Scope: artist search, selection, blacklist management, and recommendation display

## What this version did

The archived Streamlit app provided:

- Artist search through the backend API
- Selection of artists for the recommendation query
- Artist blacklist management
- Basic request-rate limiting in session state
- Artist recommendation display with genres and official website links
- A custom Streamlit-styled UI using injected CSS

It relied on two secrets:

```toml
API_URL="http://127.0.0.1:8000"
TOKEN_API_KEY="123abc456def"
```

## Legacy stack

- Python
- Streamlit
- Requests
- Backend API secured with `X-API-Key`

## Notes on the archived code

This version was centered on a single Streamlit page and used `st.session_state` to store:

- selected artists
- blacklisted artists
- search results
- request timestamps
- current query and search errors

The UI included:

- a hero card for the `rec_o` title and short description
- left-column controls for search, selected artists, blacklist, and recommendation count
- a right-column recommendation panel
- custom CSS for cards, selected rows, blacklist rows, and genre chips

## Collaborators

- [cherguia](https://github.com/cherguia)
- [ThomasIsHere](https://github.com/ThomasIsHere)
- [BenJ676](https://github.com/BenJ676)
- [GuerillaUmNeon](https://github.com/GuerillaUmNeon)

## Migration

This Streamlit version is preserved as an archive. For current development, refer to the new Next.js frontend:

- [rec_o Next.js](https://github.com/GuerillaUmNeon/rec_o-next)

## Archive purpose

This folder remains useful for:

- tracing the first product iteration
- comparing UX and architecture decisions
- preserving the original Streamlit implementation
- documenting the transition from Streamlit to Next.js
