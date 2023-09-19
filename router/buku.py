from typing import List
from schemas import BukuBase, BukuDisplay, UserBase
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_buku


router = APIRouter(
  prefix='/buku',
  tags=['buku']
)

# Create article
@router.post('/', response_model=BukuDisplay)
def create_buku(request: BukuBase, db: Session = Depends(get_db)):
  return db_buku.create_buku(db, request)

# Get specific article
@router.get('/{id}') #, response_model=BukuDisplay)
def get_buku(id: int, db: Session = Depends(get_db)):
  return {
    'data': db_buku.get_buku(db, id)
  }

