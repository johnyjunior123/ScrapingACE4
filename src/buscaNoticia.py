#retorna um dicionario com a data e descricao da noticia

from src.parse.parseDate import parseStringForDate
from src.models.noticia import Noticia

def buscarAquiAcontece(soup):
    data = soup.findAll('span', class_= "date")
    data = data[1].text
    texto = soup.find('div', class_="article editorial-text")
    textoNoticia = ''
    for item in texto.findAll('p'):
        textoNoticia += item.text
    return criarNoticia(data, textoNoticia)

def criarNoticia(dateTime, descricao):
    dateTime = parseStringForDate(dateTime)
    noticia = Noticia(dateTime[0], dateTime[1], descricao)
    return noticia

def imprimirNoticia(noticia):
    print('-'*10)
    print(f'Ocorreu em: {"-".join(noticia.data)} {noticia.hora}')
    print(f'{noticia.descricao}')
    print('-'*10)