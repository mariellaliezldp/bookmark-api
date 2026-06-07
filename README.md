# Bookmark API (FastAPI Technical Assessment)

This is a simple Bookmark API built using FastAPI.

It allows users to register, login, and manage bookmarks with tags, search, and filters.

---

## Features

### Authentication
- Register user
- Login user
- JWT token authentication

### Bookmarks
- Create bookmark
- Get all bookmarks (per user)
- Update bookmark
- Delete bookmark

### Search & Filter
- Search by keyword (title or description)
- Filter by tag
- Filter by date (from / to)
- Pagination (page, limit)

### Stats
- Total bookmarks
- Total tags
- Top tags
- Bookmarks per month

---

## Tech Stack

- FastAPI
- SQLAlchemy
- MySQL
- SQLite (for testing)
- JWT Authentication
- Pytest

---

## How to Run

### 1. Install dependencies
pip install -r requirements.txt

### 2. Setup database
Update `.env` file:

### 3. Run migrations
alembic upgrade head

### 4. Run server
uvicorn app.main:app --reload

## API Documentation
After running the server:
Swagger UI:
http://127.0.0.1:8000/docs

## API Endpoints

### Auth
- POST /api/auth/register
- POST /api/auth/login

### Bookmarks
- GET /api/bookmarks
- POST /api/bookmarks
- GET /api/bookmarks/{id}
- PUT /api/bookmarks/{id}
- DELETE /api/bookmarks/{id}

### Stats
- GET /api/bookmarks/stats

---

## Notes

- Each user can only see their own bookmarks
- Uses JWT for authentication
- Uses SQLAlchemy for database
- Includes search, filter, and pagination

## Testing
Run tests:
python -m pytest

- MLDP
