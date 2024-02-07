from pydantic import BaseModel

class Article(BaseModel):
    title: str
    year: str
    conference: str
    status: int
    link: str 

class ArticleService(BaseModel):
    index: str
    title: str
    year: str
    conference: str
    status: int
    link: str

class Achievement(BaseModel):
    year: int
    date: str
    title: str
    link: str 
    img: str