#retorna um array com todas as noticias daquela pagina
def buscarLinkAquiAcontece(soup):
    array = []
    for item in soup.findAll('div', {"class" : "column column-10 column-xs-8"}):
        array.append(item.h3.a['href'])
    return array

def buscarLinkDiarioPendense(soup):
    array = []
    soupinicial = soup.findAll('h2', {"class" : "post-title"})
    for item in soupinicial:
        array.append(item.a['href'])
    return array
    