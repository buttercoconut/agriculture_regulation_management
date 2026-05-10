from fastapi import FastAPI
from .routes import regulation, notification

app = FastAPI(title="Agriculture Regulation Management API")

app.include_router(regulation.router, prefix="/regulations", tags=["Regulations"])
app.include_router(notification.router, prefix="/notifications", tags=["Notifications"])

# Health check
@app.get("/health")
async def health_check():
    return {"status": "ok"}
