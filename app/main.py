from fastapi import FastAPI
from app.routes import user, bookmark

app = FastAPI()

app.include_router(user.router)
app.include_router(bookmark.router)


# @app.get("/")
# def read_root():
#     return {"message": "Bookmark API running"}