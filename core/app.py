from fastapi import FastAPI

from api.bonds import router

app = FastAPI(title="Bond Portfolio API")

app.include_router(router)
