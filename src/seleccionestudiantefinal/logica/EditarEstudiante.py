from src.seleccionestudiantefinal.modelo.declarative_base import engine, Base, session
from src.seleccionestudiantefinal.modelo.Estudiante import Estudiante

class Coleccion():
    def __init__(self):
        Base.metadata.create_all(engine)

    def editar_estudiante(self,idEstudiante, apellidoPaterno, apellidoMaterno, nombres, elegible):
        busqueda = session.query(Estudiante).filter(Estudiante.apellidoPaterno==apellidoPaterno, Estudiante.idEstudiante != idEstudiante).all()
        if len(busqueda)==0:
            estudiante=session.query(Estudiante).filter(Estudiante.idEstudiante==idEstudiante).first()
            estudiante.apellidoPaterno=apellidoPaterno
            estudiante.apellidoMaterno=apellidoMaterno
            estudiante.nombres=nombres
            estudiante.elegible=elegible
            session.commit()
            return True
        else:
            return False


