def insertIntoBruteInfo(url, noticia):
    return f"INSERT INTO NOTICIA (URL, DATA_NOTICIA, HORARIO, DESCRICAO) VALUES ('{url}', '{noticia.data[2]}-{noticia.data[1]}-{noticia.data[0]}', '{noticia.hora}:00', '{noticia.descricao}')"