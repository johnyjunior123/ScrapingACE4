from src.models.conector import Conector
from src.models.controller import Controller
from src.banco.config import config

controller = Controller(Conector())

controller.scrapingUma(105)