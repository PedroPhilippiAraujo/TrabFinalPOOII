import requests
import json
import qrcode

#04324565000185 - Linha Livre 
#06990590000123 - Google


class Sistema:
    
#Construtor
    
    def __init__(self):
        self.nome = ''
        self.cnpj = ''
        self.situacao = ''
        self.abertura = ''
        self.telefone = ''
        self.logradouro = ''
        self.municipio = '' 
        self.cep = ''
       
#Getters
        
    def GetNome(self):
        return self.nome
    
    def GetCNPJ(self):
        return self.cnpj
    
#Cadastro do Usuario no sistema
    def cadastrar(self,cnpj):
        
        

        url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
        querystring = {"token":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX","cnpj":"06990590000123","plugin":"RF"}
        response = requests.request("GET", url, params=querystring)
    
        resp = json.loads(response.text)
        
        if resp['status'] != 'ERROR':
            logradouro = str(f"{resp['logradouro']}, {resp['bairro']}")
            municipio = str(f"{resp['municipio']}, {resp['uf']}")
        
            self.nome = resp['nome']
            self.cnpj = cnpj
            self.situacao = resp['situacao']
            self.abertura = resp['abertura']
            self.telefone = resp['telefone']
            self.logradouro = logradouro
            self.municipio = municipio 
            self.cep = resp['cep']
        
        else:
            
            print('Cadastro realizado com sucesso')
            

#Pesquisar cadastro de usuários

    def pesquisar(self):
        
        print('Nome: {}\nCNPJ: {}\nSituação Cadastral: {}\nData de Abertura: {}\nTelefone: {}\nEndereço: {}, {}\nCEP: {}'.format(self.nome, self.cnpj, self.situacao, self.abertura, self.telefone, self.logradouro, self.municipio, self.cep))
    
#Criar QR Code do usuario    
    def criarqrcode(self):
        
        data = 'Nome: {}\nCNPJ: {}\nSituação Cadastral: {}\nData de Abertura: {}\nTelefone: {}\nEndereço: {}, {}\nCEP: {}'.format(self.nome, self.cnpj, self.situacao, self.abertura, self.telefone, self.logradouro, self.municipio, self.cep)
        img = qrcode.make(data)
        img.save('QRCode.png')
        
#Funções
        
def funcPesquisa(entrada):
    for user in lista:
        if user.GetCNPJ() == entrada:
            user.pesquisar()
            
def funcQrcode(entrada):
    
    for user in lista:
        if user.GetCNPJ() == entrada:
            user.criarqrcode()
                
def funcDeletar(entrada):
    deletado = False
    
    for pos, user in enumerate(lista):
        if user.GetCNPJ() == entrada:
            lista.pop(pos)
            deletado = True
            
    if deletado == True:
        print("Usuario Deletado com sucesso")
    else:
        print("Usuario não encontrado")


def funcListar():
    listaCNPJS = {}
    for i in lista:
        listaCNPJS[i.GetCNPJ()] = [i.GetNome()]
    
    print(listaCNPJS)


#Declaração de Variaveis
lista = []



#testar
'''
while True:
    x = int(input("1 - Cadastrar \n 2 - Pesquisar \n 3 - QRCode \n 4- Deletar \n 5 - Listar \n 6 - Sair \n Resposta: "))
    
    if x == 1:
        user = Sistema()
        user.cadastrar(input("Digite o CNPJ: "))
        lista.append(user)
        
    elif x == 2:
        entrada = input("Digite o CNPJ: ")
        funcPesquisa(entrada)
        
    elif x == 3:
        entrada = input("Digite o CNPJ: ")
        funcQrcode(entrada)
        
    elif x == 4:
        entrada = input("Digite o CNPJ: ")
        funcDeletar(entrada)
        
    elif x == 5:
        funcListar()
        
    elif x == 6:
        break
'''            