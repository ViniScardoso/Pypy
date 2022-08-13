# python -m pip install nomeDoModulo -> Caso dê problema
import os
import time
from functions import historico, imc
import getpass
import database
import platform
import locale
from analytics import getFaixaEtaria
locale.setlocale(locale.LC_ALL, 'pt_pt.UTF-8')

# clearCode = 'clear' if platform.system() == 'Linux' else 'cls'

def userMenu(userId, isRepeat = False):
    os.system('cls')

    if isRepeat:
       opcaoUser = '1'
    else:
        opcaoUser = input("\033[1mCálculo de IMC - Home\033[0m\n\n[1] - Calcular IMC\n[2] - Histórico\n[3] - Análise de Dados\n[4] - Voltar\n\n\033[1mUsuário:\033[0m ")
    
    while opcaoUser == '1':
        resultado = imc(userId)
        print(resultado)
        input("\nPressione qualquer tecla para seguir...")
        os.system('cls')
        res = input("\033[1mCálculo de IMC - Tarefa Finalizada\033[0m\n\n[1] - Calcular IMC novamente\n[2] - Voltar\n\n\033[1mUsuário:\033[0m ")
        
        if res == "1":
            userMenu(userId, True)
        elif res == "2":
            opcaoUser = "0"
            userMenu(userId)
        else:
            print("Opção inválida")
            time.sleep(1)
            userMenu(userId)
    
    while opcaoUser == "2":
        os.system('cls')
        print("\033[1mCálculo de IMC - Histórico\033[0m\n")
        dados = historico(userId)
        
        for i in dados:
            print(f"\033[1m{i[4].strftime('%A').capitalize()}, {i[4].strftime('%d')} de {i[4].strftime('%B')} de {i[4].strftime('%Y')}\033[0m")
            print(f"\033[1mHorário: \033[0m{i[4].strftime('%H')}:{i[4].strftime('%M')}")
            print(f"\033[1mPeso: \033[0m{i[1]}kg")
            print(f"\033[1mAltura: \033[0m{i[2]}m")
            print(f"\033[1mIMC: \033[0m{i[3]}\n")

        input("Pressione qualquer tecla para voltar ao menu...")
        opcaoUser == "0"
        userMenu(userId)

    while opcaoUser == "3":
        os.system('cls')
        res = input("\033[1mCálculo de IMC - Análise de Dados\033[0m\n\n[1] - IMC por faixa etária\n[2] - IMC por faixa corporal\n[3] - IMC por estatura física\n[4] - Personalizado\n[5] - Voltar\n\n\033[1mUsuário: \033[0m")
        
        if res == "1":
            getFaixaEtaria('teste')
        elif res == "5":
            userMenu(userId)

        input("Pressione qualquer tecla para voltar ao menu...")
        opcaoUser == "0"
        userMenu(userId)

    while opcaoUser == "4":
        main()

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
        main(isRepeatLog = True)
    else:
        print("\033[1mCálculo de IMC - Sucesso no Login\033[0m\n\nLogin feito com sucesso\nDirecionando para o menu inicial...")
        userId = dados[0]
        time.sleep(2)
        os.system('cls')
        userMenu(userId)

def main(isRepeatCad = False, isRepeatLog = False):
    os.system('cls')
    
    if isRepeatLog:
        userInput = "1"
    elif isRepeatCad:
        userInput = "2"
    else:
        userInput = input("\033[1mCálculo de IMC\033[0m\n\n[1] - Entrar\n[2] - Cadastrar\n[3] - Visitante\n[4] - Sair\n\n\033[1mUsuário:\033[0m ")

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
            main(isRepeatCad = True)
    elif userInput == '3':
        print(imc(userId = None, isLogado = False))
        input("\nPressione qualquer tecla para continuar...")
        main()
    elif userInput == '4':
        os.system('cls')
        print('Foi bom o tempo que passamos juntos ♡\n')
        time.sleep(4)
        os.system('cls')
        exit()

main()