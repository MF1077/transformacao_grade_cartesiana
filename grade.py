"""
Módulo de Geração e Transformação de Grade Cartesiana

Este módulo fornece funções para gerar uma grade cartesiana regular
e aplicar transformações lineares a todos os pontos da grade.

A grade é representada como duas listas: linhas verticais e horizontais,
onde cada linha é uma lista de pontos [x, y].

"""

from typing import List, Tuple
from algebra import multiplicar_matriz_vetor


def gerar_grade(
    xmin: float = -5,
    xmax: float = 5,
    ymin: float = -5,
    ymax: float = 5,
    passo: float = 1
) -> Tuple[List[List[List[float]]], List[List[List[float]]]]:
    """
    Gera uma grade cartesiana regular com linhas verticais e horizontais.

    Args:
        xmin (float): Valor mínimo no eixo x. Padrão: -5.
        xmax (float): Valor máximo no eixo x. Padrão: 5.
        ymin (float): Valor mínimo no eixo y. Padrão: -5.
        ymax (float): Valor máximo no eixo y. Padrão: 5.
        passo (float): Espaçamento entre os pontos. Deve ser positivo. Padrão: 1.

    Returns:
        Tuple[List[List[List[float]]], List[List[List[float]]]]:
            - Primeira lista: linhas verticais (cada linha é uma lista de pontos [x, y])
            - Segunda lista: linhas horizontais (cada linha é uma lista de pontos [x, y])

    Raises:
        ValueError: Se o passo não for positivo.

    Examples:
        >>> vert, hor = gerar_grade(-2, 2, -2, 2, 1)
        >>> len(vert), len(hor)
        (5, 5)
    """
    if passo <= 0:
        raise ValueError("O passo deve ser um número positivo.")

    # Gera os valores dos eixos
    xs = [xmin + i * passo for i in range(int((xmax - xmin) / passo) + 1)]
    ys = [ymin + i * passo for i in range(int((ymax - ymin) / passo) + 1)]

    # Cria linhas verticais: para cada x, uma linha vertical com todos os y
    linhas_verticais = [[[x, y] for y in ys] for x in xs]

    # Cria linhas horizontais: para cada y, uma linha horizontal com todos os x
    linhas_horizontais = [[[x, y] for x in xs] for y in ys]

    return linhas_verticais, linhas_horizontais


def transformar_grade(
    M: List[List[float]],
    grade: Tuple[List[List[List[float]]], List[List[List[float]]]]
) -> Tuple[List[List[List[float]]], List[List[List[float]]]]:
    """
    Aplica uma transformação linear definida por uma matriz 2x2 a todos os pontos da grade.

    Args:
        M (List[List[float]]): Matriz 2x2 de transformação.
        grade (Tuple[List[List[List[float]]], List[List[List[float]]]]):
            Grade original retornada por gerar_grade().

    Returns:
        Tuple[List[List[List[float]]], List[List[List[float]]]]:
            Grade transformada com a mesma estrutura da original.

    Raises:
        ValueError: Propagado de multiplicar_matriz_vetor se a matriz não for 2x2.

    Examples:
        >>> grade_orig = gerar_grade(-1, 1, -1, 1, 1)
        >>> grade_transf = transformar_grade([[1, 0], [0, 1]], grade_orig)
        >>> grade_transf == grade_orig  # Matriz identidade
        True
    """
    linhas_verticais, linhas_horizontais = grade

    # Aplica a transformação a cada ponto de cada linha vertical
    grade_vert = [
        [multiplicar_matriz_vetor(M, ponto) for ponto in linha]
        for linha in linhas_verticais
    ]

    # Aplica a transformação a cada ponto de cada linha horizontal
    grade_hor = [
        [multiplicar_matriz_vetor(M, ponto) for ponto in linha]
        for linha in linhas_horizontais
    ]

    return grade_vert, grade_hor
