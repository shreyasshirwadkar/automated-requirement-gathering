from fastapi import FastAPI
from app.routers import api_routes, auth_routes
from app.dbconfig.init_db import create_database_if_not_exists
from app.dbconfig.database import Base, engine

app = FastAPI()

create_database_if_not_exists()
Base.metadata.create_all(bind=engine)

app.include_router(api_routes.router)
app.include_router(auth_routes.router)