# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# posts = []

# class Post(BaseModel):
#     id: int
#     title: str
#     content: str
#     likes: int = 0

# post1 = Post(id=1, title="First Post", content="This is the content of the first Post.", likes=9)
# post2 = Post(id=2, title="second Post", content="This is the content of the second Post.", likes=10)
# post3 = Post(id=3, title="Third Post", content="This is the content of the third Post.")
# posts.extend([post1, post2, post3])

# @app.get("/posts")
# def return_post():
#     return {"posts": posts}

# @app.get("/posts/{post_id}")
# def return_post(post_id: int):
#     for post in posts:
#         if post.id == post_id:
#             return post
#         return {"message": "Post not found"}

# @app.post("/posts")
# def add_post(post: Post):
#     posts.append(post)
#     return {"message": "Post added", "post": post}
