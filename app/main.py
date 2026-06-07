from fastapi import FastAPI
from app.routes import auth, bookmark

app = FastAPI()

app.include_router(auth.router)
app.include_router(bookmark.router)


# @app.get("/")
# def read_root():
#     return {"message": "Bookmark API running"}