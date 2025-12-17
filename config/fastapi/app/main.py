from fastapi import FastAPI
from app.routers import statuc_content


app = FastAPI(title='Mapbook API')

app.include_router(static_content.endpoint.router, prefix='/app')