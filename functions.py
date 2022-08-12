from database import select, insert
import datetime as dt
import pytz

def imc(nome, peso, altura):
    res = round((peso / altura ** 2), 2)

    insert(f"INSERT INTO usuario VALUES (NULL ,'{nome}', {peso}, {altura}, {res}, '{dt.datetime.now(pytz.timezone('America/Sao_Paulo'))}');")

    if(res < 18.5):
        return f"\033[1mIMC:\033[0m {res} \n\033[1mESTADO: \033[0m Abaixo do peso normal"
    elif(18.5 <= res < 25):
        return f"\033[1mIMC:\033[0m {res} \n\033[1mESTADO: \033[0m Peso normal"
    elif(25 <= res < 30):
        return f"\033[1mIMC:\033[0m {res} \n\033[1mESTADO: \033[0m Sobrepeso"
    elif(30 <= res < 40):
        return f"\033[1mIMC:\033[0m {res} \n\033[1mESTADO: \033[0m Obesidade"
    elif(res > 40):
        return f"\033[1mIMC:\033[0m {res} \n\033[1mESTADO: \033[0m Obesidade Morbida"