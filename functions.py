from database import select, insert
import datetime as dt
import pytz
import os

def imc(userId, isLogado = True):
    os.system('cls')
    peso = float(input(f"\033[1mCálculo de IMC - Cálculo de IMC\n\nInsira seu peso:\033[0m "))
    altura = float(input(f"\033[1mInsira sua altura:\033[0m "))
    res = round((peso / altura ** 2), 2)

    if isLogado:
        insert(f"INSERT INTO registro VALUES (NULL, {peso}, {altura}, {res}, '{dt.datetime.now(pytz.timezone('America/Sao_Paulo'))}', {userId});")

    if(res < 18.5):
        return f"\033[1mIMC:\033[0m {res}\n\033[1mEstado: \033[0mAbaixo do peso ideal"
    elif(18.5 <= res < 25):
        return f"\033[1mIMC:\033[0m {res}\n\033[1mEstado: \033[0mPeso ideal"
    elif(25 <= res < 30):
        return f"\033[1mIMC:\033[0m {res}\n\033[1mEstado: \033[0mSobrepeso"
    elif(30 <= res < 40):
        return f"\033[1mIMC:\033[0m {res}\n\033[1mEstado: \033[0mObesidade"
    elif(res > 40):
        return f"\033[1mIMC:\033[0m {res}\n\033[1mEstado: \033[0mObesidade Mórbida"


def historico(userId):
    return select(f"SELECT * FROM registro WHERE fkUsuario = '{userId}'", True)
