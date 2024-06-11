from fastapi import FastAPI, Request, Response, HTTPException, Depends
from schema import UserGet, PostGet
from database import SessionLocal
from table_post import Post
from table_user import User
from sqlalchemy.orm import Session

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
