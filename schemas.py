from pydantic import BaseModel

class StateBase(BaseModel):
    name: str
    capital: str
    government_type: str

class StateCreate(StateBase):
    pass

class State(StateBase):
    id: int

    class Config:
        orm_mode = True


class PopulationBase(BaseModel):
    male: int
    female: int
    total: int
    state_id: int

class PopulationCreate(PopulationBase):
    pass

class Population(PopulationBase):
    id: int

    class Config:
        orm_mode = True


class NationalityBase(BaseModel):
    name: str
    language: str
    total_count: int
    population_id: int

class NationalityCreate(NationalityBase):
    pass

class Nationality(NationalityBase):
    id: int

    class Config:
        orm_mode = True
