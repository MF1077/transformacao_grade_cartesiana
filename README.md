# 📐 Transformação de Grade Cartesiana

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)]()

Uma aplicação interativa em Python que demonstra visualmente a deformação de uma grade cartesiana através da aplicação de uma matriz de transformação 2×2. Explore conceitos de álgebra linear de forma intuitiva com interface gráfica moderna e testes automatizados.

## ✨ Características

- 🔢 **Operações Matriciais**: Implementação manual de multiplicação matriz-vetor, determinantes e inversão de matrizes 2×2
- 🎨 **Design Moderno**: GUI com paleta de cores hoje em azul, branco e vermelho vibrante para tornar a experiência mais atraente
- 📊 **Visualização Gráfica**: Plotagem interativa da grade original e transformada usando Matplotlib
- 🖥️ **Interface Gráfica**: GUI elegante com Tkinter para entrada em tempo real e visualização aprimorada
- 🧪 **Testes Automatizados**: Cobertura completa com pytest para validação de funções
- 🔄 **Transformação Inversa**: Demonstração da reversibilidade quando a matriz é invertível

## 📁 Estrutura do Projeto

```
📦 Projeto_Transformacao_Grade_Cartesiana
├── 📄 algebra.py          # Operações matriciais e álgebra linear
├── 📄 grade.py            # Geração e transformação da grade cartesiana
├── 📄 visualizacao.py     # Funções de plotagem com Matplotlib
├── 📄 main.py             # Interface de console
├── 📄 gui.py              # Interface gráfica com Tkinter
├── 📁 tests/              # Testes automatizados
│   ├── 📄 test_algebra.py
│   └── 📄 test_grade.py
├── 📄 requirements.txt    # Dependências do projeto
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

## 🧪 Testes

Execute a suíte de testes para validar todas as funcionalidades:

```bash
pytest tests/ -v
```

Ou usando Python:

```bash
python -m pytest tests/ -v
```

## � Controle de Versão

Este projeto utiliza Git para controle de versão. O histórico de commits está organizado por funcionalidades:

- **Initial commit**: Estrutura básica, README, dependências e .gitignore
- **Core modules**: Módulos principais de álgebra, grade, visualização e console
- **Test suite**: Conjunto completo de testes automatizados
- **GUI interface**: Interface gráfica moderna com Tkinter

Para contribuir, siga as melhores práticas de Git:

```bash
git clone <repository-url>
cd Projeto_Transformacao_Grade_Cartesiana
git checkout -b feature/nova-funcionalidade
# Faça suas alterações
git add .
git commit -m "feat: descrição clara da mudança"
git push origin feature/nova-funcionalidade
```

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

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

> **Nota**: Para trabalho em grupo, consulte [TRABALHO_EM_GRUPO.md](TRABALHO_EM_GRUPO.md) para diretrizes detalhadas de divisão de tarefas, padrões de código e fluxo de trabalho colaborativo.

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🙋 Suporte

Se você tiver dúvidas ou encontrar problemas:

- Verifique os testes: `pytest tests/`
- Certifique-se de que todas as dependências estão instaladas
- Para problemas com a GUI, verifique se Tkinter está disponível no seu sistema Python

---
