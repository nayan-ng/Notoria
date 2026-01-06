from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.status import HTTP_303_SEE_OTHER
from bson import ObjectId

from config.db import conn
from schemas.note import notesEntity

note = APIRouter()
templates = Jinja2Templates(directory="templates")



@note.get("/", response_class=HTMLResponse)
async def home(request: Request):
    docs = conn.notedb.notes.find()
    newDocs = notesEntity(docs)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "newDocs": newDocs
    })



@note.post("/")
async def add_note(
    title: str = Form(...),
    desc: str = Form(...),
    important: str = Form(None)
):
    conn.notedb.notes.insert_one({
        "title": title,
        "desc": desc,
        "important": True if important else False
    })

    return RedirectResponse("/", status_code=HTTP_303_SEE_OTHER)
