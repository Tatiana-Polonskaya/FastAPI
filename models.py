from pydantic import BaseModel

class Indexation(BaseModel):
    id: int
    title: str


class Article(BaseModel):
    indexation: int # id of Indexation
    title: str
    year: str
    conference: str
    status: int
    link_article: str 
    link_collection: str 
    authors: str


class ArticleService(BaseModel):
    index: str
    indexation: int # id of Indexation
    title: str
    year: str
    conference: str
    status: int
    link_article: str 
    link_collection: str 
    authors: str

class Achievement(BaseModel):
    date: str
    title: str
    reward: str
    level: str
    diploma_link: str 
    event_link: str 
    img: str