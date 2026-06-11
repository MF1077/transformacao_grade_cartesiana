"""
================================================================================
TESTES UNITÁRIOS: MÓDULO DE ÁLGEBRA LINEAR
================================================================================

Testes abrangentes para todas as funções do módulo algebra.py.

Cobertura:
  • Multiplicação de matriz por vetor
  • Multiplicação de matrizes 2x2
  • Cálculo de determinantes (2x2 e 3x3)
  • Solução de sistemas lineares (eliminação de Gauss)
  • Inversão de matrizes 2x2

Tipos de testes:
  • Casos normais (entrada válida)
  • Casos extremos (valores especiais)
  • Validação de erros (entrada inválida)

Executar com:
  $ pytest tests/test_algebra.py -v
  $ pytest tests/test_algebra.py --cov=algebra  # Com cobertura

================================================================================
"""

import pytest
import math
from algebra import (
    multiplicar_matriz_vetor,
    multiplicar_matrizes,
    determinante_2x2,
    determinante_3x3,
    eliminacao_gauss,
    matriz_inversa_2x2,
)


# ============================================================================
# TESTES: MULTIPLICAÇÃO DE MATRIZ POR VETOR
# ============================================================================

class TestMultiplicarMatrizVetor:
    """Testes para a função multiplicar_matriz_vetor."""

    def test_caso_basico(self):
        """Testa multiplicação básica matriz-vetor."""
        M = [[1, 2], [3, 4]]
        v = [5, 6]
        result = multiplicar_matriz_vetor(M, v)
        expected = [17, 39]  # 1*5 + 2*6 = 17, 3*5 + 4*6 = 39
        assert result == expected

    def test_matriz_identidade(self):
        """Testa com matriz identidade."""
        M = [[1, 0], [0, 1]]
        v = [3, 7]
        result = multiplicar_matriz_vetor(M, v)
        assert result == v

    def test_matriz_invalida_tamanho(self):
        """Testa erro com matriz de tamanho inválido."""
        with pytest.raises(ValueError, match="A matriz deve ser 2x2"):
            multiplicar_matriz_vetor([[1, 2]], [1, 2])

    def test_vetor_invalido_tamanho(self):
        """Testa erro com vetor de tamanho inválido."""
        with pytest.raises(ValueError, match="o vetor deve ter 2 elementos"):
            multiplicar_matriz_vetor([[1, 2], [3, 4]], [1])

    def test_valores_negativos(self):
        """Testa com valores negativos."""
        M = [[-1, 2], [3, -4]]
        v = [-5, 6]
        result = multiplicar_matriz_vetor(M, v)
        expected = [17, -39]  # -1*(-5) + 2*6 = 5 + 12 = 17, 3*(-5) + (-4)*6 = -15 -24 = -39
        assert result == expected


class TestMultiplicarMatrizes:
    """Testes para a função multiplicar_matrizes."""

    def test_caso_basico(self):
        """Testa multiplicação básica de matrizes."""
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        result = multiplicar_matrizes(A, B)
        expected = [[19, 22], [43, 50]]
        assert result == expected

    def test_matriz_identidade(self):
        """Testa multiplicação por identidade."""
        A = [[2, 3], [4, 5]]
        I = [[1, 0], [0, 1]]
        result = multiplicar_matrizes(A, I)
        assert result == A

    def test_matriz_zero(self):
        """Testa multiplicação por matriz zero."""
        A = [[1, 2], [3, 4]]
        Z = [[0, 0], [0, 0]]
        result = multiplicar_matrizes(A, Z)
        expected = [[0, 0], [0, 0]]
        assert result == expected

    def test_matriz_a_invalida(self):
        """Testa erro com primeira matriz inválida."""
        with pytest.raises(ValueError, match="devem ser 2x2"):
            multiplicar_matrizes([[1]], [[1, 2], [3, 4]])

    def test_matriz_b_invalida(self):
        """Testa erro com segunda matriz inválida."""
        with pytest.raises(ValueError, match="devem ser 2x2"):
            multiplicar_matrizes([[1, 2], [3, 4]], [[1]])


class TestDeterminante2x2:
    """Testes para a função determinante_2x2."""

    def test_caso_basico(self):
        """Testa determinante básico."""
        M = [[1, 2], [3, 4]]
        result = determinante_2x2(M)
        expected = -2  # 1*4 - 2*3
        assert result == expected

    def test_matriz_identidade(self):
        """Testa determinante da identidade."""
        M = [[1, 0], [0, 1]]
        result = determinante_2x2(M)
        assert result == 1

    def test_matriz_singular(self):
        """Testa determinante de matriz singular."""
        M = [[2, 4], [1, 2]]
        result = determinante_2x2(M)
        assert result == 0  # 2*2 - 4*1 = 0

    def test_valores_negativos(self):
        """Testa com valores negativos."""
        M = [[-1, 2], [3, -4]]
        result = determinante_2x2(M)
        expected = 4 - 6  # (-1)*(-4) - 2*3 = 4 - 6 = -2
        assert result == expected

    def test_matriz_invalida(self):
        """Testa erro com matriz não 2x2."""
        with pytest.raises(ValueError, match="deve ser 2x2"):
            determinante_2x2([[1, 2, 3], [4, 5, 6]])


class TestDeterminante3x3:
    """Testes para a função determinante_3x3."""

    def test_matriz_singular(self):
        """Testa determinante de matriz singular conhecida."""
        M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = determinante_3x3(M)
        assert result == 0

    def test_matriz_identidade(self):
        """Testa determinante da identidade 3x3."""
        M = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        result = determinante_3x3(M)
        assert result == 1

    def test_caso_basico(self):
        """Testa determinante de matriz 3x3."""
        M = [[2, 1, 1], [1, 2, 1], [1, 1, 2]]
        result = determinante_3x3(M)
        expected = 4  # Calculado: 2*(4-1) - 1*(2-1) + 1*(1-2) = 6 - 1 - 1 = 4
        assert result == expected

    def test_matriz_invalida_tamanho(self):
        """Testa erro com matriz de tamanho incorreto."""
        with pytest.raises(ValueError, match="deve ser 3x3"):
            determinante_3x3([[1, 2], [3, 4]])

    def test_matriz_invalida_linha(self):
        """Testa erro com linha de tamanho incorreto."""
        with pytest.raises(ValueError, match="deve ser 3x3"):
            determinante_3x3([[1, 2, 3], [4, 5], [7, 8, 9]])


class TestEliminacaoGauss:
    """Testes para a função eliminacao_gauss."""

    def test_sistema_basico(self):
        """Testa resolução de sistema linear básico."""
        A = [[2, 1], [1, 1]]
        b = [3, 2]
        result = eliminacao_gauss(A, b)
        expected = [1, 1]  # Solução: x = 1, y = 1
        assert all(abs(r - e) < 1e-10 for r, e in zip(result, expected))

    def test_sistema_3x3(self):
        """Testa sistema 3x3."""
        A = [[1, 1, 1], [2, 1, 3], [3, 2, 1]]
        b = [6, 10, 8]
        result = eliminacao_gauss(A, b)
        expected = [-4/3, 14/3, 8/3]  # Solução calculada
        assert all(abs(r - e) < 1e-10 for r, e in zip(result, expected))

    def test_sistema_singular(self):
        """Testa erro com sistema singular."""
        A = [[1, 1], [1, 1]]
        b = [2, 3]
        with pytest.raises(ValueError, match="singular"):
            eliminacao_gauss(A, b)

    def test_matriz_nao_quadrada(self):
        """Testa erro com matriz não quadrada."""
        A = [[1, 2, 3], [4, 5, 6]]
        b = [1, 2]
        with pytest.raises(ValueError, match="quadrada"):
            eliminacao_gauss(A, b)

    def test_vetor_b_tamanho_incorreto(self):
        """Testa erro com vetor b de tamanho incorreto."""
        A = [[1, 2], [3, 4]]
        b = [1, 2, 3]
        with pytest.raises(ValueError, match="mesmo tamanho"):
            eliminacao_gauss(A, b)


class TestMatrizInversa2x2:
    """Testes para a função matriz_inversa_2x2."""

    def test_matriz_basica(self):
        """Testa inversa de matriz básica."""
        M = [[1, 2], [3, 4]]
        result = matriz_inversa_2x2(M)
        expected = [[-2, 1], [1.5, -0.5]]
        assert all(
            abs(r - e) < 1e-10
            for row_r, row_e in zip(result, expected)
            for r, e in zip(row_r, row_e)
        )

    def test_matriz_identidade(self):
        """Testa inversa da identidade."""
        M = [[1, 0], [0, 1]]
        result = matriz_inversa_2x2(M)
        assert result == M

    def test_verificacao_inversa(self):
        """Testa que M * M^(-1) = I."""
        M = [[4, 7], [2, 6]]
        inv = matriz_inversa_2x2(M)
        produto = multiplicar_matrizes(M, inv)
        identidade = [[1, 0], [0, 1]]

        for i in range(2):
            for j in range(2):
                assert abs(produto[i][j] - identidade[i][j]) < 1e-10

    def test_matriz_singular(self):
        """Testa erro com matriz singular."""
        M = [[1, 1], [1, 1]]
        with pytest.raises(ValueError, match="não é invertível"):
            matriz_inversa_2x2(M)

    def test_determinante_zero(self):
        """Testa erro com determinante zero."""
        M = [[2, 4], [1, 2]]
        with pytest.raises(ValueError, match="não é invertível"):
            matriz_inversa_2x2(M)

    def test_matriz_invalida(self):
        """Testa erro com matriz não 2x2."""
        with pytest.raises(ValueError, match="deve ser 2x2"):
            matriz_inversa_2x2([[1, 2, 3], [4, 5, 6]])