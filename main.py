# python -m pip install nomeDoModulo -> Caso dê problema
import os
import time
from functions import historico, imc
import getpass
import database
import platform
import locale
from analytics import getAnalise, getAnalisePersonalizada
locale.setlocale(locale.LC_ALL, 'pt_pt.UTF-8')

# clearCode = 'clear' if platform.system() == 'Linux' else 'cls'

def userMenu(userId, isRepeat = False):
    os.system('cls')

    if isRepeat:
       opcaoUser = '1'
    else:
        opcaoUser = input("\033[1mPypy - Home\033[0m\n\n[1] - Calcular IMC\n[2] - Histórico\n[3] - Análise de Dados\n[4] - Voltar\n\n\033[1mUsuário:\033[0m ")
    
    while opcaoUser == '1':
        resultado = imc(userId)
        print(resultado)
        input("\nPressione enter tecla para seguir...")
        os.system('cls')
        res = input("\033[1mPypy - Tarefa Finalizada\033[0m\n\n[1] - Calcular IMC novamente\n[2] - Voltar\n\n\033[1mUsuário:\033[0m ")
        
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
        print("\033[1mPypy - Histórico\033[0m\n")
        dados = historico(userId)
        
        for i in dados:
            print(f"\033[1m{i[4].strftime('%A').capitalize()}, {i[4].strftime('%d')} de {i[4].strftime('%B')} de {i[4].strftime('%Y')}\033[0m")
            print(f"\033[1mHorário: \033[0m{i[4].strftime('%H')}:{i[4].strftime('%M')}")
            print(f"\033[1mPeso: \033[0m{i[1]}kg")
            print(f"\033[1mAltura: \033[0m{i[2]}m")
            print(f"\033[1mIMC: \033[0m{i[3]}\n")

        input("Pressione enter para voltar ao menu...")
        opcaoUser == "0"
        userMenu(userId)

    while opcaoUser == "3":
        os.system('cls')
        res = input("\033[1mPypy - Análise de Dados\033[0m\n\n[1] - Média de IMC por faixa etária\n[2] - Média de IMC por faixa corporal\n[3] - Média de IMC por estatura física\n[4] - Personalizado\n[5] - Voltar\n\n\033[1mUsuário: \033[0m")

        while res == "1":
            os.system('cls')
            mode = input("\033[1mPypy - Selecione o Gráfico desejado \033[0m\n\n[1] - Gráfico de Linhas \n[2] - Gráfico de Barras\n[3] - Voltar\n\n\033[1mUsuário: \033[0m")
            if int(mode) >= 3:
                res = '0'
            else:
                getAnalise(res, mode)
        while res == "2":
            os.system('cls')
            mode = input("\033[1mPypy - Selecione o Gráfico desejado \033[0m\n\n[1] - Gráfico de Linhas \n[2] - Gráfico de Barras\n[3] - Voltar\n\n\033[1mUsuário: \033[0m")
            if int(mode) >= 3:
                res = '0'
            else:
                getAnalise(res, mode)
        while res == "3":
            os.system('cls')
            mode = input("\033[1mPypy - Selecione o Gráfico desejado \033[0m\n\n[1] - Gráfico de Linhas \n[2] - Gráfico de Barras\n[3] - Voltar\n\n\033[1mUsuário: \033[0m")
            if int(mode) >= 3:
                res = '0'
            else:
                getAnalise(res, mode)
        while res == "4":
            os.system('cls')

            idadeMinima = input("\033[1mPypy - Análise de Dados Personalizado\n\nDigite a idade miníma:\033[0m ")
            idadeMaxima = input("\033[1mDigite a idade máxima:\033[0m ")

            pesoMinimo = input("\033[1m\nDigite o peso mínimo:\033[0m ")
            pesoMaximo = input("\033[1mDigite o peso máximo:\033[0m ")

            alturaMinima = input("\033[1m\nDigite a altura mínima:\033[0m ")
            alturaMaxima = input("\033[1mDigite a altura máxima:\033[0m ")

            getAnalisePersonalizada(idadeMinima, idadeMaxima, pesoMinimo, pesoMaximo, alturaMinima, alturaMaxima)
            res = getAnalisePersonalizada(idadeMinima, idadeMaxima, pesoMinimo, pesoMaximo, alturaMinima, alturaMaxima)
        if res == "5":
            opcaoUser == "5"
            userMenu(userId)

    while opcaoUser == "4":
        main()

def cadastrar(nome, user, senha, dataNasc):
    retorno = database.insert(f"INSERT INTO usuario VALUES (NULL, '{nome}', '{user}', MD5('{senha}'), '{dataNasc}')")
    if retorno == 1:
        os.system('cls')
        print('\033[1mPypy - Cadastro\033[0m\n\nCadastro realizado com sucesso!')
        time.sleep(2)
        main(False, False)
    else:
        print('Username já é utlizado!')
        time.sleep(2)
        main(False, True)

def entrar(user, senha):
    os.system('cls')
    dados = database.select(f"SELECT idUsuario, username, nome FROM usuario where username = '{user}' and senha = MD5('{senha}')")
    if type(dados) == type(None):
        print("\033[1mPypy - Falha no Login\033[0m\n\nUsuário ou senha inválidos")
        time.sleep(2)
        main(isRepeatLog = True)
    else:
        print("\033[1mPypy - Sucesso no Login\033[0m\n\nLogin feito com sucesso\nAbrindo menu inicial...\n")
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
        userInput = input("\033[1mPypy - IMC\033[0m\n\n[1] - Entrar\n[2] - Cadastrar\n[3] - Visitante\n[4] - Sair\n\n\033[1mUsuário:\033[0m ")

    if userInput == "1":
        os.system('cls')
        username = input("\033[1mPypy - Login\n\nUsername:\033[0m ")
        senha = getpass.getpass('\033[1mSenha:\033[0m ')
        entrar(username, senha)
    elif userInput == "2":
        os.system('cls')
        nome = input("\033[1mPypy - Cadastro\033[0m\n\nNome completo: ")
        user = input("Username: ")
        dataNasc = input("Data de nascimento(AAAA-MM-DD): ")
        senha = getpass.getpass("Senha:")
        confSenha = getpass.getpass("Confirme a senha: ")
        if senha == confSenha:
            cadastrar(nome, user, senha, dataNasc)
        else:
            os.system('cls')
            print("\033[1mPypy\033[0m\n\nAs senhas são diferentes")
            time.sleep(3)
            main(isRepeatCad = True)
    elif userInput == '3':
        print(imc(userId = None, isLogado = False))
        input("\nPressione enter para continuar...")
        main()
    elif userInput == '4':
        os.system('cls')
        print("""Foi bom o tempo que passamos juntos ♡\n\n\n\n\033[1mDesenvolvido por\n\nLeonardo Vasconcelos Paulino\033[0m\ngithub.com/LeoVasc5\n\n\033[1mVinícius da Silva Cardoso\033[0m\ngithub.com/ViniScardoso\n\n""")
        time.sleep(7)
        os.system('cls')
        exit()

main()