import matplotlib.pyplot as plt
from database import select

def getAnalise(analise, mode):
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')

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

        x = ['0 - 4', '5 - 9', '10 - 14', '15 - 19', '20 - 24', '25 - 29', '30 - 34', '35 - 39', '40 - 44', '45 - 49', 
        '50 - 54', '55 - 59', '60 - 64', '65 - 69', '70 ou mais']

        plt.title("Análise de IMC por faixa etária")
        plt.xlabel('Idade')
        plt.ylabel('IMC')
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
 
        x = ['0 - 9', '10 - 19', '20 - 29', '30 - 39', '40 - 49', '50 - 59', '60 - 69', '70 - 79', '80 - 89', '90 - 99', 
            '100 - 109', '110 - 119', '120 ou mais']

        plt.title("Análise de IMC por faixa corporal")
        plt.xlabel('Peso')
        plt.ylabel('IMC')
        if(mode == '1'):
            plt.plot(x, y)
        elif(mode == '2'):
            plt.bar(x,y)
        plt.show()

    elif(analise == '3'): ##Analise de IMC por altura
        x = [1.40, 1.50, 1.60, 1.70, 1.80, 1.90, 2.00, 2.10, 2.20]
        y = []

        print("Aguarde um momento enquanto geramos o seu gráfico...\n")
        for i in x:    
            valor = (select(f"""SELECT AVG(dataset.imc) FROM (SELECT peso, altura, imc, TIMESTAMPDIFF(YEAR,datanasc,MAX(dataHoraReg)) AS idade 
            FROM registro JOIN usuario ON fkUsuario = idUsuario GROUP BY fkUsuario) AS dataset WHERE altura >= {i} AND altura < {i + 0.1};"""))

            if valor[0] == None:
                y.append(0)
            else:
                y.append(valor[0])
 
        x = ['1.40 - 1.49', '1.50 - 1.59', '1.60 - 1.69', '1.70 - 1.79', '1.80 - 1.89', '1.90 - 1.99', '2.00 - 2.09', '2.10 - 2.19', '2.20 ou mais']

        plt.title("Análise de IMC por faixa de estatura")
        plt.xlabel('Altura')
        plt.ylabel('IMC')

        if(mode == '1'):
            plt.plot(x, y)
        elif(mode == '2'):
            plt.bar(x,y)
        plt.show()

# getAnalise('3', '2')