from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .declarative_base import Base

class Actividad(Base):
    __tablename__ = 'actividad'

    idActividad = Column(Integer, primary_key=True)
    denominacionActividad = Column(String)
    fecha = Column(String)
    equipo = Column (Integer, ForeignKey('equipo.idEquipo'))