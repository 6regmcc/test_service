import os
from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import FastAPI, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from db_connection import db_create_all, get_db
from model import Note
from schema import CreateNote
import os
from dotenv import load_dotenv
load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_create_all()
    print("Creating/Updating db tables")
    print(f'Current env is {os.environ.get("ENVIRONMENT")}')
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/create_note")
def create_note(note_data:CreateNote, db: Annotated[Session, Depends(get_db)]):
    note = Note(**note_data.model_dump())
    db.add(note)
    db.commit()
    db.refresh(note)
    return note


@app.get("/notes")
def get_notes(db: Annotated[Session, Depends(get_db)]):
    notes = db.scalars(select(Note)).all()
    return_notes = [{**note.to_dict()} for note in notes]
    return return_notes


@app.get("/hello")
def hello():
    return {"hello": "I am test_service"}