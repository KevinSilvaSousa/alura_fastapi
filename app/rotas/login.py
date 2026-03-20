from typing import Annotated
from fastapi import APIRouter, Depends, Form
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from app.dependencias import obter_cliente_repositorio

router = APIRouter(
    prefix="/login"
)

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def pagina_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/")
async def login(request: Request, email=Form(...), senha = Form(...)):
    if email == "admin@techlog.com.br" and senha == "senha123":
       response = RedirectResponse (url="/", status_code=303)
       response.set_cookie(key="session_token", value="token-senha", httponly=True)

       return response