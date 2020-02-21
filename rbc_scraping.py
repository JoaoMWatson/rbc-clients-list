import requests
import time
import json
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

count = 0

areaAtuacao = ["ELETRICIDADE E MAGNETISMO",
               "RADIA%C7%D5ES%20IONIZANTES", "AC%DASTICA%2"+"0E%20VIBRA%C7%D5ES",
               "ALTA%2"+"0FREQU%CANCIA%2"+"0E%20TELECOMUNICA%C7%D5ES", "DIMENSIONAL",
               "F%CDSICO-QU%CDMICA", "FOR%C7A,%20TORQUE%20"+"E%2"+"0%20DUREZA",
               "MASSA", "%D3PTICA", "PRESS%C3O", "TEMPERATURA E UMIDADE",
               "TEMPO%20"+"E%20"+"FREQU%CANCIA", "VAZ%C3O%2" +
               "0E%20VELOCIDADE%20DE%2"+"0FLUIDOS",
               "VISCOSIDADE", "VOLUME%2"+"0E%20MASSA%2"+"0ESPEC%CDFICA"]


for i in range(0, 15):
    for numAcreditacao in range(1, 1051):
        try:
            url = str("http://www.inmetro.gov.br/laboratorios/rbc/detalhe_laboratorio.asp?num_certificado=" +
                      str(numAcreditacao)+"&situacao=AT&area="+areaAtuacao[i])

            session = requests.session()

            print("\n Ta abrindo", numAcreditacao)
            response = session.get(url)
            print("\n Abriu", numAcreditacao)
            soup = BeautifulSoup(response.text, 'html.parser')

        except Exception as e:
            print(e)
            
        finally:
            response.close()

print("Acabou")
