from fastapi import FastAPI
from app.routes import auth, bookmark

from app.core.error_handler import http_exception_handler, validation_exception_handler
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI(
    title="Bookmark API",
    description="A simple bookmark management system with auth, filtering, and tagging.",
    version="1.0.0"
)
app.include_router(auth.router)
app.include_router(bookmark.router)

app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)


# @app.get("/")
# def read_root():
#     return {"message": "Bookmark API running"}