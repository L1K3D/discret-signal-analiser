import numpy as np
import matplotlib.pyplot as plt

# Função de boas-vindas e instruções para o usuário
def apresentar_sistema():
    print("\nBem-vindo ao Analisador de Sinais Discretos!")
    print("-" * 40)
    print("Este sistema permite processar sinais discretos aplicando diversas transformações e análises.")
    print("Você poderá visualizar gráficos e entender características do sistema que manipula o sinal.")
    print("Insira um conjunto de até 9 números inteiros entre -9 e 9.")
    print("Recomendamos escolher valores entre -3 e 3 para melhor interpretação visual.")
    print("-" * 40)

# Função para obter entrada do usuário de forma validada
def obter_sinal():
    while True:
        entrada = input("\nDigite até 9 números inteiros separados por espaço: ")
        try:
            x = list(map(int, entrada.split()))  # Converte os valores de string para inteiro
            if len(x) > 9:
                print("Por favor, insira no máximo 9 números.")  # Verifica quantidade
            elif any(abs(num) > 9 for num in x):
                print("Todos os números devem estar entre -9 e 9.")  # Verifica limites
            else:
                return np.array(x)  # Retorna um array NumPy
        except ValueError:
            print("Entrada inválida. Certifique-se de inserir apenas números inteiros.")

# Função para plotar graficamente o sinal original
def plotar_sinal(x):
    n = np.arange(len(x))  # Gera eixo n (índices)
    plt.figure(figsize=(8, 4))
    plt.stem(n, x, basefmt=" ")  # Gráfico de haste (sinal discreto)
    plt.title("Sinal Original x[n]")
    plt.xlabel("n")
    plt.ylabel("x[n]")
    plt.grid()
    plt.show()

# --- Execução do menu e entrada do usuário ---
apresentar_sistema()
sinal = obter_sinal()
plotar_sinal(sinal)

# --- Inicialização dos dados para transformações ---
x = sinal
n = np.arange(len(x))

# --- Transformações no sinal ---

# 1. Deslocamento temporal: move o sinal 2 unidades para frente no tempo
n_shifted = n + 2
x_shifted = x  # O valor do sinal não muda

# 2. Reflexão temporal: inverte o eixo do tempo
n_reflected = -n
x_reflected = x  # Valores permanecem os mesmos

# 3. Compressão temporal por 2: 'acelera' o tempo
n_compressed = n // 2  # Diminui os índices para comprimir
x_compressed = x[n_compressed]  # Seleciona os elementos correspondentes

# --- Plotagem dos sinais transformados ---
fig, axs = plt.subplots(3, 1, figsize=(10, 8))

# Gráfico do deslocamento temporal
axs[0].stem(n_shifted, x_shifted, basefmt=" ")
axs[0].set_title("Sinal Deslocado x[n-2]")
axs[0].grid()

# Gráfico da reflexão temporal
axs[1].stem(n_reflected, x_reflected, basefmt=" ")
axs[1].set_title("Sinal Refletido x[-n]")
axs[1].grid()

# Gráfico da compressão temporal
axs[2].stem(n_compressed, x_compressed, basefmt=" ")
axs[2].set_title("Sinal Comprimido x[2n]")
axs[2].grid()

plt.tight_layout()
plt.show()

# --- Implementação de Sistemas Discretos ---

# Sistema 1: Diferença entre amostras consecutivas
y1 = np.zeros_like(x)  # Inicializa vetor de saída com zeros
y1[1:] = x[1:] - x[:-1]  # y[n] = x[n] - x[n-1]; y[0] = 0 assumido

# Sistema 2: Soma acumulada do sinal (integrador)
y2 = np.cumsum(x)  # Soma cumulativa de x[0] até x[n]

# Sistema 3: Compressão temporal (já feita anteriormente)
y3 = x_compressed

# --- Função para análise das propriedades de um sistema ---
def analisar_sistema(y, nome):
    print(f"Análise do Sistema: {nome}")
    
    # Verifica causalidade: todas as respostas estão associadas a n >= 0
    print(f"Causal: {'Sim' if np.all(y[n >= 0]) else 'Não'}")
    
    # Verifica presença de memória: mais de um valor de entrada influencia a saída
    print(f"Com memória: {'Sim' if len(y) > 1 else 'Não'}")
    
    # Verifica estabilidade: nenhuma saída tende ao infinito
    print(f"Estável: {'Sim' if np.all(np.abs(y) < np.inf) else 'Não'}")
    
    # Verifica invariança no tempo (simplificada e aproximada com roll)
    print(f"Invariante no tempo: {'Sim' if np.array_equal(y, np.roll(y, 1)) else 'Não'}")
    
    # Verifica linearidade (simplificação com homogeneidade e aditividade parcial)
    print(f"Linear: {'Sim' if np.all(y * 2 == np.concatenate(([0], y[:-1])) * 2) else 'Não'}")
    print("-" * 40)

# --- Chamada da análise para cada sistema definido ---
analisar_sistema(y1, "y[n] = x[n] - x[n-1]")  # Sistema derivador
analisar_sistema(y2, "y[n] = soma acumulada de x[k]")  # Sistema integrador
analisar_sistema(y3, "y[n] = x[2n]")  # Sistema compressão