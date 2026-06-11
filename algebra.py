"""
Módulo de Álgebra Linear

Este módulo implementa operações matriciais fundamentais para o projeto
de transformação de grade cartesiana, incluindo multiplicação de matrizes,
cálculo de determinantes, resolução de sistemas lineares e inversão de matrizes.

Todas as funções incluem validação de entrada e tratamento de erros.

"""

from typing import List


def multiplicar_matriz_vetor(M: List[List[float]], v: List[float]) -> List[float]:
    """
    Aplica a transformação linear definida por uma matriz 2x2 a um vetor 2D.

    Args:
        M (List[List[float]]): Matriz 2x2 de transformação.
        v (List[float]): Vetor 2D a ser transformado.

    Returns:
        List[float]: Vetor resultante da transformação.

    Raises:
        ValueError: Se a matriz não for 2x2 ou o vetor não tiver 2 elementos.

    Examples:
        >>> multiplicar_matriz_vetor([[1, 0], [0, 1]], [2, 3])
        [2.0, 3.0]
    """
    if len(M) != 2 or len(M[0]) != 2 or len(M[1]) != 2 or len(v) != 2:
        raise ValueError("A matriz deve ser 2x2 e o vetor deve ter 2 elementos.")

    x = M[0][0] * v[0] + M[0][1] * v[1]
    y = M[1][0] * v[0] + M[1][1] * v[1]
    return [x, y]


def multiplicar_matrizes(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
    """
    Multiplica duas matrizes 2x2 usando o algoritmo padrão de multiplicação matricial.

    Args:
        A (List[List[float]]): Primeira matriz 2x2.
        B (List[List[float]]): Segunda matriz 2x2.

    Returns:
        List[List[float]]: Produto das duas matrizes.

    Raises:
        ValueError: Se as matrizes não forem 2x2.

    Examples:
        >>> multiplicar_matrizes([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        [[19.0, 22.0], [43.0, 50.0]]
    """
    if (len(A) != 2 or len(B) != 2 or
        len(A[0]) != 2 or len(A[1]) != 2 or
        len(B[0]) != 2 or len(B[1]) != 2):
        raise ValueError("Ambas as matrizes devem ser 2x2.")

    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]],
    ]


def determinante_2x2(M: List[List[float]]) -> float:
    """
    Calcula o determinante de uma matriz 2x2 usando a fórmula padrão.

    Args:
        M (List[List[float]]): Matriz 2x2.

    Returns:
        float: Valor do determinante.

    Raises:
        ValueError: Se a matriz não for 2x2.

    Examples:
        >>> determinante_2x2([[1, 2], [3, 4]])
        -2.0
    """
    if len(M) != 2 or len(M[0]) != 2 or len(M[1]) != 2:
        raise ValueError("A matriz deve ser 2x2.")
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]


def determinante_3x3(M: List[List[float]]) -> float:
    """
    Calcula o determinante de uma matriz 3x3 usando expansão de Laplace.

    Args:
        M (List[List[float]]): Matriz 3x3.

    Returns:
        float: Valor do determinante.

    Raises:
        ValueError: Se a matriz não for 3x3.

    Examples:
        >>> determinante_3x3([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        0.0
    """
    if len(M) != 3 or any(len(row) != 3 for row in M):
        raise ValueError("A matriz deve ser 3x3.")

    a, b, c = M[0]
    d, e, f = M[1]
    g, h, i = M[2]

    return (
        a * (e * i - f * h)
        - b * (d * i - f * g)
        + c * (d * h - e * g)
    )


def eliminacao_gauss(A: List[List[float]], b: List[float]) -> List[float]:
    """
    Resolve um sistema linear Ax = b usando eliminação de Gauss com pivoteamento parcial.

    Args:
        A (List[List[float]]): Matriz quadrada dos coeficientes.
        b (List[float]): Vetor dos termos independentes.

    Returns:
        List[float]: Solução do sistema linear.

    Raises:
        ValueError: Se a matriz não for quadrada, b não tiver o tamanho correto,
                   ou o sistema for singular/quase singular.

    Examples:
        >>> eliminacao_gauss([[2, 1], [1, 1]], [3, 2])
        [1.0, 1.0]
    """
    n = len(A)
    if n == 0 or any(len(row) != n for row in A) or len(b) != n:
        raise ValueError("A deve ser uma matriz quadrada e b deve ter o mesmo tamanho.")

    # Cria a matriz aumentada [A|b]
    M = [list(row) + [float(b[i])] for i, row in enumerate(A)]

    # Eliminação para frente com pivoteamento parcial
    for k in range(n):
        # Encontra o pivô com maior valor absoluto na coluna k
        pivot = max(range(k, n), key=lambda i: abs(M[i][k]))

        if abs(M[pivot][k]) < 1e-12:
            raise ValueError("Sistema singular ou quase singular.")

        # Troca linhas se necessário
        if pivot != k:
            M[k], M[pivot] = M[pivot], M[k]

        # Eliminação
        for i in range(k + 1, n):
            fator = M[i][k] / M[k][k]
            for j in range(k, n + 1):
                M[i][j] -= fator * M[k][j]

    # Substituição para trás
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        soma = M[i][n]
        for j in range(i + 1, n):
            soma -= M[i][j] * x[j]
        x[i] = soma / M[i][i]

    return x


def matriz_inversa_2x2(M: List[List[float]]) -> List[List[float]]:
    """
    Calcula a inversa de uma matriz 2x2 usando a fórmula analítica.

    Args:
        M (List[List[float]]): Matriz 2x2 a ser invertida.

    Returns:
        List[List[float]]: Matriz inversa.

    Raises:
        ValueError: Se a matriz não for 2x2 ou não for invertível.

    Examples:
        >>> matriz_inversa_2x2([[1, 2], [3, 4]])
        [[-2.0, 1.0], [1.5, -0.5]]
    """
    det = determinante_2x2(M)
    if abs(det) < 1e-12:
        raise ValueError("A matriz não é invertível (determinante zero ou próximo de zero).")

    return [
        [M[1][1] / det, -M[0][1] / det],
        [-M[1][0] / det, M[0][0] / det],
    ]
