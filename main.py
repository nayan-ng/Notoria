from dotenv import load_dotenv
load_dotenv()


from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.note import note


app = FastAPI()

app.mount(
    path="/static",
    app=StaticFiles(directory="static"),
    name="static"
)

app.include_router(note)
