from pydantic import BaseModel
from datetime import date


class ArticleBase(BaseModel):
    title: str
    content: str
    published_date: date


class ArticleCreate(ArticleBase):
    author_id: int


class Article(ArticleBase):
    article_id: int

    class Config:
        orm_mode = True
