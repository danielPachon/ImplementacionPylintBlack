from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas import author as author_schema
from ..services import author_service
from ..config.database import get_db

router = APIRouter(prefix="/authors", tags=["authors"])


@router.post("/", response_model=author_schema.Author)
def create_author(author: author_schema.AuthorCreate, db: Session = Depends(get_db)):
    return author_service.create_author(db, author)


@router.get("/{author_id}", response_model=author_schema.Author)
def get_author(author_id: int, db: Session = Depends(get_db)):
    author = author_service.get_author_by_id(db, author_id)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


@router.put("/{author_id}", response_model=author_schema.Author)
def update_author(
    author_id: int,
    updated_author: author_schema.AuthorCreate,
    db: Session = Depends(get_db),
):
    author = author_service.update_author(db, author_id, updated_author)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


@router.delete("/{author_id}")
def delete_author(author_id: int, db: Session = Depends(get_db)):
    author_service.delete_author(db, author_id)
    return {"detail": "Author deleted successfully"}


@router.get("/", response_model=list[author_schema.Author])
def get_all_authors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return author_service.get_all_authors(db, skip, limit)
