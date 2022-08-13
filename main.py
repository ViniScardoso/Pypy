# python -m pip install nomeDoModulo -> Caso dê problema
import os
import time
from functions import historico, imc
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

def userMenu(userId, isRepeat = False):
    os.system('cls')

    if isRepeat:
       opcaoUser = '1'
    else:
        opcaoUser = input("\033[1mCálculo de IMC - Home\033[0m\n\n[1] - Calcular IMC\n[2] - Histórico\n[3] - Análise de Dados\n\n\033[1mUsuário:\033[0m ")
    
    while opcaoUser == '1':
        resultado = imc(userId)
        print(resultado)
        input("\nPressione qualquer tecla para seguir...")
        os.system('cls')
        res = input("\033[1mCálculo de IMC - Tarefa Finalizada\033[0m\n\n[1] - Voltar para a home\n[2] - Nova operação\n\n\033[1mUsuário:\033[0m ")
        
        if res == "1":
            opcaoUser = "0"
            userMenu(userId)
        elif res == "2":
            userMenu(userId, True)
        else:
            print("Opção inválida")
            time.sleep(1)
            userMenu(userId)
    
    while opcaoUser == "2":
        os.system('cls')
        dados = historico(userId)
        for i in dados:
            print(dados[0], dados[1])

        input("Pressione qualquer tecla para voltar ao menu...")
        opcaoUser == "0"
        userMenu(userId)

def cadastrar(nome, user, dataNasc, senha):
    retorno = database.insert(f"INSERT INTO usuario VALUES (NULL, '{nome}', '{user}', '{dataNasc}', '{senha}')")
    if retorno == 1:
        os.system('cls')
        print('\033[1mCálculo de IMC - Cadastro\033[0m\n\nCadastro realizado com sucesso!')
        time.sleep(2)
        main(False, False)
    else:
        print('Username já é utlizado!')
        time.sleep(2)
        main(False, True)

def entrar(user, senha):
    os.system('cls')
    dados = database.select(f"SELECT idUsuario, username, nome FROM usuario where username = '{user}' and senha = '{senha}'")
    if type(dados) == type(None):
        print("\033[1mCálculo de IMC - Falha no Login\033[0m\n\nUsuário ou senha inválidos")
        time.sleep(4)
        main(False, False, True)
    else:
        print("\033[1mCálculo de IMC - Sucesso no Login\033[0m\n\nLogin feito com sucesso, Redirecionando para o menu inicial ...")
        userId = dados[0]
        time.sleep(2)
        os.system('cls')
        userMenu(userId)
        #chamar menu do usuario


def main(isRepeat = False, isRepeatCad = False, isRepeatLog = False):
    if isRepeat:
        os.system('cls')
    else:
        os.system('cls')
        
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
            nome = input("\033[1mCálculo de IMC - Cadastro\033[0m\n\nNome completo: ")
            user = input("Username: ")
            dataNasc = input("Data de nascimento(AAAA-MM-DD): ")
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


    