import matplotlib.pyplot as plt
import os
from database import select

def getAnalise(analise, mode):
    if analise == "1": ## Analise de IMC por faixa etária
        x = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
        y = []

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
        wm = plt.get_current_fig_manager()
        # wm.window.state('zoomed')
        plt.show()
    
    elif analise == '2': ##Analise de IMC por peso
        x = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
        y = []

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
        wm = plt.get_current_fig_manager()
        plt.show()

    elif analise == '3': ##Analise de IMC por altura
        x = [1.40, 1.50, 1.60, 1.70, 1.80, 1.90, 2.00, 2.10, 2.20]
        y = []

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
        wm = plt.get_current_fig_manager()
        plt.show()


def getAnalisePersonalizada(idadeMinima, idadeMaxima, pesoMinimo, pesoMaximo, alturaMinima, alturaMaxima):
    os.system('cls')
    repeat = '1'
    
    while repeat == '1':
        res = input("\033[1mPypy - Escolha o tipo de gráfico\033[0m\n\n[1] - Gráfico de Linhas\n[2] - Gráfico de Barras\n\n\033[1mUsuário:\033[0m ")
        valor = select(f"""SELECT * FROM (SELECT peso, altura, imc, TIMESTAMPDIFF(YEAR,datanasc,MAX(dataHoraReg)) AS idade 
        FROM registro JOIN usuario ON fkUsuario = idUsuario GROUP BY fkUsuario) AS dataset WHERE idade BETWEEN {idadeMinima} 
        AND {idadeMaxima} AND peso BETWEEN {pesoMinimo} AND {pesoMaximo} AND altura BETWEEN {alturaMinima} AND {alturaMaxima} ORDER BY imc;""", True)

        idades = []
        pesos = []
        alturas = []
        imcs = []

        for i in valor:
            pesos.append(i[0])
            alturas.append(i[1])
            imcs.append(i[2])
            idades.append(i[3])


        if res == '1':
            fig, (ax1, ax2, ax3) = plt.subplots(3)
            fig.suptitle('Análise de Dados por IMC')
            fig.tight_layout()

            ax1.plot(imcs, pesos)
            ax1.set_xlabel('IMC')
            ax1.set_ylabel('Peso')

            ax2.plot(imcs, alturas)
            ax2.set_xlabel('IMC')
            ax2.set_ylabel('Altura')

            ax3.plot(imcs, idades)
            ax3.set_xlabel('IMC')
            ax3.set_ylabel('Idade')
        elif res == '2':
            fig, (ax1, ax2, ax3) = plt.subplots(3)
            fig.suptitle('Análise de Dados por IMC')
            fig.tight_layout()

            ax1.bar(imcs, pesos, width=0.3)
            ax1.set_xlabel('IMC')
            ax1.set_ylabel('Peso')

            ax2.bar(imcs, alturas)
            ax2.set_xlabel('IMC')
            ax2.set_ylabel('Altura')

            ax3.bar(imcs, idades)
            ax3.set_xlabel('IMC')
            ax3.set_ylabel('Idade')
    
        wm = plt.get_current_fig_manager()
        wm.window.state('zoomed')
        plt.show()

        os.system('cls')
        resUsuario = input("\033[1mPypy - Análise de Dados\033[0m\n\n[1] - Escolher outro gráfico\n[2] - Alterar parâmetros de pesquisa\n[3] - Voltar\n\n\033[1mUsuário:\033[0m") 

        if resUsuario == '1':
            getAnalisePersonalizada(idadeMinima, idadeMaxima, pesoMinimo, pesoMaximo, alturaMinima, alturaMaxima)
        elif resUsuario == '2':
            repeat = '0'
        else:
            return "5"


# getAnalise('1', '1')
# getAnalisePersonalizada(10, 50, 50, 90, 1.40, 1.90)