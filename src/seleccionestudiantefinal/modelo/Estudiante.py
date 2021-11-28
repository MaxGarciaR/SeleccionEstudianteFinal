import enum

from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from .declarative_base import Base

class Elegible(enum.Enum):
    si=1
    no=2

class Estudiante(Base):
    __tablename__='estudiante'

    idEstudiante = Column(Integer, primary_key=True)
    apellidoPaterno = Column(String)
    apellidoMaterno = Column(String)
    nombres = Column(String)
    elegible= Column(Enum(Elegible))
    equipos = relationship ('Equipo', secondary = 'estudiante_equipo',)
    asignaturas = relationship('Asignatura', secondary='asignatura_estudiante',)

class EstudianteEquipo (Base):
    __tablename__= 'estudiante_equipo'

    equipo_id= Column (Integer, ForeignKey('equipo.idEquipo'),primary_key=True)
    estudiante_id= Column (Integer, ForeignKey('estudiante.idEstudiante'),primary_key=True)