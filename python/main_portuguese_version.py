import numpy as np
import matplotlib.pyplot as plt

def apresentar_sistema():
    print("\nBem-vindo ao Analisador de Sinais Discretos!")
    print("-" * 40)
    print("Este sistema permite processar sinais discretos aplicando diversas transformações e análises.")
    print("Você poderá visualizar gráficos e entender características do sistema que manipula o sinal.")
    print("Insira um conjunto de até 9 números inteiros entre -9 e 9.")
    print("Recomendamos escolher valores entre -3 e 3 para melhor interpretação visual.")
    print("-" * 40)

def obter_sinal():
    while True:
        entrada = input("\nDigite até 9 números inteiros separados por espaço: ")
        try:
            x = list(map(int, entrada.split()))
            if len(x) > 9:
                print("Por favor, insira no máximo 9 números.")
            elif any(abs(num) > 9 for num in x):
                print("Todos os números devem estar entre -9 e 9.")
            else:
                return np.array(x)
        except ValueError:
            print("Entrada inválida. Certifique-se de inserir apenas números inteiros.")

def plotar_sinal(x):
    n = np.arange(len(x))
    plt.figure(figsize=(8, 4))
    plt.stem(n, x, basefmt=" ")
    plt.title("Sinal Original x[n]")
    plt.xlabel("n")
    plt.ylabel("x[n]")
    plt.grid()
    plt.show()

# Execução do menu
apresentar_sistema()
sinal = obter_sinal()
plotar_sinal(sinal)

#---###---#

