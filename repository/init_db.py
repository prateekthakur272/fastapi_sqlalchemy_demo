from database import (engine, Base,)
from models import Note
Base.metadata.create_all(bind=engine)