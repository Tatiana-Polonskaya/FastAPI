from fastapi import FastAPI, HTTPException
from models import Achievement, Article
from starlette import status
from starlette.responses import Response
from uuid import uuid4
from fastapi.middleware.cors import CORSMiddleware


import json

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
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

@app.get("/")
async def root():
    return {"greeting":"Hello world"}


@app.get("/articles/")
def get_all_articles():
    with open(pathArticles, "r") as f:
        articles = json.load(f)
    return articles


@app.get("/articles/{index}")
def get_article_by_index(index: str):
    with open(pathArticles, "r") as f:
        articles = json.load(f)
    try:
        article = next(a for a in articles if a["index"] == index)
        return article
    except StopIteration:
        raise HTTPException(status_code=404, detail="Article not found")

@app.post("/articles/")
def create_article(article: Article):
    with open(pathArticles, "r") as f:
        articles = json.load(f)
    newArticle = article.dict()
    unique_id = str(uuid4())
    newArticle["index"] =unique_id
    articles.append(newArticle)
    with open(pathArticles, "w") as f:
        json.dump(articles, f)
    return newArticle

@app.delete("/articles/{index}")
def delete_article_by_index(index: str):
    with open(pathArticles, "r") as f:
        articles = json.load(f)
    try:
        articles.remove(next(a for a in articles if a["index"] == index))
    except ValueError:
        raise HTTPException(status_code=404, detail="Article not found")
    with open(pathArticles, "w") as f:
        json.dump(articles, f)
    return {"message": "Article deleted"}



@app.get("/achievements/")
def get_all_achievements():
    with open(pathAchievements, "r") as f:
        achievements = json.load(f)
    return achievements

@app.get("/achievements/{index}")
def get_achievement_by_year(index: str):
    with open(pathAchievements, "r") as f:
        achievements = json.load(f)
    try:
        achievement = next(a for a in achievements if a["index"] == index)
        return achievement
    except StopIteration:
        raise HTTPException(status_code=404, detail="Achievement not found")


@app.post("/achievements/")
def create_achievement(achievement: Achievement):
    with open(pathAchievements, "r") as f:
        achievements = json.load(f)
    newAchienement = achievement.dict()
    unique_id = str(uuid4())
    newAchienement["index"] =unique_id
    achievements.append(newAchienement)
    with open(pathAchievements, "w") as f:
        json.dump(achievements, f)
    return newAchienement

@app.delete("/achievements/{index}")
def delete_achievement_by_index(index: str):
    with open(pathAchievements, "r") as f:
        achievements = json.load(f)
    try:
        achievements.remove(next(a for a in achievements if a["index"] == index))
    except ValueError:
        raise HTTPException(status_code=404, detail="Article not found")
    with open(pathArticles, "w") as f:
        json.dump(achievements, f)
    return {"message": "Achievement deleted"}

userlist = ["Spike","Jet","Ed","Faye","Ein"]
@app.get("/userlist")
async def userlist_(start: int = 0, limit: int = 10):
    return userlist[start:start+limit]


# @app.post("/lookup")
# async def userlookup(username: str = Form(...), user_id: str = Form("")):
#     return {"username": username, "user_id":user_id}