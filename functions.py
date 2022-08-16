from itertools import count
from database import select, insert
import datetime as dt
import pytz
import os
import time

def imc(userId, isLogado = True):
    os.system('cls')
    peso = input(f"\033[1mPypy - Cálculo de IMC\n\nInsira seu peso:\033[0m ")
    altura = input(f"\033[1mInsira sua altura:\033[0m ")

    if len(peso) > 3 or len(altura) > 4:
        print("Entrada de dados inválida.")
        time.sleep(1)
        imc(userId)
    else:
        peso = float(peso)
        altura = float(altura)
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

def relatorio(mode):
    if mode == '1':
        x = [1, 10, 20, 30, 40, 50, 60, 70]
        y = ['0 - 9', '10 - 19', '20 - 29', '30 - 39', '40 - 49', '50 - 59', '60 - 69', '70 ou mais']
        media = total = cont = abaixoPeso = pesoIdeal = sobrepeso = obesidade = morbida =  0

        os.system('cls')
        print("\033[1mPypy - Relatório por Faixa Etária\033[0m\n")
        for i in x:
            valor = (select(f"""SELECT * FROM (SELECT imc, TIMESTAMPDIFF(YEAR,datanasc,MAX(dataHoraReg)) AS idade FROM registro JOIN usuario ON fkUsuario = idUsuario GROUP BY fkUsuario) AS dataset WHERE idade >= {i} AND idade < {i+10};""", True))
            print("Idade: "+ str(i) + " até " + str(i+9) +" anos: " + str(len(valor)))
            totalReg = select("SELECT COUNT(idRegistro) FROM registro")
            for j in valor:
                total += j[0]
                if(j[0] < 18.5):
                    abaixoPeso+=1
                elif(18.5 <= j[0] < 25):
                    pesoIdeal+=1
                elif(25 <= j[0] < 30):
                    sobrepeso+=1
                elif(30 <= j[0] < 40):
                    obesidade+=1
                elif(j[0] > 40):
                    morbida+=1
            media = total / len(valor)
           

            print(f"--------------------------------------------\n\033[1m{y[cont]} ANOS\nQuantidade:\033[0m {round(len(valor) / totalReg[0] * 100, 0)}% ({len(valor)} registros)")
            print(f"""\033[1mIMC Médio:\033[0m {round(media, 1)}\n\033[1mAbaixo do Peso:\033[0m {round(abaixoPeso/len(valor) * 100, 0)}% ({abaixoPeso} registros) 
\033[1mPeso Ideal: \033[0m{round(pesoIdeal / len(valor) * 100, 0)}% ({pesoIdeal} registros) 
\033[1mSobrepeso: \033[0m{round(sobrepeso / len(valor) * 100, 0)}% ({sobrepeso} registros) 
\033[1mObesidade: \033[0m{round(obesidade / len(valor) * 100, 0)}% ({obesidade} registros) 
\033[1mObesidade morbida: \033[0m{round(morbida / len(valor) * 100, 0)}% ({morbida} registros)\n-------------------------------------------\n""")
            cont+=1
            abaixoPeso = pesoIdeal = sobrepeso = obesidade = morbida = media = total = 0        
            
        input("Aperte enter para continuar...")
        return 0


    if mode == '2':
        x = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
        y = ['0 - 9', '10 - 19', '20 - 29', '30 - 39', '40 - 49',
        '50 - 59', '60 - 69', '70 - 79', '80 - 89', '90 - 99', '100 - 109', '110 ou mais']
        media = total = cont = abaixoPeso = pesoIdeal = sobrepeso = obesidade = morbida =  0

        os.system('cls')
        print("\033[1mPypy - Relatório por Faixa Etária\033[0m\n")
        for i in x:
            valor = (select(f"""SELECT * FROM (SELECT imc, peso FROM registro JOIN usuario ON fkUsuario = idUsuario GROUP BY fkUsuario) AS dataset WHERE peso >= {i} AND peso < {i+9};""", True))
            totalReg = select("SELECT COUNT(idRegistro) FROM registro")
            for j in valor:
                total += j[0]
                if(j[0] < 18.5):
                    abaixoPeso+=1
                elif(18.5 <= j[0] < 25):
                    pesoIdeal+=1
                elif(25 <= j[0] < 30):
                    sobrepeso+=1
                elif(30 <= j[0] < 40):
                    obesidade+=1
                elif(j[0] > 40):
                    morbida+=1
            
            media = total / len(valor)

            print(f"--------------------------------------------\n\033[1m{y[cont]} KG\nQuantidade:\033[0m {round(len(valor) / totalReg[0] * 100, 0)}% ({len(valor)} registros)")
            print(f"""\033[1mIMC Médio:\033[0m {round(media, 1)}\n\033[1mAbaixo do Peso:\033[0m {round(abaixoPeso / len(valor) * 100, 0)}% ({abaixoPeso} registros) 
\033[1mPeso Ideal: \033[0m{round(pesoIdeal / len(valor) * 100, 0)}% ({pesoIdeal} registros) 
\033[1mSobrepeso: \033[0m{round(sobrepeso / len(valor) * 100, 0)}% ({sobrepeso} registros) 
\033[1mObesidade: \033[0m{round(obesidade / len(valor) * 100, 0)}% ({obesidade} registros) 
\033[1mObesidade morbida: \033[0m{round(morbida / len(valor) * 100, 0)}% ({morbida} registros)\n-------------------------------------------\n""")

            abaixoPeso = pesoIdeal = sobrepeso = obesidade = morbida = media = total = 0        
            cont+=1
            
        input("Aperte enter para continuar...")

    if mode == '3':
        x = [0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2]
        y = ['20cm - 39cm', '40cm - 59cm', '60cm - 79cm', '80cm - 99cm', '1m - 1.19m',
        '1.20m - 1.39m', '1.40m - 1.59m', '1.60m - 1.79m', '1.80m - 1.99m', '2m - 2.19m', '2.20m ou mais']
        media = total = cont = abaixoPeso = pesoIdeal = sobrepeso = obesidade = morbida =  0

        os.system('cls')
        print("\033[1mPypy - Relatório por Faixa Etária\033[0m\n")
        for i in x:
            valor = (select(f"""SELECT * FROM (SELECT imc, peso FROM registro JOIN usuario ON fkUsuario = idUsuario GROUP BY fkUsuario) AS dataset WHERE peso >= {i} AND peso < {i+20};""", True))
            totalReg = select("SELECT COUNT(idRegistro) FROM registro")
            for j in valor:
                total += j[0]
                if(j[0] < 18.5):
                    abaixoPeso+=1
                elif(18.5 <= j[0] < 25):
                    pesoIdeal+=1
                elif(25 <= j[0] < 30):
                    sobrepeso+=1
                elif(30 <= j[0] < 40):
                    obesidade+=1
                elif(j[0] > 40):
                    morbida+=1
            
            media = total / len(valor)

            print(f"--------------------------------------------\n\033[1m{y[cont]} metros\nQuantidade:\033[0m {round(len(valor) / totalReg[0] * 100, 0)}% ({len(valor)} registros)")
            print(f"""\033[1mIMC Médio:\033[0m {round(media, 1)}\n\033[1mAbaixo do Peso:\033[0m {round(abaixoPeso / len(valor) * 100, 0)}% ({abaixoPeso} registros) 
\033[1mPeso Ideal: \033[0m{round(pesoIdeal / len(valor) * 100, 0)}% ({pesoIdeal} registros) 
\033[1mSobrepeso: \033[0m{round(sobrepeso / len(valor) * 100, 0)}% ({sobrepeso} registros) 
\033[1mObesidade: \033[0m{round(obesidade / len(valor) * 100, 0)}% ({obesidade} registros) 
\033[1mObesidade morbida: \033[0m{round(morbida / len(valor) * 100, 0)}% ({morbida} registros)\n-------------------------------------------\n""")

            abaixoPeso = pesoIdeal = sobrepeso = obesidade = morbida = media = total = 0        
            cont+=1
            
        input("Aperte enter para continuar...")

relatorio('3')