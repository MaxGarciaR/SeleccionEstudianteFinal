from src.seleccionestudiantefinal.modelo.Asignatura import Asignatura
from src.seleccionestudiantefinal.modelo.Equipo import Equipo
from src.seleccionestudiantefinal.modelo.Actividad import Actividad
from src.seleccionestudiantefinal.modelo.Estudiante import Estudiante, Elegible
from src.seleccionestudiantefinal.modelo.declarative_base import Session, engine, Base

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    session = Session()




