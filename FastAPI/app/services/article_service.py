from sqlalchemy.orm import Session
from sqlalchemy import func
from ..models import Article
from ..schemas.article import ArticleCreate, ArticleUpdate


# Servicio para crear un artículo
def create_article(db: Session, article: ArticleCreate):
    db_article = Article(**article.dict())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article


# Servicio para obtener todos los artículos
def get_articles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Article).offset(skip).limit(limit).all()


# Servicio para obtener un artículo por ID
def get_article_by_id(db: Session, article_id: int):
    return db.query(Article).filter(Article.article_id == article_id).first()


# Servicio para actualizar un artículo
def update_article(db: Session, article_id: int, article: ArticleUpdate):
    db_article = db.query(Article).filter(Article.article_id == article_id).first()
    if db_article:
        for key, value in article.dict(exclude_unset=True).items():
            setattr(db_article, key, value)
        db.commit()
        db.refresh(db_article)
    return db_article


# Servicio para eliminar un artículo
def delete_article(db: Session, article_id: int):
    db_article = db.query(Article).filter(Article.article_id == article_id).first()
    if db_article:
        db.delete(db_article)
        db.commit()
    return db_article


# Servicio para contar el total de artículos
def count_articles(db: Session):
    return db.query(func.count(Article.article_id)).scalar()


# Servicio para obtener artículos por autor
def get_articles_by_author(db: Session, author_id: int):
    return db.query(Article).filter(Article.author_id == author_id).all()


# Servicio para buscar artículos por título
def search_articles_by_title(db: Session, title: str):
    return db.query(Article).filter(Article.title.ilike(f"%{title}%")).all()


# Servicio para obtener artículos publicados en una fecha específica
def get_articles_by_date(db: Session, published_date):
    return db.query(Article).filter(Article.published_date == published_date).all()


# Servicio para obtener los artículos más recientes
def get_recent_articles(db: Session, limit: int = 5):
    return db.query(Article).order_by(Article.published_date.desc()).limit(limit).all()
