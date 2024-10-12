from sqlalchemy.orm import Session
from ..schemas.author import AuthorCreate, Author
from ..models import Author as AuthorModel


def create_author(db: Session, author: AuthorCreate) -> Author:
    db_author = AuthorModel(**author.dict())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def get_author(db: Session, author_id: int) -> Author:
    return db.query(AuthorModel).filter(AuthorModel.author_id == author_id).first()


def get_authors(db: Session, skip: int = 0, limit: int = 10) -> list[Author]:
    return db.query(AuthorModel).offset(skip).limit(limit).all()


def update_author(db: Session, author_id: int, author: AuthorCreate) -> Author:
    db_author = db.query(AuthorModel).filter(AuthorModel.author_id == author_id).first()
    if db_author:
        for key, value in author.dict().items():
            setattr(db_author, key, value)
        db.commit()
        db.refresh(db_author)
        return db_author
    return None


def delete_author(db: Session, author_id: int) -> bool:
    db_author = db.query(AuthorModel).filter(AuthorModel.author_id == author_id).first()
    if db_author:
        db.delete(db_author)
        db.commit()
        return True
    return False
