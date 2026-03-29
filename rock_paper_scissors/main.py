from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import random

app = FastAPI()
templates = Jinja2Templates(directory="templates")


def get_result(player, computer):
    if player == computer:
        return "Draw"
    elif (player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock"):
        return "You Win!"
    else:
        return "Computer Wins!"


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/play", response_class=HTMLResponse)
def play(request: Request, player_choice: str = Form(...)):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = get_result(player_choice, computer_choice)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "player_choice": player_choice,
        "computer_choice": computer_choice,
        "result": result,
    })