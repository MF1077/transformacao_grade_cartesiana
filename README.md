# 📐 Transformação de Grade Cartesiana

Uma aplicação interativa em Python que demonstra visualmente a deformação de uma grade cartesiana através da aplicação de uma matriz de transformação 2×2. Explore conceitos de álgebra linear de forma intuitiva com interface gráfica moderna.

## ✨ Características

- 🔢 **Operações Matriciais**: Implementação manual de multiplicação matriz-vetor, determinantes e inversão de matrizes 2×2
- 🎨 **Design Moderno**: GUI com paleta de cores hoje em azul, branco e vermelho vibrante para tornar a experiência mais atraente
- 📊 **Visualização Gráfica**: Plotagem interativa da grade original e transformada usando Matplotlib
- 🖥️ **Interface Gráfica**: GUI elegante com Tkinter para entrada em tempo real e visualização aprimorada
- 🔄 **Transformação Inversa**: Demonstração da reversibilidade quando a matriz é invertível

## 📁 Estrutura do Projeto

```
📦 Projeto_Transformacao_Grade_Cartesiana
├── 📄 algebra.py          # Operações matriciais e álgebra linear
├── 📄 grade.py            # Geração e transformação da grade cartesiana
├── 📄 visualizacao.py     # Funções de plotagem com Matplotlib
├── 📄 main.py             # Interface de console
├── 📄 gui.py              # Interface gráfica com Tkinter
├──  requirements.txt    # Dependências do projeto
├── 📄 README.md           # Este arquivo
└── 📄 TRABALHO_EM_GRUPO.md # Guia para desenvolvimento colaborativo
```

## 🚀 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos de Instalação

1. **Clone ou baixe o repositório** (se aplicável)

2. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Uso

### Interface Gráfica (Recomendada)

Para uma experiência interativa e visual:

```bash
python gui.py
```

- Insira os coeficientes `a`, `b`, `c`, `d` da matriz 2×2 nos campos
- Clique em "Calcular e Plotar" para visualizar a transformação
- Observe a grade original (azul) e transformada (vermelha) em tempo real

### Interface de Console

Para uso programático ou em ambientes sem GUI:

```bash
python main.py
```

- Digite os valores solicitados no terminal
- A visualização será exibida em uma janela separada


## �📖 Exemplos de Uso

### Matriz Identidade
```
a = 1, b = 0
c = 0, d = 1
```
Resultado: Grade permanece inalterada.

### Rotação de 90°
```
a = 0, b = -1
c = 1, d = 0
```
Resultado: Grade rotacionada no sentido anti-horário.

### Escala
```
a = 2, b = 0
c = 0, d = 0.5
```
Resultado: Grade alongada horizontalmente e comprimida verticalmente.

