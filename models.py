from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = "postgresql://postgres:admin@localhost:5432/geography_db"


engine = create_engine(DATABASE_URL)
Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    capital = Column(String, nullable=False)
    government_type = Column(String, nullable=False)
    population = relationship("Population", back_populates="state")


class Population(Base):
    __tablename__ = 'populations'

    id = Column(Integer, primary_key=True, index=True)
    male = Column(Integer, nullable=False)
    female = Column(Integer, nullable=False)
    total = Column(Integer, nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="population")
    nationality = relationship("Nationality", back_populates="population")

class Nationality(Base):
    __tablename__ = 'nationalities'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    language = Column(String, nullable=False)
    total_count = Column(Integer, nullable=False)
    population_id = Column(Integer, ForeignKey('populations.id'), nullable=False)
    population = relationship("Population", back_populates="nationality")


Base.metadata.create_all(bind=engine)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
