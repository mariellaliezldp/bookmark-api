# Bookmark API (FastAPI Technical Assessment)

This is a simple Bookmark API built using FastAPI and containerized with Docker.

It allows users to register, login, and manage bookmarks with tags, search, and filters.

## Tech Stack

- FastAPI
- SQLAlchemy
- MySQL
- SQLite (for testing)
- JWT Authentication
- Docker / Docker Compose
- Pytest

---

## How to Run

### 1. Clone repository

git clone https://github.com/mariellaliezldp/bookmark-api.git

cd bookmark-api


### 2. Create environment variables

Create a .env file (do not commit this file):

#### SECRET_KEY=your-secret-key

#### ALGORITHM=HS256

#### MYSQL_ROOT_PASSWORD=your-password

#### DATABASE_URL=mysql+pymysql://root:your-password@db:3306/bookmark_db


### 3. Start application

docker-compose up --build


### 4. Run migrations

docker exec -it bookmark_api alembic upgrade head


### API Documentation

After running the app:

### Swagger UI: http://localhost:8000/docs

---

## Testing

Run tests:

python -m pytest

## Docker Architecture

#### FastAPI app runs in container bookmark_api

#### MySQL runs in container bookmark_mysql

#### Services communicate via Docker network (db:3306)


## Notes

Database runs inside Docker container

Alembic is used for migrations

JWT is used for authentication

Each user can only access their own bookmarks

---

- MLDP
