from app.database import Base, engine
import app.models.user
import app.models.bookmark
import app.models.tag
import app.models.bookmark_tags

Base.metadata.create_all(bind=engine)
print("Tables created successfully")