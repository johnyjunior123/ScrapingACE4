# modulo para tratamento do campo data recebido do scraping
def parseStringForDate(data):
    datetime = data.split(' - ')
    datetime[0] = datetime[0].split(' ')
    datetime[0][1] = parseMounth(datetime[0][1])
    #datetime[0] = "-".join(datetime[0]) retirado temporariamente para poder efetuar o insert no banco mais facilmente
    return datetime

def parseMounth(mounth):
    mounthInPortuguese = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                            'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    return '0' + str(mounthInPortuguese.index(mounth)+1)
