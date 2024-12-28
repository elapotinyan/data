from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import SessionLocal, State, Population, Nationality
from schemas import StateCreate, State as StateSchema, PopulationCreate, Population as PopulationSchema, NationalityCreate, Nationality as NationalitySchema

app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/states/", response_model=StateSchema)
def create_state(state: StateCreate, db: Session = Depends(get_db)):
    db_state = State(**state.dict())
    db.add(db_state)
    db.commit()
    db.refresh(db_state)
    return db_state

@app.get("/states/", response_model=list[StateSchema])
def get_states(db: Session = Depends(get_db)):
    return db.query(State).all()

