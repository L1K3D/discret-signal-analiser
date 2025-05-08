# Importando bibliotecas necessárias
import numpy as np                          # Para operações numéricas e vetoriais
import matplotlib.pyplot as plt            # Para geração de gráficos
import tkinter as tk                       # Para criação da interface gráfica
from tkinter import messagebox             # Para exibição de mensagens pop-up
from tkinter import ttk                    # Para uso de widgets modernos (como abas)
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Para embutir gráficos matplotlib no tkinter

def get_system_analysis(x):
    """Gera uma string com a análise dos sistemas baseados no sinal de entrada x."""
    n = np.arange(len(x))  # Vetor de índices
    result_str = ""        # Inicializa string de resultado

    # --- Sistema 1: Diferença entre amostras consecutivas ---
    y1 = np.zeros_like(x)                  # Inicializa vetor de saída
    y1[1:] = x[1:] - x[:-1]                # y[n] = x[n] - x[n-1], com y[0] = 0
    result_str += "Sistema 1: y[n] = x[n] - x[n-1]\n"
    result_str += "  Causal: Sim\n  Com memória: Sim\n  Estável: Sim\n  Invariante no tempo: Não\n  Linear: Sim\n"
    result_str += "-" * 40 + "\n\n"

    # --- Sistema 2: Soma acumulada ---
    y2 = np.cumsum(x)                      # y[n] = soma acumulada até n
    result_str += "Sistema 2: y[n] = soma acumulada de x[k]\n"
    result_str += "  Causal: Sim\n  Com memória: Sim\n  Estável: Sim\n  Invariante no tempo: Não\n  Linear: Sim\n"
    result_str += "-" * 40 + "\n\n"

    # --- Sistema 3: Compressão no tempo ---
    n_compressed = n // 2                  # Índices para compressão temporal
    y3 = x[n_compressed] if len(n_compressed) <= len(x) else x  # y[n] = x[2n]
    result_str += "Sistema 3: y[n] = x[2n]\n"
    result_str += "  Causal: Sim\n  Com memória: Não\n  Estável: Sim\n  Invariante no tempo: Sim\n  Linear: Sim\n"
    result_str += "-" * 40 + "\n"

    return result_str

def update_sinais_tab(x):
    """Atualiza a aba de sinais exibindo o sinal original e suas transformações."""
    n = np.arange(len(x))  # Índices do sinal

    # --- Gráfico do sinal original ---
    fig_orig = plt.Figure(figsize=(6, 3), dpi=100)
    ax_orig = fig_orig.add_subplot(111)
    ax_orig.stem(n, x, basefmt=" ")               # Gráfico de haste (stem)
    ax_orig.set_title("Sinal Original x[n]")
    ax_orig.grid(True)

    # --- Gráficos das transformações ---
    fig_trans = plt.Figure(figsize=(6, 8), dpi=100)

    # Deslocamento temporal: x[n-2]
    ax1 = fig_trans.add_subplot(311)
    ax1.stem(n + 2, x, basefmt=" ")
    ax1.set_title("Sinal Deslocado x[n-2]")
    ax1.grid(True)

    # Reflexão temporal: x[-n]
    ax2 = fig_trans.add_subplot(312)
    ax2.stem(-n, x, basefmt=" ")
    ax2.set_title("Sinal Refletido x[-n]")
    ax2.grid(True)

    # Compressão temporal: x[2n]
    ax3 = fig_trans.add_subplot(313)
    n_compressed = n // 2
    x_compressed = x[n_compressed] if len(n_compressed) <= len(x) else x
    ax3.stem(n_compressed, x_compressed, basefmt=" ")
    ax3.set_title("Sinal Comprimido x[2n]")
    ax3.grid(True)

    # Remove widgets anteriores da aba
    for widget in frameSinais.winfo_children():
        widget.destroy()

    # --- Criação de container com rolagem ---
    canvasFrame = tk.Frame(frameSinais)
    canvasFrame.pack(fill=tk.BOTH, expand=True)

    scroll_sinais = tk.Scrollbar(canvasFrame)
    scroll_sinais.pack(side=tk.RIGHT, fill=tk.Y)

    canvas = tk.Canvas(canvasFrame, yscrollcommand=scroll_sinais.set)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    scroll_sinais.config(command=canvas.yview)

    # Frame interno para colocar os gráficos
    frame_inner = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame_inner, anchor="nw")

    # Adiciona gráfico original
    canvas_orig = FigureCanvasTkAgg(fig_orig, master=frame_inner)
    canvas_orig.draw()
    canvas_orig.get_tk_widget().pack(pady=5)

    # Adiciona gráfico das transformações
    canvas_trans = FigureCanvasTkAgg(fig_trans, master=frame_inner)
    canvas_trans.draw()
    canvas_trans.get_tk_widget().pack(pady=5)

    # Atualiza a área de rolagem
    frame_inner.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def processar_sinal():
    """Valida a entrada do usuário, processa o sinal e atualiza a interface."""
    entrada = entry.get()
    try:
        # Converte entrada para lista de inteiros
        x_list = list(map(int, entrada.split()))
        
        # Valida número de elementos
        if len(x_list) > 9:
            messagebox.showerror("Erro", "Insira no máximo 9 números.")
            return
        # Valida faixa de valores
        elif any(abs(num) > 9 for num in x_list):
            messagebox.showerror("Erro", "Os números devem estar entre -9 e 9.")
            return
        x = np.array(x_list)  # Converte para array numpy
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida. Use apenas números inteiros.")
        return

    # Atualiza gráficos
    update_sinais_tab(x)

    # Atualiza análise textual dos sistemas
    analysis_str = get_system_analysis(x)
    textAnalysis.config(state="normal")
    textAnalysis.delete("1.0", tk.END)
    textAnalysis.insert(tk.END, analysis_str)
    textAnalysis.config(state="disabled")

    # Alterna para aba de sinais automaticamente
    notebook.select(tab_sinais)

# --- Montagem da Interface Gráfica ---

# Criação da janela principal
root = tk.Tk()
root.title("Analisador de Sinais Discretos")
root.geometry("800x800")

# Frame superior com instruções e entrada
frameInput = tk.Frame(root)
frameInput.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

tk.Label(frameInput, text="Bem-vindo ao Analisador de Sinais Discretos!", font=("Arial", 16)).pack()
tk.Label(frameInput, text="Digite até 9 números inteiros entre -9 e 9, separados por espaço.", font=("Arial", 12)).pack()
tk.Label(frameInput, text="Recomendamos escolher valores entre -3 e 3.", font=("Arial", 12)).pack(pady=5)

# Campo de entrada
entry = tk.Entry(frameInput, font=("Arial", 12), width=40)
entry.pack(pady=5)

# Botão para processar o sinal
btnProcessar = tk.Button(frameInput, text="Processar Sinal", font=("Arial", 12), command=processar_sinal)
btnProcessar.pack(pady=5)

# Notebook com abas: Sinais e Análise
notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Aba de Sinais
tab_sinais = tk.Frame(notebook)
notebook.add(tab_sinais, text="Sinais")
frameSinais = tk.Frame(tab_sinais)
frameSinais.pack(fill=tk.BOTH, expand=True)

# Aba de Análise de Sistemas
tab_analise = tk.Frame(notebook)
notebook.add(tab_analise, text="Análise de Sistemas")

frame_analise = tk.Frame(tab_analise)
frame_analise.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

scrollbar_analise = tk.Scrollbar(frame_analise)
scrollbar_analise.pack(side=tk.RIGHT, fill=tk.Y)

# Caixa de texto com análise dos sistemas
textAnalysis = tk.Text(frame_analise, wrap=tk.WORD, font=("Arial", 12), yscrollcommand=scrollbar_analise.set)
textAnalysis.pack(fill=tk.BOTH, expand=True)
scrollbar_analise.config(command=textAnalysis.yview)
textAnalysis.config(state="disabled")  # Inicialmente desabilitado

# Inicia o loop principal da interface
root.mainloop()