from src.models.conector import Conector
from src.models.controller import Controller
from src.banco.config import config

conector = Conector(config)

controller = Controller(conector)

controller.scrapingUma(105)