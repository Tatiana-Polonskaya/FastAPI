from fastapi import FastAPI, HTTPException
from models import Achievement, Article, ArticleService
from starlette import status
from starlette.responses import Response
from uuid import uuid4
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Body
from starlette.requests import Request

import json

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://localhost:3000",
    "https://localhost:5000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

pathArticles = "data/articles.json"
pathAchievements = "data/achievements.json"
pathIndexation = "data/indexation.json"

encoding="UTF-8"

@app.get("/")
async def root():
    return {"greeting":"Hello world"}


@app.get("/articles/")
def get_all_articles():
    with open(pathArticles, "r", encoding=encoding) as f:
        articles = json.load(f)
    return articles


@app.get("/articles/{id}")
def get_article_by_index(id: str):
    with open(pathArticles, "r", encoding=encoding) as f:
        articles = json.load(f)
    try:
        print("id", id)
        article = next(a for a in articles if a["index"] == id)
        return article
    except StopIteration:
        raise HTTPException(status_code=404, detail="Article not found")

@app.post("/articles/")
def create_article(article:  Article):
    with open(pathArticles, "r", encoding=encoding) as f:
        articles = json.load(f)
    newArticle = article.dict()
    unique_id = str(uuid4())
    newArticle["index"] =unique_id
    articles.append(newArticle)
    with open(pathArticles, "w", encoding=encoding) as f:
        json.dump(articles, f)
    return Response(status_code=status.HTTP_200_OK)

@app.delete("/articles/{index}")
def delete_article_by_index(index: str):
    with open(pathArticles, "r", encoding=encoding) as f:
        articles = json.load(f)
    try:
        articles.remove(next(a for a in articles if a["index"] == index))
    except ValueError:
        raise HTTPException(status_code=404, detail="Article not found")
    with open(pathArticles, "w", encoding=encoding) as f:
        json.dump(articles, f)
    return {"message": "Article deleted"}


@app.put("/articles/{index}")
def put_article_by_index(index: str, item: Article):
    with open(pathArticles, "r", encoding=encoding) as f:
        articles = json.load(f)
    try:
        editArticle = item.dict()
        editArticle["index"] = index
        articles[articles.index(next(a for a in articles if a["index"] == index))] = editArticle
    except ValueError:
        raise HTTPException(status_code=404, detail="Article not found")
    with open(pathArticles, "w") as f:
        json.dump(articles, f)
    return {"message": "Article updated"}


@app.get("/achievements/")
def get_all_achievements():
    with open(pathAchievements, "r", encoding=encoding) as f:
        achievements = json.load(f)
    return achievements

@app.get("/achievements/{index}")
def get_achievement_by_year(index: str):
    with open(pathAchievements, "r", encoding=encoding) as f:
        achievements = json.load(f)
    try:
        achievement = next(a for a in achievements if a["index"] == index)
        return achievement
    except StopIteration:
        raise HTTPException(status_code=404, detail="Achievement not found")


@app.post("/achievements/")
def create_achievement(achievement: Achievement):
    with open(pathAchievements, "r", encoding=encoding) as f:
        achievements = json.load(f)
    newAchienement = achievement.dict()
    unique_id = str(uuid4())
    newAchienement["index"] =unique_id
    achievements.append(newAchienement)
    with open(pathAchievements, "w", encoding=encoding) as f:
        json.dump(achievements, f)
    return newAchienement

@app.delete("/achievements/{index}")
def delete_achievement_by_index(index: str):
    with open(pathAchievements, "r", encoding=encoding) as f:
        achievements = json.load(f)
    try:
        achievements.remove(next(a for a in achievements if a["index"] == index))
    except ValueError:
        raise HTTPException(status_code=404, detail="Article not found")
    with open(pathArticles, "w", encoding=encoding) as f:
        json.dump(achievements, f)
    return {"message": "Achievement deleted"}



# --------------------------------------INDEXATION--------------------------------------
@app.get("/indexations")
async def get_all_indexations():
    with open(pathIndexation, "r", encoding=encoding) as f:
        indexations = json.load(f)
    return indexations


# @app.post("/lookup")
# async def userlookup(username: str = Form(...), user_id: str = Form("")):
#     return {"username": username, "user_id":user_id}