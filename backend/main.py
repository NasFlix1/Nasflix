# backend/main.py
from fastapi import FastAPI
from routers import media
import databases
import sqlalchemy

DATABASE_URL = "sqlite:///./nasflix.db"  # Remplace par PostgreSQL si nécessaire
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

app = FastAPI(title="Nasflix API")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Inclure les routes pour gérer les médias
app.include_router(media.router)

@app.get("/")
def home():
    return {"message": "Bienvenue sur Nasflix"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

