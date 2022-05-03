from fastapi import FastAPI, HTTPException, status
from .schema import*
from .models import*
from .database import session, Base, engine

Base.metadata.create_all(engine)

app = FastAPI()


@app.get('/')
def root():
    return 'MY_TODO'


@app.post('/my_todo')
def create_todo(request: valid):
    to_create = table(task=request.task)
    session.add(to_create)
    session.commit()
    id = to_create.id
    session.close()
    return f'created todo item with id {id}'


@app.put('/my_todo/{id}')
def update_todo(id: int, task: str):
    to_update = session.query(table).get(id)
    if to_update:
        to_update.task = task
        session.commit()

    session.close()

    if not to_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'todo item with id {id} not found')
    return to_update


@app.get('/my_todo/{id}')
def get_by_id(id: int):
    get_id = session.query(table).get(id)
    session.close()
    if not get_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'todo item with id {id} not found')
    return get_id


@app.get('/my_todo')
def todo_list():
    get_list = session.query(table).all()
    session.close()
    return get_list


@app.delete('/my_todo/{id}')
def delete_todo(id: int):
    to_delete = session.query(table).get(id)
    if to_delete:
        session.delete(to_delete)
        session.commit()
        session.close()
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'todo item with id {id} not found')

    return f'item by id {id} deleted successfully'
