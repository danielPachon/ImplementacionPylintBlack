from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas import article as article_schema
from ..services import article_service
from ..config.database import get_db

router = APIRouter(prefix="/articles", tags=["articles"])


@router.post("/", response_model=article_schema.Article)
def create_article(
    article: article_schema.ArticleCreate, db: Session = Depends(get_db)
):
    """
    Crea un nuevo artículo.
    """
    return article_service.create_article(db, article)


@router.get("/{article_id}", response_model=article_schema.Article)
def get_article(article_id: int, db: Session = Depends(get_db)):
    """
    Obtiene un artículo por su ID.
    """
    db_article = article_service.get_article(db, article_id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Artículo no encontrado")
    return db_article


@router.get("/", response_model=list[article_schema.Article])
def get_articles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Obtiene una lista de artículos, con paginación.
    """
    articles = article_service.get_articles(db, skip=skip, limit=limit)
    return articles


@router.put("/{article_id}", response_model=article_schema.Article)
def update_article(
    article_id: int,
    article: article_schema.ArticleCreate,
    db: Session = Depends(get_db),
):
    """
    Actualiza un artículo existente por su ID.
    """
    db_article = article_service.update_article(db, article_id, article)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Artículo no encontrado")
    return db_article


@router.delete("/{article_id}")
def delete_article(article_id: int, db: Session = Depends(get_db)):
    """
    Elimina un artículo por su ID.
    """
    result = article_service.delete_article(db, article_id)
    if not result:
        raise HTTPException(status_code=404, detail="Artículo no encontrado")
    return {"detail": "Artículo eliminado correctamente"}
