import pathlib
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

BASE_DIR = pathlib.Path(__file__).parent

app = FastAPI()
template = Jinja2Templates(directory=BASE_DIR / "templates")

@app.get("/", response_class=HTMLResponse)
def home_view(request: Request):
    return template.TemplateResponse("home.html", {"request": request})

@app.post("/")
def home_detail_view():
    return {"message": "Hello, World!"}
