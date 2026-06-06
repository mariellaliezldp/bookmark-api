from fastapi import FastAPI
from app.routes import user, bookmark, tag

app = FastAPI()

app.include_router(user.router)
app.include_router(bookmark.router)
app.include_router(tag.router)


# @app.get("/")
# def read_root():
#     return {"message": "Bookmark API running"}