from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Minimal FastAPI TrueNAS App")

templates = Jinja2Templates(directory=Path(__file__).parent / "templates")


@app.get("/", response_class=HTMLResponse)
def index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        "index.html", {"request": request, "title": "Buecherhallen Scraper"}
    )


@app.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "ok",
    }
