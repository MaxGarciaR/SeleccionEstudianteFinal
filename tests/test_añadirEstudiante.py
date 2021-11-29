from faker import Faker
import random
import unittest
from src.seleccionestudiantefinal.logica.AñadirEstudiante import AñadirEstudiante
from src.seleccionestudiantefinal.modelo.Estudiante import Estudiante, Elegible
from src.seleccionestudiantefinal.modelo.declarative_base import Session

class AñadirEstudianteTestCase(unittest.TestCase):
    def setUp(self):
        self.AñadirEstudiante = AñadirEstudiante()

        self.session = Session()

        self.data_factory = Faker ()

        self.seed (1000)

        self.data = [ ]
        self.añaEstudiante=[ ]
        self.elegible = [Elegible.si, Elegible.no]
        for i in range (0,10):
            self.data.append((
                self.data_factory.unique.name( ),
                self.data_factory.unique.name( ),
                self.data_factory.unique.name( ),
                random.choice (self.elegible)))
            self.añaEstudiante.append(
                Estudiante(
                    apellidoPaterno = self.data[-1][0],
                    apellidoMaterno = self.data[-1][1],
                    nombres = self.data[-1][2],
                    elegibles = self.data[-1][3],
                    equipos = [],
                    asignaturas = [],
                ))
            self.session.add (self.añaEstudiante[-1])

        self.session.commit()

