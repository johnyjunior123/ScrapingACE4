def insertIntoBruteInfo(url, noticia):
    if(url.find('diariopenedense')):
        return f"INSERT INTO NOTICIA (URL, DATA_NOTICIA, DESCRICAO) VALUES ('{url}', '{noticia.data[2]}-{noticia.data[1]}-{noticia.data[0]}', '{noticia.descricao}')"
    return f"INSERT INTO NOTICIA (URL, DATA_NOTICIA, HORA, DESCRICAO) VALUES ('{url}', '{noticia.data[2]}-{noticia.data[1]}-{noticia.data[0]}', '{noticia.hora}:00', '{noticia.descricao}')"


url = 'google.com.br'
print(url.find('1'))
