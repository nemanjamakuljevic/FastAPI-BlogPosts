from .. import models, schemas, utils
from fastapi import Body, FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from typing import Optional, List

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.get("/", response_model=List[schemas.UserOut])
def get_posts(db: Session = Depends(get_db)):
    users = db.query(models.Post).all()
    return  users


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    #hash pass - user.password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get('/{id}', response_model=schemas.UserOut)
def get_user(id: int,db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {id} does not exist")
    return user


# @router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int, db: Session = Depends(get_db)):

#     user = db.query(models.User).filter(models.User.id == id)

#     if user.first() == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
#     user.delete(synchronize_session=False)
#     db.commit()

#     return Response(status_code=status.HTTP_204_NO_CONTENT)

