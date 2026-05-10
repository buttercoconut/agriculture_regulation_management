# main application
from fastapi import FastAPI
from .routes import regulation
from .database import init_db

app = FastAPI(title="Agriculture Regulation Management API")

@app.on_event("startup")
async def startup_event():
    init_db()

app.include_router(regulation.router)

# Additional routers can be included here
