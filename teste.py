import requests
import time
import json
import pandas as pd
from bs4 import BeautifulSoup


url = "http://www.oconsumidor.gov.br/laboratorios/rbc/detalhe_laboratorio.asp?num_certificado=461&situacao=AT&area=ELETRICIDADE%20E%20MAGNETISMO"

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

mainTable = soup.find("table", attrs={
                      'width': "60%", "cellspacing": "2", "cellpadding": "2", "border": "0", "align": "center"})

contactTable = mainTable.find_next("table", attrs={
                         "width": "60%", "cellspacing": "2", "cellpadding": "2", "align": "center"})

print(mainTable)
print(contactTable)

r.close()
