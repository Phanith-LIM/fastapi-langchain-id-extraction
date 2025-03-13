from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from modules.gemini.controller import router as gemini_router
app = FastAPI(
    docs_url="/",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(gemini_router)
