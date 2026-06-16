from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker, Session
import os
from dotenv import load_dotenv

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/produtos")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Produto(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    estoque = Column(Integer, default=0)
    ativo = Column(Boolean, default=True)

Base.metadata.create_all(bind=engine)

class ProdutoCreate(BaseModel):
    nome: str = Field(min_length=1)
    preco: float = Field(gt=0)
    estoque: int = 0
    ativo: bool = True

class ProdutoOut(ProdutoCreate):
    id: int
    class Config:
        from_attributes = True

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/produtos", response_model=list[ProdutoOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Produto).all()




@app.post("/produtos", response_model=ProdutoOut, status_code=status.HTTP_201_CREATED)
def criar(produto: ProdutoCreate, db: Session = Depends(get_db)):
    novo = Produto(**produto.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@app.get("/produtos/{id}", response_model=ProdutoOut)
def buscar(id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@app.delete("/produtos/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar(id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    db.delete(produto)
    db.commit()

@app.put("/produtos/{id}", response_model=ProdutoOut)
def atualizar(
    id: int,
    dados: ProdutoCreate,
    db: Session = Depends(get_db)
):
    produto = db.query(Produto).filter(
        Produto.id == id
    ).first()

    if not produto:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

    produto.nome = dados.nome
    produto.preco = dados.preco
    produto.estoque = dados.estoque
    produto.ativo = dados.ativo

    db.commit()
    db.refresh(produto)

    return produto