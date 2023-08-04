<h1 style="text-align: center;">Raspador de Dados</h1>

![a versão atual do projeto é 1.0](https://img.shields.io/badge/Versão-1.0-279)
![feito em python](https://img.shields.io/badge/Linguagem-Python-321)
![utilizado banco mysql](https://img.shields.io/badge/SGBD-MySQL-244)

> Esse é um programa que tem como objetivo retirar de um site de noticias, alguns dados com finalidade didatica. Sendo seu escopo muito restrito a um conjunto pequeno de dados e localidade.

<h2>Primeiros passos</h2>

Primeiro será necessário a instalação das bibliotecas do python utilizado no programa:

```pip install bs4```

```pip install urllib3```

Além disso é necessário a utilização de um SGBD para armazenar os dados recolhidos, o programa em especifico foi criado com especialização no MySQL caso não o possua:

[Baixar MySQL](https://dev.mysql.com/downloads/)

[Baixar Schema](https://drive.google.com/file/d/1uS8QgsvJmK_qcSgdoWqDV3IomUJxpRdm/view?usp=sharing)

<h2>Utilizando o programa</h2>

> No momento o programa não possuí GUI ou utilização de API, então a utilização é através do controller no arquivo app.py

~~~python 
from src.models.conector import Conector
from src.models.controller import Controller
from src.banco.config import config

conector = Conector(config)

controller = Controller(conector)
~~~

Sendo o atual alvo do scraping um site especifico, o controller possuirá duas funções


`controller.scrapingTodas(argumento1, argumento2)`

Argumento 1 = Pagina Inicial (De onde a raspagem se iniciará)
Argumento 2 = Pagina Final (Até que pagina será feito)

Obs: A raspagem é feita de forma descrecente por exemplo: da pagina 302 à 102.

`controller.scrapingUma(pagina)`

pagina = numero da pagina para raspagem

Ao final da raspagem, é criado um objeto Noticia e feito a adição das noticias no banco de dados de maneira a ficarem dessa maneira:

DATA | HORA | DESCRICAO
---- | ---- | --------
2022-08-05 | 08:00 | Foi constatado...