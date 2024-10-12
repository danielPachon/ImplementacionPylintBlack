from fastapi import FastAPI, Depends, HTTPException
from .config.database import engine, Base
from .routes import article_route, author_route

app = FastAPI()

# Crea todas las tablas
Base.metadata.create_all(bind=engine)

# Incluye las rutas
app.include_router(article_route.router)
app.include_router(author_route.router)
