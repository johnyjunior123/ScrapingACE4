import sys
sys.path.insert(0, "../")

from src.buscaNoticia import buscarAquiAcontece
from src.requisicao import requisicao
from src.buscaPagina import buscarLinkAquiAcontece
from src.banco.inserts import insertIntoBruteInfo

class Controller:

    def __init__(self, conector):
        self.conector = conector


    def testeInsert(self, url):
        noticia = buscarAquiAcontece(requisicao(url))
        self.conector.executarSQL(insertIntoBruteInfo(url,noticia))

    def scrapingUma(self, pagina):
        url = f"https://aquiacontece.com.br/noticias/editoria/policial/arquivo?page={pagina}"
        links = buscarLinkAquiAcontece(requisicao(url))
        for i in range(0,10):
            noticia = buscarAquiAcontece(requisicao(links[i]))
            self.conector.executarSQL(insertIntoBruteInfo(links[i],noticia))
    
    def scrapingTodas(self, paginainicio, paginafinal):
        while paginainicio >= paginafinal:
            url = f"https://aquiacontece.com.br/noticias/editoria/policial/arquivo?page={paginainicio}"
            links = buscarLinkAquiAcontece(requisicao(url))
            for i in range(0,10):
                noticia = buscarAquiAcontece(requisicao(links[i]))
                self.conector.executarSQL(insertIntoBruteInfo(links[i],noticia))
            paginainicio -= 1

