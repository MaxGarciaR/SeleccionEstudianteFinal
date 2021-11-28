from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .declarative_base import Base

class Asignatura(Base):
    __tablename__ = 'asignatura'

    idAsignatura = Column (Integer, primary_key=True)
    nombreAsignatura = Column (String)
    estudiant = relationship ('Estudiante', secondary = 'asignatura_estudiante',)


class AsignaturaEstudiante (Base):
    __tablename__ = 'asignatura_estudiante'

    estudiante_id = Column (Integer, ForeignKey('estudiante.idEstudiante'), primary_key=True)
    asignatura_id = Column (Integer, ForeignKey('asignatura.idAsignatura'), primary_key=True)