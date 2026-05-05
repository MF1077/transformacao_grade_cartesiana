"""
Testes para o módulo grade.py

Este arquivo contém testes unitários para as funções de geração
e transformação de grades cartesianas.

Executar com: pytest tests/test_grade.py -v
"""

import pytest
import math
from grade import gerar_grade, transformar_grade


class TestGerarGrade:
    """Testes para a função gerar_grade."""

    def test_grade_basica(self):
        """Testa geração de grade básica."""
        grade = gerar_grade(-2, 2, -2, 2, 1)
        linhas_verticais, linhas_horizontais = grade

        # Verifica número de linhas
        assert len(linhas_verticais) == 5  # x: -2, -1, 0, 1, 2
        assert len(linhas_horizontais) == 5  # y: -2, -1, 0, 1, 2

        # Verifica conteúdo da primeira linha vertical
        assert linhas_verticais[0] == [[-2, -2], [-2, -1], [-2, 0], [-2, 1], [-2, 2]]

        # Verifica conteúdo da primeira linha horizontal
        assert linhas_horizontais[0] == [[-2, -2], [-1, -2], [0, -2], [1, -2], [2, -2]]

    def test_grade_passo_diferente(self):
        """Testa geração com passo diferente."""
        grade = gerar_grade(-1, 1, -1, 1, 0.5)
        vert, hor = grade

        # Com passo 0.5, de -1 a 1: -1, -0.5, 0, 0.5, 1 (5 pontos)
        assert len(vert) == 5
        assert len(hor) == 5

        # Verifica pontos da primeira linha vertical
        expected_vertical = [[-1, -1], [-1, -0.5], [-1, 0], [-1, 0.5], [-1, 1]]
        assert vert[0] == expected_vertical

    def test_grade_limites_iguais(self):
        """Testa grade com limites iguais (ponto único)."""
        grade = gerar_grade(0, 0, 0, 0, 1)
        vert, hor = grade

        assert len(vert) == 1
        assert len(hor) == 1
        assert vert[0] == [[0, 0]]
        assert hor[0] == [[0, 0]]

    def test_passo_negativo(self):
        """Testa erro com passo negativo."""
        with pytest.raises(ValueError, match="positivo"):
            gerar_grade(passo=-1)

    def test_passo_zero(self):
        """Testa erro com passo zero."""
        with pytest.raises(ValueError, match="positivo"):
            gerar_grade(passo=0)

    def test_passo_muito_pequeno(self):
        """Testa com passo muito pequeno (deve funcionar, mas pode ser lento)."""
        grade = gerar_grade(-1, 1, -1, 1, 0.1)
        vert, hor = grade

        # Deve ter 21 pontos (de -1 a 1 com passo 0.1)
        assert len(vert) == 21
        assert len(hor) == 21


class TestTransformarGrade:
    """Testes para a função transformar_grade."""

    def test_matriz_identidade(self):
        """Testa transformação com matriz identidade (sem mudança)."""
        M = [[1, 0], [0, 1]]
        grade_original = gerar_grade(-1, 1, -1, 1, 1)
        grade_transformada = transformar_grade(M, grade_original)

        # Deve ser idêntica à original
        assert grade_transformada == grade_original

    def test_matriz_escala(self):
        """Testa transformação de escala."""
        M = [[2, 0], [0, 0.5]]  # Escala x2 horizontal, x0.5 vertical
        grade_original = gerar_grade(0, 1, 0, 1, 1)
        grade_transformada = transformar_grade(M, grade_original)

        vert, hor = grade_transformada

        # (1, 0) -> (2, 0)
        linha_vertical_x1 = vert[1]  # x=1
        ponto_y0 = linha_vertical_x1[0]  # y=0
        assert abs(ponto_y0[0] - 2.0) < 1e-10  # x deve ser 2
        assert abs(ponto_y0[1] - 0.0) < 1e-10  # y deve ser 0

    def test_rotacao_90_graus(self):
        """Testa rotação de 90 graus no sentido anti-horário."""
        theta = math.pi / 2
        M = [[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]]
        grade_original = gerar_grade(0, 1, 0, 1, 1)
        grade_transformada = transformar_grade(M, grade_original)

        vert, hor = grade_transformada

        # (1, 0) -> (0, 1)
        linha_vertical_x1 = vert[1]  # x=1 (original)
        ponto_y0 = linha_vertical_x1[0]  # y=0 (original)
        assert abs(ponto_y0[0] - 0.0) < 1e-10  # x deve ser 0
        assert abs(ponto_y0[1] - 1.0) < 1e-10  # y deve ser 1

    def test_reflexao_sobre_x(self):
        """Testa reflexão sobre o eixo x."""
        M = [[1, 0], [0, -1]]  # Reflexão: y -> -y
        grade_original = gerar_grade(0, 1, 0, 1, 1)
        grade_transformada = transformar_grade(M, grade_original)

        vert, hor = grade_transformada

        # (0, 1) -> (0, -1)
        linha_vertical_x0 = vert[0]  # x=0
        ponto_y1 = linha_vertical_x0[1]  # y=1
        assert abs(ponto_y1[0] - 0.0) < 1e-10  # x deve ser 0
        assert abs(ponto_y1[1] - (-1.0)) < 1e-10  # y deve ser -1

    def test_cisalhamento(self):
        """Testa transformação de cisalhamento."""
        M = [[1, 1], [0, 1]]  # Cisalhamento horizontal
        grade_original = gerar_grade(0, 1, 0, 1, 1)
        grade_transformada = transformar_grade(M, grade_original)

        vert, hor = grade_transformada

        # (0, 1) -> (1, 1) (adiciona x ao longo de y)
        linha_vertical_x0 = vert[0]  # x=0
        ponto_y1 = linha_vertical_x0[1]  # y=1
        assert abs(ponto_y1[0] - 1.0) < 1e-10  # x deve ser 1
        assert abs(ponto_y1[1] - 1.0) < 1e-10  # y deve ser 1

    def test_matriz_zero(self):
        """Testa transformação com matriz zero (colapsa tudo na origem)."""
        M = [[0, 0], [0, 0]]
        grade_original = gerar_grade(-1, 1, -1, 1, 1)
        grade_transformada = transformar_grade(M, grade_original)

        vert, hor = grade_transformada

        # Todos os pontos devem ir para (0, 0)
        for linha in vert + hor:
            for ponto in linha:
                assert abs(ponto[0] - 0.0) < 1e-10
                assert abs(ponto[1] - 0.0) < 1e-10

    def test_grade_vazia(self):
        """Testa transformação de grade com limites que geram grade vazia."""
        # Nota: gerar_grade com limites iguais cria grade mínima
        M = [[1, 0], [0, 1]]
        grade_original = gerar_grade(0, 0, 0, 0, 1)
        grade_transformada = transformar_grade(M, grade_original)

        # Deve manter a estrutura
        assert len(grade_transformada[0]) == 1
        assert len(grade_transformada[1]) == 1
        assert grade_transformada[0][0] == [[0, 0]]
        assert grade_transformada[1][0] == [[0, 0]]