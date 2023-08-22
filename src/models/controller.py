import sys 
index = sys.path[0].split('\\').index('ScrapingACE4')
path = "\\".join(sys.path[0].split('\\')[0:index+1])
sys.path.insert(0, path)

from src.requisicao import requisicao
from src.buscaNoticia import buscarAquiAcontece
from src.buscaPagina import buscarLinkAquiAcontece
from src.banco.inserts import insertIntoBruteInfo

class Controller:

    def __init__(self, conector):
        self.conector = conector

    def aquiAcontece(self, paginainicio, paginafinal):
        while paginainicio >= paginafinal:
            url = f"https://aquiacontece.com.br/noticias/editoria/policial/arquivo?page={paginainicio}"
            links = buscarLinkAquiAcontece(requisicao(url))
            for i in range(0,10):
                noticia = buscarAquiAcontece(requisicao(links[i]))
                self.conector.executarSQL(insertIntoBruteInfo(links[i],noticia))
            paginainicio -= 1