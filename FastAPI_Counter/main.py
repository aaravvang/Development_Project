from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")

app = FastAPI()

# Request body model
global counter
counter = 0

@app.get('/')
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get('/counter')
def count():
    return {"counter": counter}

@app.post('/increment')
def increment():
    global counter
    counter = counter+1
    return {"counter": counter}

@app.post('/decrement')
def decrement():
    global counter
    counter = counter-1
    return {"counter": counter}

@app.post('/reset')
def reset():
    global counter
    counter = 0
    return {"counter": counter}

