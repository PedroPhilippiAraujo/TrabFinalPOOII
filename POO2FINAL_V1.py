import requests
import json

class Usuario:
    
    #Construtor
    def __init__(self,nome,cnpj,situacao,abertura,telefone,logradouro,municipio,cep):
        self.nome = nome
        self.cnpj = cnpj
        self.situacao = situacao
        self.abertura = abertura
        self.telefone = telefone
        self.logradouro = logradouro
        self.municipio = municipio 
        self.cep = cep
    
    #gets
    def get_nome(self):
        return self.nome
    def get_cnpj(self):
        return self.cnpj

    def pesquisar(self):
        print(f"Nome: {self.nome}")
        print(f"CNPJ: {self.cnpj}")
        print(f"Situação Cadastral: {self.situacao}")
        print(f"Data de Abertura: {self.abertura}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.logradouro}, {self.municipio}")
        print(f"CEP: {self.cep}")
        
        
        
#Cadastro do usuário no sistema

def cadastrar():  

    x=int(input('\nQuantidade de CNPJs para cadastro: '))
    while not (1 <= x):
        print('\nQuantidade inválida. Por favor, digite novamente.')
        x=int(input('Quantidade de CNPJs para cadastro: '))
    
    for i in range(1,x+1):
        cnpj = input("Digite o CNPJ para cadastro: ")
        url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
        querystring = {"token":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX","cnpj":"06990590000123","plugin":"RF"}
        response = requests.request("GET", url, params=querystring)
    
        resp = json.loads(response.text)
        
        
        if resp['status'] != 'ERROR':
            logradouro = str(f"{resp['logradouro']}, {resp['bairro']}")
            municipio = str(f"{resp['municipio']}, {resp['uf']}")
        
        
            user = Usuario(resp['nome'],cnpj,resp['situacao'],resp['abertura'],resp['telefone'],logradouro,municipio,resp['cep'])
        
        
            cadastro.append(user)
        else:
            print(resp['message'])
        
        

#Editar dados de usuários previamente cadastrados

def editar():
'''            
    nome=str(input('\nNome: ').upper())
    while (nome == '' or nome == ' ' or nome == '  ' or nome == '   '):
        print("Erro! Dado obrigatório.")
        nome=str(input('Nome: ').upper())

    dia = int(input('Dia de nascimento: '))
    while (dia <= 0):
        print("Erro! Dado obrigatório.")
        dia = int(input('Dia de nascimento: '))

    mes = int(input('Mês de nascimento: '))
    while (mes <= 0):
        print("Erro! Dado obrigatório.")
        mes = int(input('Mês de nascimento: '))
            
            
    ano = int(input('Ano de nascimento: '))
    while (ano <=0):
        print("Erro! Dado obrigatório.")
        ano = int(input('Ano de nascimento: '))
            
    data = Nascimento(dia,mes,ano)
    idade = data.calculo_idade()
    maioridade = data.calculo_maioridade()
           
    sexo = str(input('Como a pessoa define seu gênero?\n 1) Masculino\n 2) Feminino\n 3) Outros\nResposta: '))
    while not (sexo == '1' or sexo == '2' or sexo == '3'):
        print('\nDigite 1, 2 ou 3.')
        sexo = str(input('Como a pessoa define seu gênero?\n 1) Masculino\n 2) Feminino\n 3) Outros\nResposta: '))
    if (sexo == '1'):
        sexo=str('MASCULINO')
    elif (sexo == '2'):
        sexo=str('FEMININO')
    else:
        sexo=str(input('Especifique o gênero da pessoa: ').upper())
                
    nac=str(input('Nacionalidade: ').upper())
    while (nac == '' or nac == ' ' or nac == '  ' or nac == '   '):
        print("Erro! Dado obrigatório.")
        nac =str(input('Nacionalidade: ').upper())
            
    perg=str(input('A pessoa possui dupla nacionalidade?\nResposta: ').upper())
    while not (perg == 'SIM' or perg == 'NÃO' or perg == 'NAO' or perg == 'S' or perg == 'N'):
        print('\nDigite "Sim" ou "Não".')
        perg=str(input('A pessoa possui dupla nacionalidade?\nResposta: ').upper())
            
    if(perg == 'SIM' or  perg == 'S'):
        dupla=str(input('Digite a segunda nacionalidade da pessoa: ').upper())
        if (dupla == "BRASILEIRO") or (dupla == "BRASILEIRA"):
            troca = dupla
            dupla = nac
            nac = troca
    
    
    municipio=str(input('Município de moradia: ').upper())
    while (municipio == '' or municipio == ' ' or municipio == '  ' or municipio == '   '):
        print("Erro! Dado obrigatório.")
        municipio =str(input('Município de moradia: ').upper())
            
    estado=str(input('Estado de moradia: ').upper())
    while (estado == '' or estado == ' ' or estado == '  ' or estado == '   '):
        print("Erro! Dado obrigatório.")
        estado =str(input('Estado de moradia: ').upper())
    

    
    nomemae=str(input('Nome da mãe: ').upper())
    if (nomemae == '' or nomemae == ' ' or nomemae == '  ' or nomemae == '   '):
        nomemae='-1'
                    
    nomepai=str(input('Nome do pai: ').upper())
    if (nomepai == '' or nomepai == ' ' or nomepai == '  ' or nomepai == '   '):
        nomepai='-1'
                
    cpf=str(input('CPF: '))
    if (cpf == '' or cpf == ' ' or cpf == '  ' or cpf == '   '):
        cpf='-1'
                           
    user.set_nome(nome)
    user.set_idade(idade)
    user.set_maioridade(maioridade)
    user.set_sexo(sexo)
    user.set_nacionalidade(nac)
    user.set_endereco(municipio,estado)
    user.set_nomemae(nomemae)
    user.set_nomepai(nomepai)
    user.set_cpf(cpf)
    
    if (perg == 'SIM' or  perg == 'S'):
        user.set_dupla(dupla)
        
    print('\nAlterações salvas com sucesso.')
'''
#Censo
                
def censo():
    '''
    if cadastrofeito == False:
        print("\nErro! Nenhum dado foi cadastrado no sistema. \nPor Favor, cadastre usuários antes de prosseguir.")
        
    else:
        censo=str(input('\nO que você deseja saber?\n 1) Quantidade e percentual de usuários que são maiores de idade\n 2) Quantidade e percentual de usuários que têm o mesmo nome\n 3) Quantidade e percentual de usuários que são brasileiros e que são estrangeiros\n 4) Quantidade e percentual de usuários que não possuem filiação registrada\n 5) Quantidade e percentual de usuários que não possuem CPF registrado\n 6) Voltar\nResposta: '))
        while not (censo == '1' or censo == '2' or censo == '3' or censo == '4' or censo == '5' or censo == '6'):
            print('\nDigite 1, 2, 3, 4, 5 ou 6.')
            censo=str(input('O que você deseja saber?\n 1) Quantidade e percentual de usuários que são maiores de idade\n 2) Quantidade e percentual de usuários que têm o mesmo nome\n 3) Quantidade e percentual de usuários que são brasileiros e que são estrangeiros\n 4) Quantidade e percentual de usuários que não possuem filiação registrada\n 5) Quantidade e percentual de usuários que não possuem CPF registrado\n 6) Voltar\nResposta: '))
    
        if(censo == '1'):
            perc = count = 0
            
            for user in cadastro:
                if (user.get_maioridade() == True):
                    count += 1
                    
            perc = (count*100)/len(cadastro)
            
            
            print('\nQuantidade de usuários maiores de idade: {}'.format(count))
            print('Percentual de usuários maiores de idade: {:.2f}%'.format(perc))
            
        if(censo == '2'):
            perc = count = 0
            
            for user1 in cadastro:
                for user2 in cadastro:
                    if (user1.get_nome() == user2.get_nome()):
                        count += 1
                count-=1
            
            perc = (count*100)/len(cadastro)
            
            print('\nQuantidade de usuários que têm o mesmo nome: {}'.format(count))
            print('Percentual de usuários que têm o mesmo nome: {:.2f}%'.format(perc))
            
        if(censo == '3'):
            perc = bra = est = 0
            
            for user in cadastro:
                if(user.get_nacionalidade() == 'BRASILEIRO' or user.get_nacionalidade() == 'BRASILEIRA'):
                    bra+=1
                else:
                    est+=1
            
            perc = (bra*100)/len(cadastro)
            
            print('\nQuantidade de brasileiros: {}'.format(bra))
            print('Quantidade de estrangeiros: {}'.format(est))
            print('Percentual de brasileiros: {:.2f}%'.format(perc))
            print('Percentual de estrangeiros: {:.2f}%'.format(100-perc))
            
        if(censo == '4'):
            percambos = percpai = percmae = countambos = countpai = countmae = 0
            
            for user in cadastro:
                if(user.get_nomepai() == '-1' and user.get_nomemae() == '-1'):
                    countambos+=1
                elif(user.get_nomepai() == '-1'):
                    countpai+=1
                elif(user.get_nomemae() == '-1'):
                    countmae+=1
                    
            percpai = (countpai*100)/len(cadastro)
            percmae = (countmae*100)/len(cadastro)
            percambos = (countambos*100)/len(cadastro)
            
            print('\nQuantidade de usuários que não possuem paternidade registrada: {}'.format(countpai))
            print('Quantidade de usuários que não possuem maternidade registrada: {}'.format(countmae))
            print('Percentual de usuários que não possuem paternidade registrada: {:.2f}%'.format(percpai))
            print('Percentual de usuários que não possuem maternidade registrada: {:.2f}%'.format(percmae))
            print('Quantidade de usuários que não possuem nem paternidade nem maternidade registrada: {}'.format(countambos))
            print('Percentual de usuários que não possuem nem paternidade nem maternidade registrada: {:.2f}%'.format(percambos))
            
        if(censo == '5'):
            perc = count = 0
            
            for user in cadastro:
                if(user.get_cpf() == '-1'):
                    count+=1
            
            perc = (count*100)/len(cadastro)
            
            print('\nQuantidade de usuários que não possuem CPF registrado: {}'.format(count))
            print('Percentual de usuários que não possuem CPF registrado: {:.2f}%'.format(perc))
        
        if(censo == '6'):
            print('\nVocê voltará para o menu inicial.')
'''
    
#lista de CNPJs cadastrados
def lista():
    
    lista = {}
    
    for user in cadastro:
        lista[user.get_cnpj()] = [user.get_nome()]
        
    for k,v in lista.items():
        print('\nCNPJ: {} Nome: {}'.format(k,v))
        

#Declaração de variáveis
        
cadastro=[]
cadastrofeito = False

#Início do programa

print("Seja bem-vindo!")

while True:

    pergunta=str(input('\nO que você quer fazer?\n 1) Cadastrar\n 2) Pesquisar cadastro\n 3) Editar cadastro\n 4) Deletar cadastro\n 5) Censo\n 6) Lista de CNPJs cadastrados\n 7) Sair\n Resposta: '))
    while not (pergunta == '1' or pergunta == '2' or pergunta == '3' or pergunta == '4' or pergunta == '5' or pergunta == '6' or pergunta == '7'):
        print('\nDigite 1, 2, 3, 4 ou 5.')
        pergunta=str(input('O que você quer fazer?\n 1) Cadastrar\n 2) Pesquisar cadastro\n 3) Editar cadastro\n 4) Deletar cadastro\n 5) Censo\n 6) Lista de RGs cadastrados\n 7) Sair\n Resposta: '))
    
    if (pergunta == '1'):
        cadastrar()
        cadastrofeito = True
        
        
    elif (pergunta == '2'):

        if cadastrofeito == False:
            print("\nErro! Nenhum dado foi cadastrado no sistema. \nPor Favor, cadastre usuários antes de prosseguir.")

        else:
            cnpj=str(input('\nDigite o CNPJ de quem você quer pesquisar: '))
            found = False
            for user in cadastro:
                if (cnpj == user.get_cnpj()):
                    found = True
                    user.pesquisar()
                        
            if found == False:
                print('\nUsuário não cadastrado no sistema.')
                    
                    
    elif (pergunta == '3'):
        if cadastrofeito == False:
            print("\nErro! Nenhum dado foi cadastrado no sistema. \nPor Favor, cadastre usuários antes de prosseguir.")
        
        else:
            rg=str(input("\nDigite o RG da pessoa cujo cadastro você deseja editar: "))
            found = False
            for user in cadastro:
                if (rg == user.get_rg()):
                    found = True
                    editar()
                    
            if found == False:
                print('\nUsuário não cadastrado no sistema.')


    elif (pergunta == '4'):
        if cadastrofeito == False:
            print("\nErro! Nenhum dado foi cadastrado no sistema. \nPor Favor, cadastre usuários antes de prosseguir.")
        
        else:
            cnpj=str(input("\nDigite o cnpj da empresa cujo cadastro você deseja deletar: "))
            found = False
            
            for pos, user in enumerate(cadastro):
                if cnpj == user.get_cnpj():
                    found = True
                    cadastro.pop(pos)
                    print('\nCadastro deletado com sucesso.')         
                    
            if (len(cadastro) == 0):
                cadastrofeito = False
            
            if found == False:
                print('\nUsuário não cadastrado no sistema.')
    
    
    elif (pergunta == '5'):
        censo()
    
    
    elif (pergunta == '6'):
        
        if cadastrofeito == False:
            print("\nErro! Nenhum dado foi cadastrado no sistema. \nPor Favor, cadastre usuários antes de prosseguir.")
        else:
            lista()
      
      
    elif (pergunta == '7'):
        break
    
    
    r=input("\nDeseja continuar? ").upper()
    while not (r == 'SIM' or r == 'NÃO' or r == 'NAO' or r == 'S' or r == 'N'):
        print('\nDigite "Sim" ou "Não".')
        r=str(input("Deseja continuar? ").upper())
    
    if (r == 'NÃO' or r == 'NAO' or r == 'N'):
        break

print("\nFim do programa. Obrigado por utilizar.")