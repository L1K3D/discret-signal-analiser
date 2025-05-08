# 📡 Discrete Signal Analyzer - EN US

## Overview
The **Discrete Signal Analyzer** is a Python-based tool for processing discrete-time signals by applying **transformations** (time shift, reflection, and compression) and **analyzing system properties** (causality, memory, stability, time invariance, and linearity). It allows users to input a **custom signal** and observe the transformed outputs through graphical representations.

## 🔧 Features
- Accepts **up to 9 integers** as input for signal processing.
- Applies the following **signal transformations**:
  - **Time Shift**: Moves the signal forward by 2 units.
  - **Time Reflection**: Flips the signal over the time axis.
  - **Time Compression**: Reduces the time scale by a factor of 2.
- Implements **three discrete systems** for analysis:
  - **System 1**: Difference between consecutive samples \( y[n] = x[n] - x[n-1] \).
  - **System 2**: Cumulative sum (integrator) \( y[n] = \sum x[k] \).
  - **System 3**: Time compression \( y[n] = x[2n] \).
- Evaluates **five properties** of each system:
  - **Causality**
  - **Memory**
  - **Stability**
  - **Time Invariance**
  - **Linearity**
- Generates **stem plots** for visualizing discrete-time signals.

---

## 🚀 How to Install & Run

### Prerequisites
Ensure you have Python installed (version **3.6+** recommended). Also, install the necessary dependencies:
```bash
pip install numpy matplotlib
```

### Running the Script
Clone the repository or download the script:
```bash
git clone https://github.com/your-username/discrete-signal-analyzer.git
cd discrete-signal-analyzer
```
Run the Python script:
```bash
python signal_analyzer.py
```

Upon execution:
1. The program will **ask for a sequence of up to 9 numbers**.
2. The script will validate the input and process the signal.
3. **Graphs** will be generated to visualize the **original signal** and **transformed signals**.
4. The system analysis will be displayed in the **terminal**.

---

## 🖥️ Example Usage
### Input:
```
Enter up to 9 integers separated by spaces: 0 -2 -1 0 1 2 3 0 0
```

### Output:
**Graphical Representation**
✅ Original Signal  
✅ Shifted Signal \( x[n-2] \)  
✅ Reflected Signal \( x[-n] \)  
✅ Compressed Signal \( x[2n] \)  

**Terminal Analysis**
```
System Analysis: y[n] = x[n] - x[n-1]
  Causal: Yes
  Memory-based: Yes
  Stable: Yes
  Time-invariant: No
  Linear: Yes
----------------------------------------
System Analysis: y[n] = cumulative sum of x[k]
  Causal: Yes
  Memory-based: Yes
  Stable: Yes
  Time-invariant: No
  Linear: Yes
----------------------------------------
System Analysis: y[n] = x[2n]
  Causal: Yes
  Memory-based: No
  Stable: Yes
  Time-invariant: Yes
  Linear: Yes
----------------------------------------
```

---

## 📌 Notes & Limitations
- The input signal **must be integers** in the range **-9 to 9**.
- The system **assumes causal behavior** based on non-negative indices.
- The **cumulative sum system is limited** to the input size provided.
- The **compressed signal may discard some values** depending on the length.

---

## 🤝 Contributing
Have ideas for improving the project? Feel free to **fork** this repository and submit **pull requests**! If you encounter issues, please report them in the **GitHub Issues** section.

---

## 📜 License
This project is open-source and available under the **MIT License**.

---
---
---

Claro! Aqui está um README formatado no estilo do GitHub, agora completamente em **português**, explicando o funcionamento do código, como utilizá-lo e os resultados esperados. 🚀

---

# 📡 Analisador de Sinais Discretos

## 📌 Visão Geral
O **Analisador de Sinais Discretos** é um sistema em Python que processa sinais de tempo discreto aplicando **transformações** (deslocamento, reflexão e compressão) e **analisando propriedades do sistema** (causalidade, memória, estabilidade, invariância no tempo e linearidade). Ele permite que o usuário forneça um **sinal personalizado**, visualize **gráficos das transformações** e analise **como diferentes sistemas reagem ao sinal**.

---

## 🔧 Recursos
✔ Permite entrada de até **9 números inteiros** para análise de sinais.  
✔ Aplica as seguintes **transformações** no sinal de entrada:
   - **Deslocamento Temporal**: Move o sinal **2 unidades** para frente no tempo.
   - **Reflexão Temporal**: Espelha o sinal sobre o eixo do tempo.
   - **Compressão Temporal**: Reduz a escala de tempo por um fator de **2**.
✔ Implementa **3 sistemas discretos** para análise:
   - **Sistema 1:** Diferença entre amostras consecutivas \( y[n] = x[n] - x[n-1] \).
   - **Sistema 2:** Soma acumulada (integrador) \( y[n] = \sum x[k] \).
   - **Sistema 3:** Compressão temporal \( y[n] = x[2n] \).
✔ Avalia **5 propriedades** dos sistemas:
   - **Causalidade**
   - **Memória**
   - **Estabilidade**
   - **Invariância no tempo**
   - **Linearidade**
✔ Gera **gráficos discretos** para visualização dos sinais.

---

## 🚀 Como instalar e executar

### Pré-requisitos
Certifique-se de ter o **Python 3.6+** instalado e os pacotes necessários. Para instalar os pacotes:

```bash
pip install numpy matplotlib
```

### Executando o código
Baixe o repositório ou clone-o usando o Git:
```bash
git clone https://github.com/seu-usuario/analisador-sinais-discretos.git
cd analisador-sinais-discretos
```
Agora, execute o script Python:
```bash
python analisador_sinais.py
```

### Após a execução
1️⃣ O programa solicitará que você digite um **conjunto de até 9 números inteiros**.  
2️⃣ O código **validará a entrada** e processará o sinal.  
3️⃣ **Gráficos serão gerados** para exibir o **sinal original** e suas **transformações**.  
4️⃣ A análise dos **sistemas discretos** será exibida no **terminal**.  

---

## 🖥️ Exemplo de Uso
### Entrada do usuário:
```
Digite até 9 números inteiros separados por espaço: 0 -2 -1 0 1 2 3 0 0
```

### Saída esperada:
✅ **Gráficos gerados**:  
📌 Sinal **original**  
📌 Sinal **deslocado** \( x[n-2] \)  
📌 Sinal **refletido** \( x[-n] \)  
📌 Sinal **comprimido** \( x[2n] \)  

✅ **Análise exibida no terminal**:
```
Análise do Sistema: y[n] = x[n] - x[n-1]
  Causal: Sim
  Com memória: Sim
  Estável: Sim
  Invariante no tempo: Não
  Linear: Sim
----------------------------------------
Análise do Sistema: y[n] = soma acumulada de x[k]
  Causal: Sim
  Com memória: Sim
  Estável: Sim
  Invariante no tempo: Não
  Linear: Sim
----------------------------------------
Análise do Sistema: y[n] = x[2n]
  Causal: Sim
  Com memória: Não
  Estável: Sim
  Invariante no tempo: Sim
  Linear: Sim
----------------------------------------
```

---

## ⚠️ **Observações Importantes**
- O sinal de entrada **deve conter apenas números inteiros** entre **-9 e 9**.
- O sistema **assume comportamento causal** baseado em índices **não negativos**.
- O sistema de soma acumulada **é limitado ao tamanho do vetor fornecido**.
- A compressão temporal **pode descartar alguns valores**, dependendo do comprimento do vetor.

---

## 🤝 **Contribuindo**
Quer sugerir melhorias ou novas funcionalidades? Sinta-se à vontade para **fazer um fork** deste repositório e enviar um **pull request**! Se encontrar **bugs**, relate-os na seção **Issues** no GitHub. 📬

---

## 📜 **Licença**
Este projeto é **open-source** e está disponível sob a **Licença MIT**.

---