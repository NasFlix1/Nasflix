from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# 📌 Connexion à SQLite
DATABASE_URL = "sqlite:///nas_search.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# 📂 Création de la session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 🎮 Table pour stocker les fichiers
class Fichier(Base):
    __tablename__ = "fichiers"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)
    chemin = Column(String)
    type = Column(String)

# 🛠 Création des tables
Base.metadata.create_all(bind=engine)
