from src.models.conector import Conector
from src.models.controller import Controller

controller = Controller(Conector("teste1"))

controller.diarioPenedense(8, 6)