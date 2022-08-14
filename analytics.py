import matplotlib.pyplot as plt
from database import select
# import numpy as np

def getAnalise(analise, mode):
    if(analise == "1"): ## Analise de IMC por faixa etária
        x = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
        y = []

        print("Aguarde um momento enquanto geramos o seu gráfico...\n")
        for i in x:    
            valor = (select(f"""SELECT AVG(dataset.imc) FROM (SELECT peso, altura, imc, TIMESTAMPDIFF(YEAR,datanasc,MAX(dataHoraReg)) AS idade 
            FROM registro JOIN usuario ON fkUsuario = idUsuario GROUP BY fkUsuario) AS dataset WHERE idade >= {i} AND idade < {i+5};"""))

            if valor[0] == None:
                y.append(0)
            else:
                y.append(valor[0])
 
        if(mode == '1'):
            plt.plot(x, y)
        elif(mode == '2'):
            plt.bar(x,y)
        plt.show()
    
    elif(analise == '2'): ##Analise de IMC por peso
        x = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
        y = []

        print("Aguarde um momento enquanto geramos o seu gráfico...\n")
        for i in x:    
            valor = (select(f"""SELECT AVG(dataset.imc) FROM (SELECT peso, altura, imc, TIMESTAMPDIFF(YEAR,datanasc,MAX(dataHoraReg)) AS idade 
            FROM registro JOIN usuario ON fkUsuario = idUsuario GROUP BY fkUsuario) AS dataset WHERE peso >= {i} AND peso < {i+10};"""))

            if valor[0] == None:
                y.append(0)
            else:
                y.append(valor[0])
 
        if(mode == '1'):
            plt.plot(x, y)
        elif(mode == '2'):
            plt.bar(x,y)
        plt.show()

    elif(analise == '3'): ##Analise de IMC por altura
        x = [1.40, 1.50, 1.60, 1.80, 1.90, 2.00, 2.10]
        y = []

        print("Aguarde um momento enquanto geramos o seu gráfico...\n")
        for i in x:    
            valor = (select(f"""SELECT AVG(dataset.imc) FROM (SELECT peso, altura, imc, TIMESTAMPDIFF(YEAR,datanasc,MAX(dataHoraReg)) AS idade 
            FROM registro JOIN usuario ON fkUsuario = idUsuario GROUP BY fkUsuario) AS dataset WHERE altura >= {i} AND altura < {i + 0.1};"""))

            if valor[0] == None:
                y.append(0)
            else:
                y.append(valor[0])
 
        

        if(mode == '1'):
            plt.plot(x, y)
        elif(mode == '2'):
            plt.bar(x,y)
        plt.show()

# getAnalise(analise, mode)