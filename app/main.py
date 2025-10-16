import os

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Minimal FastAPI TrueNAS App")

templates = Jinja2Templates(directory="app/templates")

# Required environment variables
REQUIRED_VARS = ["APP_VAR1", "APP_VAR2", "APP_VAR3"]


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "title": "Deployed to TrueNAS"}
    )


@app.get("/health")
def health() -> dict[str, str]:
    """Returns the current values of the required environment variables."""
    return {
        "status": "ok",
    }
