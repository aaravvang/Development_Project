from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get("/")
def home(request:Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/convert",response_class=HTMLResponse)
async def convert(request:Request,temp_c: float = Form(...)):
    temp_f = (temp_c*(9/5))+32
    return templates.TemplateResponse("index.html",{"temperature_fahrenheit": temp_f, "request": request})