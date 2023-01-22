import requests
import xml.etree.ElementTree as ET


tree = ET.parse('available.xml')
root = tree.getroot()
lista_moeda = list()

for child in root:
    lista_moeda.append(child.tag)


'''
for child in root:
    dicionario[child.tag] = child.text
    
for k, v in dicionario.items():
    print(k, v)'''


def cota(moeda):
    r = requests.get(f'http://economia.awesomeapi.com.br/json/last/{moeda}')
    return r.json()[moeda.replace('-', '')]['bid']