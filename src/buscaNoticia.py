#retorna um dicionario com a data e descricao da noticia

from src.parse.parseDate import parseStringForDateAquiAcontece, parseStringForDateDiarioPenedense
from src.models.noticia import Noticia

def buscarAquiAcontece(soup):
    data = soup.findAll('span', class_= "date")
    data = data[1].text
    texto = soup.find('div', class_="article editorial-text")
    textoNoticia = ''
    for item in texto.findAll('p'):
        textoNoticia += item.text
    return criarNoticiaAquiAcontece(data, textoNoticia)

def buscarDiarioPenedense(soup):
    data = soup.find('span', class_= "date meta-item tie-icon")
    data = data.text
    texto = soup.find('div', class_="entry-content entry clearfix")
    textoNoticia = ''
    for item in texto.findAll('p'):
        textoNoticia += item.text
    return criarNoticiaDiarioPenedense(data, textoNoticia)

def criarNoticiaAquiAcontece(dateTime, descricao):
    dateTime = parseStringForDateAquiAcontece(dateTime)
    noticia = Noticia(dateTime[0], dateTime[1], descricao)
    return noticia

def criarNoticiaDiarioPenedense(dateTime, descricao):
    dateTime = parseStringForDateDiarioPenedense(dateTime)
    noticia = Noticia(data=dateTime[0], descricao=descricao)
    return noticia

def imprimirNoticia(noticia):
    print('-'*10)
    print(f'Ocorreu em: {"-".join(noticia.data)} {noticia.hora}')
    print(f'{noticia.descricao}')
    print('-'*10)
