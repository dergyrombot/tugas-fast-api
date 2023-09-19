from sqlalchemy.orm.session import Session
from db.models import DbBuku
from schemas import BukuDisplay

def create_buku(db: Session, request: BukuDisplay):
  new_buku = DbBuku(
    nama = request.nama,
    penerbit = request.penerbit,
    penulis = request.penulis
    )
  db.add(new_buku)
  db.commit()
  db.refresh(new_buku)
  return new_buku

def get_buku(db: Session, id: int):
  buku = db.query(DbBuku).filter(DbBuku.id == id).first()
  # Handle errors
  return buku