
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings
 
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# adding middleware in order to allow requests to be send from browser, 
# ex: fetch('http://localhost:8000/').then(res => res.json()).then(console.log)
# origins = ["https://www.google.com"]
origins = ["*"] # - every single domain, in case API should be public

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():    
    return {"message": "Hello world!"} 




    # 18:06:14
