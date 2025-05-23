from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.features.summarization.routes.summarize import router as summarize_router

app = FastAPI()

# Mount the summarize router
app.include_router(summarize_router, prefix="/summarize")

# CORS middleware to allow frontend-backend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all domains (for dev only)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "AI Study Assistant Backend Running"}
