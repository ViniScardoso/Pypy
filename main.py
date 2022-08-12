import os
import time
from functions import imc
import getpass
from login import logar, cadastrar


def main(isRepeat = False):
    if isRepeat:
        os.system('cls')
    else:
        os.system('cls')
        # nome = input("\033[1mCálculo de IMC\n\nNome:\033[0m ")
        # peso = float(input("\033[1mKG:\033[0m "))
        # altura = float(input("\033[1mAltura: \033[0m"))
        # print(f"{imc(nome, peso, altura)}.\n\n")
        
        userInput = input("\033[1mCálculo de IMC\033[0m\n\n[1] - Entrar\n[2] - Cadastrar\n[3] - Visitante\n\n\033[1mUsuário:\033[0m ")

        if userInput == "1":
            username = input("username: ")
            senha = getpass.getpass('Senha:')
            logar(username, senha)
        elif userInput == "2":
            nome = input("Nome completo: ")
            user = input("Username: ")
            dataNasc = input("Data de nascimento - (AAAA-MM-DD): ")
            senha = getpass.getpass("Senha:")
            confSenha = getpass.getpass("Confirme a senha: ")
            if senha == confSenha:
                cadastrar(nome, user, senha, dataNasc)


        
    res = input("[1] - Nova operação\n[2] - Sair \n")
    if res == "1":
        main(False)
    elif res == "2":
        print("Obrigado por usar nossos serviços <3")
        time.sleep(4)
        exit()
    else:
        print("Opção inválida")
        time.sleep(1)
        main(True)
    
main()


    