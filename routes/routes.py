from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from database import Session, engine
from repository.models import Note
from schemas.schemas import NotePydanticIn, NotePydanticOut

router = APIRouter(prefix='/api')
db = Session(bind=engine)


@router.get('/', response_class=JSONResponse)
def get_notes():
    notes = db.query(Note).all()
    if(notes):
        return notes
    return JSONResponse({'message': 'not found'}, status_code=status.HTTP_404_NOT_FOUND)


@router.get('/{id}', response_class=JSONResponse)
def get_note(id:int):
    note = db.query(Note).filter(Note.id==id).first()
    if(note):
        return note
    return JSONResponse({'message': 'not found'}, status_code=status.HTTP_404_NOT_FOUND)


@router.post('/new')
async def new_note(note:NotePydanticIn):
    new_note = Note(**note.model_dump())
    db.add(new_note)
    db.commit()
    return note.model_dump()


@router.put('/{id}')
async def update_note(id:int, note: NotePydanticIn):
    new_note = db.query(Note).filter(Note.id == id).first()
    new_note.title = note.title
    new_note.description = note.description
    db.commit()
    return {'id':id, **note.model_dump()}


@router.delete('/{id}')
async def delete_note(id:int):
    note = db.query(Note).filter(Note.id == id).first()
    if note:
        db.delete(note)
        db.commit()
        return {'message':'deleted'}
    return JSONResponse({'message':'not found'}, status_code=status.HTTP_404_NOT_FOUND)
    
