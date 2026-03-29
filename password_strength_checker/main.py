from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def check_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()" for c in password)

    if(length<6):
        return "Weak"
    if password.isdigit() or password.isalpha():
        return "Weak"
    if(length>=8 and has_upper and has_lower and has_digit and has_special):
        return "Strong"
    else:
        return "Medium"
    

@app.get("/", response_class=HTMLResponse)
def home(request:Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/check", response_class=HTMLResponse)
def check(request:Request, password: str = Form(...)):
    strength = check_strength(password)
    return templates.TemplateResponse("index.html", {"request":request, "password":password, "strength":strength})

