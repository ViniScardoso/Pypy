import matplotlib.pyplot as plt
from database import select
import numpy as np

def getAnalise(analise, mode):
    if(analise == '1'):
        x = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
        y = []

        print("Aguarde um momento enquanto geramos o seu gráfico...\n")
        for i in x:    
            valor = (select(f"""SELECT AVG(dataset.imc) FROM (SELECT peso, altura, imc, TIMESTAMPDIFF(YEAR,datanasc,MAX(dataHoraReg)) AS idade 
            FROM registro JOIN usuario ON fkUsuario = idUsuario GROUP BY fkUsuario) AS dataset WHERE idade > {i} AND idade < {i+5};"""))

            if valor[0] == None:
                y.append(0)
            else:
                y.append(valor[0])
 
        if(mode == '1'):
            plt.plot(x, y)
        plt.show()
    
    elif(analise == '2'):
        print('Analise')

# getAnalise(analise, mode)