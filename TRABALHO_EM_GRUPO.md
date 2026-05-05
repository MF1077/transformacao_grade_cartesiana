# 👥 Guia de Trabalho em Grupo - Transformação de Grade Cartesiana

## 📋 Resumo do Projeto

Este projeto demonstra visualmente como uma grade cartesiana se deforma quando submetida a uma transformação linear representada por uma matriz 2×2. É uma ferramenta educacional interativa para aprender álgebra linear.

### Objetivo Principal
Criar uma aplicação Python profissional que:
- Implemente operações de álgebra linear manualmente
- Visualize transformações de forma intuitiva
- Forneça interface gráfica moderna e intuitiva
- Inclua testes automatizados completos

---

## 👨‍💼 Divisão de Tarefas e Responsabilidades

### 1️⃣ **Núcleo Matemático** (algebra.py e grade.py)
**Responsáveis**: Quem trabalha com lógica matemática

**Tarefas**:
- ✅ Implementar operações matriciais (multiplicação, determinante, inversão)
- ✅ Gerar e transformar grades cartesianas
- ✅ Validar entradas matemáticas
- ✅ Otimizar cálculos

**Checklist**:
- [ ] Testar todas as funções manualmente
- [ ] Verificar edge cases (matrizes singulares, valores extremos)
- [ ] Documentar fórmulas matemáticas usadas
- [ ] Adicionar exemplos de uso nas docstrings

---

### 2️⃣ **Visualização e Gráficos** (visualizacao.py)
**Responsáveis**: Quem trabalha com matplotlib e design visual

**Tarefas**:
- ✅ Plotar grades original e transformada
- ✅ Visualizar grades inversas
- ✅ Mostrar interpretação do determinante
- ✅ Melhorar estética dos gráficos

**Checklist**:
- [ ] Testar diferentes matrizes de transformação
- [ ] Ajustar cores e estilos
- [ ] Garantir que legendas não sobreponham o gráfico
- [ ] Adicionar mais informações visuais úteis

---

### 3️⃣ **Interface de Usuário** (gui.py e main.py)
**Responsáveis**: Quem trabalha com interfaces e UX

**Tarefas**:
- ✅ Criar interface gráfica em Tkinter
- ✅ Implementar validação de entrada
- ✅ Integrar plotagem com Matplotlib
- ✅ Desenvolver console interativo

**Checklist**:
- [ ] Testar usabilidade com diferentes tipos de entrada
- [ ] Melhorar feedback do usuário (mensagens, cores)
- [ ] Tornar interface responsiva
- [ ] Adicionar teclas de atalho

---

### 4️⃣ **Testes e Qualidade** (tests/)
**Responsáveis**: Quem trabalha com garantia de qualidade

**Tarefas**:
- ✅ Escrever testes unitários para cada função
- ✅ Testar casos extremos e erros
- ✅ Manter cobertura de testes alta (>90%)
- ✅ Validar casos de uso reais

**Checklist**:
- [ ] Todos os testes passam (`pytest tests/ -v`)
- [ ] Cobertura de código >90%
- [ ] Testes documentados com comentários
- [ ] Adicionar testes de integração

---

### 5️⃣ **Documentação e Git** (README.md, commits, etc.)
**Responsáveis**: Quem organiza o projeto e documentação

**Tarefas**:
- ✅ Manter README atualizado
- ✅ Organizar commits de forma clara
- ✅ Documentar mudanças
- ✅ Criar guias de contribuição

**Checklist**:
- [ ] README reflete estado atual do projeto
- [ ] Cada commit tem mensagem clara
- [ ] Histórico Git é linear e compreensível
- [ ] CHANGELOG.md atualizado

---

## 🔄 Fluxo de Trabalho

### Fase 1: Planejamento
1. Ler e entender este documento
2. Escolher sua área de responsabilidade
3. Revisar o código existente
4. Criar issues (tarefas) no projeto

### Fase 2: Desenvolvimento
1. Criar uma branch para sua tarefa:
   ```bash
   git checkout -b feature/meu-melhoramento
   ```

2. Fazer alterações no seu código:
   - Manter os comentários atualizados
   - Seguir o padrão de código existente
   - Testar frequentemente

3. Adicionar ou atualizar testes:
   ```bash
   pytest tests/ -v
   ```

4. Fazer commits com mensagens descritivas:
   ```bash
   git commit -m "feat: adiciona validação de matriz singular"
   ```

### Fase 3: Revisão e Integração
1. Fazer push da branch:
   ```bash
   git push origin feature/meu-melhoramento
   ```

2. Criar um Pull Request
3. Aguardar revisão dos colegas
4. Fazer ajustes se necessário
5. Merge para main branch

### Fase 4: Deploy
1. Executar todos os testes
2. Atualizar documentação
3. Criar commit final de release
4. Testar a aplicação completa

---

## 📝 Padrões de Código

### 1. **Docstrings (Documentação de Funções)**
Todas as funções devem ter docstring seguindo o padrão Google:

```python
def exemplo_funcao(parametro1: str, parametro2: int) -> bool:
    """
    Descrição breve do que a função faz.

    Descrição mais detalhada se necessário, explicando o algoritmo
    ou lógica especial usada.

    Args:
        parametro1 (str): Descrição do primeiro parâmetro.
        parametro2 (int): Descrição do segundo parâmetro.

    Returns:
        bool: Descrição do valor retornado.

    Raises:
        ValueError: Quando X acontece.
        TypeError: Quando Y acontece.

    Examples:
        >>> exemplo_funcao("teste", 42)
        True
    """
    pass
```

### 2. **Type Hints (Dicas de Tipo)**
Use type hints em todas as funções:

```python
def processar(dados: List[float], iteracoes: int) -> Dict[str, Any]:
    """Processa dados numericamente."""
    pass
```

### 3. **Comentários Inline**
Use para lógica complexa:

```python
# Normalizar o vetor dividindo pela norma euclidiana
norma = (x**2 + y**2) ** 0.5
x_norm = x / norma
y_norm = y / norma
```

### 4. **Nomenclatura**
- Variáveis: `snake_case` → `matriz_transformacao`
- Classes: `PascalCase` → `TransformacaoApp`
- Constantes: `UPPER_SNAKE_CASE` → `MAX_ITERACOES`
- Funções privadas: `_funcao_interna()`

### 5. **Formatação**
- Máximo 100 caracteres por linha
- Espaçamento com 4 espaços
- Linhas em branco entre seções lógicas

---

## ✅ Checklist de Qualidade

Antes de fazer commit, verifique:

- [ ] Código segue padrões (Black, PEP 8)
- [ ] Todas as funções têm docstrings
- [ ] Type hints em todos os parâmetros e returns
- [ ] Testes cobrem a funcionalidade
- [ ] Comentários explicam lógica complexa
- [ ] Sem erros de sintaxe
- [ ] Sem warnings do linter
- [ ] Mensagem de commit é clara

---

## 🚀 Comandos Úteis

### Executar testes
```bash
pytest tests/ -v
pytest tests/test_algebra.py -v  # Teste específico
pytest tests/ --cov              # Com cobertura
```

### Verificar estilo do código
```bash
black . --check
pylint *.py
flake8 .
```

### Executar a aplicação
```bash
python gui.py      # Interface gráfica
python main.py     # Interface console
```

### Trabalhar com Git
```bash
git status                              # Ver status
git log --oneline                       # Ver histórico
git diff                                # Ver mudanças
git add arquivo.py                      # Adicionar arquivo
git commit -m "mensagem descritiva"     # Fazer commit
git push origin branch-name             # Enviar para remoto
```

---

## 📞 Comunicação da Equipe

### Canais de Comunicação
- 💬 **Reuniões**: Segundas e Quartas (defina horário)
- 📧 **Email**: Para questões não urgentes
- 💻 **GitHub Issues**: Para bugs e tarefas
- 📋 **Trello/Jira**: Para organizar sprints (opcional)

### Reuniões de Status
**Frequência**: 2x por semana
**Duração**: 15 minutos
**Agenda**:
1. O que foi feito desde última reunião
2. Bloqueadores/dúvidas
3. Próximas prioridades

### Regras de Revisão de Código
- Mínimo 1 aprovação antes de merge
- Verificar testes passando
- Resolver conflitos localmente
- Deixar feedback construtivo

---

## 📊 Progresso do Projeto

### Versão 1.0 (Atual)
- ✅ Operações matriciais básicas
- ✅ Geração de grades
- ✅ Visualização com Matplotlib
- ✅ Interface gráfica com Tkinter
- ✅ Testes automatizados
- ✅ Documentação completa

### Versão 1.1 (Planejado)
- 🔲 Suporte para matrizes 3×3
- 🔲 Animações de transformação
- 🔲 Exportação de gráficos
- 🔲 Histórico de transformações

### Versão 2.0 (Futuro)
- 🔲 Aplicação web (Flask/Django)
- 🔲 Suporte para matrizes NxN
- 🔲 Cálculos simbólicos
- 🔲 Integração com SymPy

---

## 🎓 Recursos de Aprendizado

### Álgebra Linear
- [3Blue1Brown - Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
- [Khan Academy - Linear Algebra](https://www.khanacademy.org/math/linear-algebra)

### Python
- [Real Python - Type Hints](https://realpython.com/python-type-hints/)
- [PEP 8 Style Guide](https://pep8.org/)

### Git
- [Pro Git Book](https://git-scm.com/book)
- [GitHub Skills](https://skills.github.com/)

---

## ❓ FAQ - Perguntas Frequentes

**P: Como começo?**
R: Leia o README.md, escolha sua área, e comece com tarefas pequenas.

**P: E se eu cometer um erro?**
R: Sem problema! Use `git revert` ou `git reset`. Todos aprendem.

**P: Posso mudar de área durante o projeto?**
R: Sim! Comunique ao time e faça handover das tarefas.

**P: Como reportar um bug?**
R: Abra uma issue no GitHub com título claro e passos para reproduzir.

**P: Quanto tempo deve levar cada tarefa?**
R: Tarefas simples (2-4h), médias (1-2 dias), complexas (3+ dias).

---

## 📞 Contato e Suporte

**Líder do Projeto**: [Nome]  
**Email**: [Email]  
**Horário Disponível**: [Horário]

---

**Versão**: 1.0  
**Data da Última Atualização**: 05/05/2026  
**Próxima Revisão**: 31/05/2026

---

**Desenvolvido com ❤️ para aprendizado colaborativo em álgebra linear!**
