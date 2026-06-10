# rec_o — Streamlit Archive

A **2-week bootcamp data science project** – the original Streamlit frontend for exploring music recommendations.

**Live Archive:** [reco-front.streamlit.app](https://reco-front.streamlit.app/)

## Overview

This repository contains the **original Streamlit implementation** of rec_o, built during a 2-week data science bootcamp project. It served as the proof-of-concept for the music recommendation discovery interface and demonstrated the core functionality before evolving into the production-ready Next.js version.

**The active frontend has moved to:** [rec_o-next (Next.js)](https://github.com/GuerillaUmNeon/rec_o-next)

## Project Status

- **Status:** Archived – no active development
- **Purpose:** Reference, historical comparison, and transition documentation
- **Stack:** Python + Streamlit (legacy)
- **Scope:** Artist search, selection, blacklist management, and recommendation display

## Architecture & Implementation

### Single-Page Application

The Streamlit app was built as a single-page application (`app.py`) using `st.session_state` for client-side state management across user interactions.

### UI Layout

- **Hero Section:** Title and project description
- **Left Column:** Search, artist selection, blacklist, and recommendation count controls
- **Right Column:** Real-time recommendation results display

### Features Implemented

- 🔍 **Artist Search** – Backend API integration for artist lookup with disambiguation
- ✅ **Selection Management** – Add/remove artists from query list
- 🚫 **Blacklist Controls** – Exclude artists from recommendations
- ⏱️ **Request Rate Limiting** – 5 requests per 60-second window
- 🏷️ **Genre Display** – Recommendation results with genre chips
- 🔗 **Official Links** – Direct links to artist websites via MusicBrainz

### State Management

Session state tracked:

- `selected_artists` – Artists included in queries
- `blacklisted_artists` – Artists to exclude
- `search_results` – Current search results
- `request_timestamps` – Rate limiting timestamps
- `search_error` – User-facing error messages

### Styling

Custom CSS injected into Streamlit with responsive cards, themed chips, and context-aware colors for selected/blacklisted items.

## Tech Stack

- **Language:** Python 3
- **Framework:** [Streamlit](https://streamlit.io/) – Rapid web app framework
- **HTTP Client:** [Requests](https://requests.readthedocs.io/) – API communication
- **Environment:** [python-dotenv](https://pypi.org/project/python-dotenv/) – Configuration management

## Requirements

```
streamlit
requests
python-dotenv
```

## Environment Configuration

Requires `.streamlit/secrets.toml`:

```toml
API_URL = "http://127.0.0.1:8000"
TOKEN_API_KEY = "123abc456def"
```

## Why This Was Archived

While functional, the Streamlit implementation had limitations:

- **Scalability** – Single-page state management became complex
- **Customization** – Limited control over UI/UX beyond Streamlit defaults
- **Performance** – Full-page refreshes on state changes
- **Type Safety** – No TypeScript support
- **Production Readiness** – Not ideal for complex interactions

These constraints led to the development of **rec_o-next**, a modern Next.js implementation with:

- Full React component architecture
- TypeScript for type safety
- Tailwind CSS for advanced styling
- Server-side API routes
- Enhanced user experience with dual input modes (manual search + ListenBrainz)

## How to Run Locally

```bash
# Clone repository
git clone https://github.com/GuerillaUmNeon/rec_o-front.git
cd rec_o-front

# Create secrets file
mkdir -p .streamlit
cat > .streamlit/secrets.toml << EOF
API_URL = "http://127.0.0.1:8000"
TOKEN_API_KEY = "your-api-key"
EOF

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
```

The app will open at `http://localhost:8501`

## Project History

**Bootcamp Timeline:**

- **Week 1-2:** Built initial Streamlit proof-of-concept during data science bootcamp
- **Post-Bootcamp:** Evolved into production-ready Next.js implementation
- **Current:** Streamlit version archived as reference

## Collaborators

This bootcamp project was developed by:

- [@GuerillaUmNeon](https://github.com/GuerillaUmNeon)
- [@ThomasIsHere](https://github.com/ThomasIsHere)
- [@cherguia](https://github.com/cherguia)
- [@BenJ676](https://github.com/BenJ676)

Thank you to all contributors who helped build this initial version during the bootcamp!

## Related Projects

- **Current Frontend:** [rec_o-next](https://github.com/GuerillaUmNeon/rec_o-next) – Modern Next.js implementation
- **Backend API:** [rec_o](https://github.com/GuerillaUmNeon/rec_o) – Recommendation engine and search service
- **Live Application:** [rec-o-next.vercel.app](https://rec-o-next.vercel.app)

## Archive Value

This repository remains useful for:

- 📖 Tracing the first product iteration
- 🔄 Comparing UX and architecture decisions (Streamlit vs Next.js)
- 🏛️ Preserving the original implementation history
- 📚 Documenting the technology migration path
- 🎓 Educational reference for Streamlit development

## License

This project is private. See repository settings for access details.
