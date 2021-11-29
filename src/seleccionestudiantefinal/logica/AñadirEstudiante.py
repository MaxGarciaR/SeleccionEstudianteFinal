from src.seleccionestudiantefinal.modelo.declarative_base import engine, Base, session
from src.seleccionestudiantefinal.modelo.Estudiante import Estudiante

class AñadirEstudiante():
    def __init__(self):
        Base.metadata.create_all(engine)

    def añadir_Estudiante(self, apellidoPaterno, apellidoMaterno, nombres, elegible):
        busqueda = session.query(Estudiante).filter(Estudiante.apellidoMaterno==apellidoPaterno).all()
        if len(busqueda) == 0:
            estudiante = Estudiante(apellidoPaterno=apellidoPaterno, apellidoMaterno=apellidoMaterno,nombres=nombres,elegible=elegible)
            session.add(Estudiante)
            session.commit()
            return True
        else:
            return False
