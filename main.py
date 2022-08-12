# python -m pip install nomeDoModulo -> Caso dê problema
import os
import time
from functions import imc
import getpass
import database
# from login import cadastrar
import platform

# osClient = platform.system()
# clearCode = ''

# if(osClient == 'Linux'):
#     clearCode = 'clear'
# else:
#     clearCode = 'cls'

def userMenu(isRepeat = False):
    os.system('cls')
    
    if isRepeat:
       opcaoUser = '1'
    else:
        opcaoUser = input("\033[1mCálculo de IMC - Home\033[0m\n\n[1] - Calcular IMC\n[2] - Histórico\n[3] - Análise de Dados\n\n\033[1mUsuário:\033[0m ")
    
    while opcaoUser == '1':
        resultado = imc(6)
        print(resultado)
        input("Pressione qualquer tecla para seguir")
        res = input("[1] - Nova operação\n[2] - Voltar para o menu \n")
        if res == "2":
            opcaoUser = "2"
            userMenu()
        elif res == "1":
            userMenu(True)
        else:
            print("Opção inválida")
            time.sleep(1)
            userMenu()    

def cadastrar(nome, user, dataNasc, senha):
    retorno = database.insert(f"INSERT INTO usuario VALUES (NULL, '{nome}', '{user}', '{dataNasc}', '{senha}')")
    if retorno == 1:
        os.system('cls')
        print('Cadastro realizado com sucesso!')
        time.sleep(2)
        main(False, False)
    else:
        print('Username já é utlizado!')
        time.sleep(2)
        main(False, True)

def entrar(user, senha):
    os.system('cls')
    dados = database.select(f"SELECT username, senha FROM usuario where username = '{user}' and senha = '{senha}'")
    if type(dados) == type(None):
        print("Usuário ou senha inválidos")
        print(type(dados))
        time.sleep(4)
        main(False, False, True)
    else:
        print("Login feito com sucesso")
        time.sleep(2)
        os.system('cls')
        userMenu()
        #chamar menu do usuario


def main(isRepeat = False, isRepeatCad = False, isRepeatLog = False):
    if isRepeat:
        os.system('cls')
    else:
        os.system('cls')
        # nome = input("\033[1mCálculo de IMC\n\nNome:\033[0m ")
        # peso = float(input("\033[1mKG:\033[0m "))
        # altura = float(input("\033[1mAltura: \033[0m"))
        # print(f"{imc(nome, peso, altura)}.\n\n")
        
        if isRepeatCad:
            userInput = "2"
        elif isRepeatLog:
            userInput = "1"
        else:
            userInput = input("\033[1mCálculo de IMC\033[0m\n\n[1] - Entrar\n[2] - Cadastrar\n[3] - Visitante\n\n\033[1mUsuário:\033[0m ")

        if userInput == "1":
            os.system('cls')
            username = input("\033[1mCálculo de IMC - Login\n\nUsername:\033[0m ")
            senha = getpass.getpass('\033[1mSenha:\033[0m ')
            entrar(username, senha)
        elif userInput == "2":
            os.system('cls')
            nome = input("\033[1mCálculo de IMC\033[0m\n\nNome completo: ")
            user = input("Username: ")
            dataNasc = input("Data de nascimento - (AAAA-MM-DD): ")
            senha = getpass.getpass("Senha:")
            confSenha = getpass.getpass("Confirme a senha: ")
            if senha == confSenha:
                cadastrar(nome, user, senha, dataNasc)
            else:
                os.system('cls')
                print("\033[1mCálculo de IMC\033[0m\n\nAs senhas são diferentes")
                time.sleep(3)
                main(False, True)
    
main()


    