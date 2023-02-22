from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from mangum import Mangum
from os import getenv
from .summarizers.routers import router as summarizer_router
from .search.routers import router as search_router
from app.search2.routers import router as search2_router

app = FastAPI(debug=getenv("DEBUG", False))

@app.get("/livez/")
async def live():
    return "Chathitilla.."

app.include_router(summarizer_router, tags=["summarizer"])
app.include_router(search_router, prefix="/search", tags=["search"])
app.include_router(search2_router, prefix="/search2", tags=["search", "new"])

app.mount("/", StaticFiles(directory="ui", html=True), name="ui")

handler = Mangum(app)
