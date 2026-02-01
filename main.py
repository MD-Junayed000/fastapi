from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.util.init_db import create_tables


@asynccontextmanager
async def lifespan(app : FastAPI):
    # Intializes the db tables when the application starts up
    print("Created")
    create_tables()
    yield # seperation point

app = FastAPI(lifespan=lifespan)

@app.get("/health")
def health_check():
    return {"status":"Running..."}