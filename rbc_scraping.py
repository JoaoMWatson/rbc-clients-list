import requests
import time
import json
import pandas as pd
from bs4 import BeautifulSoup


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
            # url = str("http://www.inmetro.gov.br/laboratorios/rbc/detalhe_laboratorio.asp?num_certificado=" +
            #           str(numAcreditacao)+"&situacao=AT&area="+areaAtuacao[i])

            url = "http://www.oconsumidor.gov.br/laboratorios/rbc/detalhe_laboratorio.asp?num_certificado=461&situacao=AT&area=ELETRICIDADE%20E%20MAGNETISMO"

            r = requests.get(url)

            soup = BeautifulSoup(r.content, 'html.parser')

            mainTable = soup.find("table", attrs={
                                  'width': "60%", "cellspacing": "2", "cellpadding": "2", "border": "0", "align": "center"})

            contactTable = soup.find("table", attrs={"width"="60%", "cellspacing": "2", "cellpadding": "2", "align": "center"})

        except Exception as e:
            print(e)

        finally:
            r.close()
