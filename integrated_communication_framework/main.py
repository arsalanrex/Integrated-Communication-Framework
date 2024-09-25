# main.py

import asyncio
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from api.api_manager import router as api_router
from database.db_manager import init_db
from config.settings import Settings

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.on_event("startup")
async def startup_event():
    settings = Settings()
    await init_db(settings.database_url)

@app.get("/", response_class=HTMLResponse)
async def root():
    with open("index.html", "r") as f:
        return f.read()

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    settings = Settings()
    asyncio.run(init_db(settings.database_url))
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)