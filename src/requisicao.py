from src.util import eliminarLixo
from urllib3 import request
from bs4 import BeautifulSoup

# faz as requisições e retorna um objeto soup para as outras funções
def requisicao(url):
    req = request('GET', url)
    html = req.data.decode('utf-8')
    html = eliminarLixo(html)
    return transformarEmSoup(html)

def transformarEmSoup(html):
    return BeautifulSoup(html, 'html.parser')