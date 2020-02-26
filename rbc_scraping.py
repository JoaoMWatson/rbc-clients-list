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

main_info = [[], [], [], [], [], [], [], [], [], [], [], [], []]

contact_info = [[], [], []]

for area in range(0, 15):
    for numAcreditacao in range(1, 1051):
        try:
            url = str("http://www.inmetro.gov.br/laboratorios/rbc/detalhe_laboratorio.asp?num_certificado=" +
                      str(numAcreditacao)+"&situacao=AT&area="+areaAtuacao[area])

            r = requests.get(url)

            soup = BeautifulSoup(r.content, 'html.parser')
            if(soup.title.string == "The page cannot be displayed"):
                pass
            else:
                main_table = soup.find("table", attrs={
                    'width': "60%", "cellspacing": "2", "cellpadding": "2", "border": "0", "align": "center"})
    
                contact_table = main_table.find_next("table", attrs={
                    "width": "60%", "cellspacing": "2", "cellpadding": "2", "align": "center"})
    
                main_lines = main_table.find_all("td", attrs={"class": "size11"})
    
                contact_lines = contact_table.find_all(
                    "td", attrs={"class": "size11"})
    
                for i in range(4, 14):
                    try:
                        main_info[i-4].append(main_lines[i].b.string)
                    except AttributeError:
                        main_info[i-4].append(main_lines[i].string)
    
                for i in range(0, 3):
                    try:
                        contact_info[i].append(contact_lines[i].a.string)
                    except AttributeError:
                        contact_info[i].append(contact_lines[i].string)
    
                print(f"\nArea de atuação: {areaAtuacao[area]}")
                print(f"\nNumero Acreditação: {numAcreditacao}")

        except Exception as e:
            print(e)
            pass

        finally:
            r.close()

data = {"Razão Social": main_info[0], "Nome do Laboratório": main_info[1], "Situação": main_info[2],
              "Endereço": main_info[3], "Bairro": main_info[4], "CEP": main_info[5], 
              "Cidade": main_info[6], "UF": main_info[7], "Telefone": main_info[8], 
              "Fax": main_info[9], "Grupo de Serviço de Calibração": contact_info[0],
              "Gerente tecnico": contact_info[1], "Email": contact_info[2]}

dataFrame = pd.DataFrame(data)

dataFrame.to_csv(r'~/git/webscraping-rbc/contatosLaboratorios.csv')