from src.models.conector import Conector
from src.models.controller import Controller

controller = Controller(Conector("teste"))

controller.aquiAcontece(6, 6)