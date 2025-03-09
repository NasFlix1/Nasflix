from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, Fichier

app = FastAPI()

# 📌 Fonction pour obtenir la session SQLite
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ➕ Ajouter un fichier à la base
@app.post("/ajouter_fichier/")
def ajouter_fichier(nom: str, chemin: str, type: str, db: Session = Depends(get_db)):
    fichier = Fichier(nom=nom, chemin=chemin, type=type)
    db.add(fichier)
    db.commit()
    db.refresh(fichier)
    return {"message": "Fichier ajouté", "fichier": fichier}
