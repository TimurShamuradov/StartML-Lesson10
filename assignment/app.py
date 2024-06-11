from fastapi import FastAPI, Request, Response, HTTPException, Depends
from schema import UserGet, PostGet, FeedGet
from database import SessionLocal
from table_post import Post
from table_user import User
from table_feed import Feed
from sqlalchemy.orm import Session
from typing import List

app = FastAPI()


def get_db():
    with SessionLocal() as session:
        return session


@app.get("/user/{id}", response_model=UserGet)
def get_user(id: int, db: Session = Depends(get_db)):
    result = db.query(User).filter(User.id == id).first()
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return result


@app.get("/post/{id}", response_model=PostGet)
def get_post(id: int, db: Session = Depends(get_db)):
    result = db.query(Post).filter(Post.id == id).first()
    if not result:
        raise HTTPException(404, detail="post not found")
    return result


@app.get("/user/{id}/feed", response_model=List[FeedGet])
def get_user_feed(id: int, limit=10, db: Session = Depends(get_db)):
    query = db.query(Feed)\
             .filter(Feed.user_id == id)\
             .order_by(Feed.time.desc())\
             .limit(limit)\
             .all()

    if not query:
        return []
        raise HTTPException(200, detail="empty list")
    return query


@app.get("/post/{id}/feed", response_model=List[FeedGet])
def get_post_feed(id: int, limit: int = 10, db: Session = Depends(get_db)):
    post_feed = db.query(Feed)\
                 .filter(Feed.post_id == id)\
                 .order_by(Feed.time.desc())\
                 .limit(limit)\
                 .all()
    if not post_feed:
        return []
        raise HTTPException(200, detail="list is empty")
    return post_feed
