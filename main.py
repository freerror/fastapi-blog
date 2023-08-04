from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import sqlite3

app = FastAPI()

class User(BaseModel):
    id: Optional[int] = None
    name: str
    email: str

class Post(BaseModel):
    id: Optional[int] = None
    title: str
    content: str
    user_id: int

def get_db_connection():
    conn = sqlite3.connect('blog.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.get('/users/', response_model=List[User])
def read_users():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return users

@app.get('/users/{user_id}', response_model=User)
def read_user(user_id: int):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
    conn.close()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post('/users/')
def create_user(user: User):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (user.name, user.email))
    user.id = cursor.lastrowid
    conn.commit()
    conn.close()
    return user

@app.get('/posts/', response_model=List[Post])
def read_posts():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return posts

@app.get('/posts/{post_id}', response_model=Post)
def read_post(post_id: int):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.post('/posts/')
def create_post(post: Post):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO posts (title, content, user_id) VALUES (?, ?, ?)', (post.title, post.content, post.user_id))
    post.id = cursor.lastrowid
    conn.commit()
    conn.close()
    return post
