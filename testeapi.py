import requests
import json

def consulta(cnpj):
    
    url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
    querystring = {"token":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX","cnpj":"06990590000123","plugin":"RF"}
    response = requests.request("GET", url, params=querystring)
    
    resp = json.loads(response.text)
    
    print(resp['nome'])
    
 
entrada = input("digite o cnpj")
consulta(entrada)
