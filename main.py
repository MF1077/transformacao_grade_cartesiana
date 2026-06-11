"""
================================================================================
APLICAÇÃO: TRANSFORMAÇÃO DE GRADE CARTESIANA - INTERFACE DE CONSOLE
================================================================================

Demonstra transformações lineares aplicando uma matriz 2x2 a uma grade
cartesiana regular, mostrando os efeitos geométricos visualmente.

Fluxo de execução:
  1. Entrada dos coeficientes da matriz 2x2 (a, b, c, d)
  2. Cálculo do determinante e sua interpretação geométrica
  3. Geração de uma grade cartesiana regular
  4. Aplicação da transformação linear em todos os pontos
  5. Cálculo da transformação inversa (se existir)
  6. Exibição visual comparativa das grades

================================================================================
"""

from algebra import determinante_2x2, matriz_inversa_2x2
from grade import gerar_grade, transformar_grade
from visualizacao import plotar_grade, interpretar_determinante


# ============================================================================
# FUNÇÕES DE ENTRADA E VALIDAÇÃO
# ============================================================================

def ler_coordenada(nome: str) -> float:
    """
    Solicita ao usuário um valor numérico para um coeficiente da matriz.

    Valida a entrada e repete o prompt até obter um número válido.

    Args:
        nome (str): Nome do coeficiente (a, b, c, ou d).

    Returns:
        float: Valor numérico inserido pelo usuário.

    Raises:
        KeyboardInterrupt: Se o usuário pressionar Ctrl+C.
    """
    while True:
        try:
            valor = float(input(f"Digite o valor de {nome}: ").strip())
            return valor
        except ValueError:
            print("❌ Entrada inválida. Use um número real (ex: 1.0, -2.5)")
        except KeyboardInterrupt:
            print("\n⏹️  Execução interrompida pelo usuário.")
            raise


# ============================================================================
# FUNÇÕES AUXILIARES
# ============================================================================

def construir_matriz(a: float, b: float, c: float, d: float) -> list[list[float]]:
    """
    Constrói uma matriz 2x2 a partir dos coeficientes fornecidos.

    Estrutura:
        [ a  b ]
        [ c  d ]

    Args:
        a, b, c, d (float): Coeficientes da matriz.

    Returns:
        list[list[float]]: Matriz 2x2 como lista de listas.
    """
    return [[a, b], [c, d]]


def formatar_matriz(M: list[list[float]]) -> str:
    """
    Formata uma matriz 2x2 para exibição legível no console.

    Args:
        M (list[list[float]]): Matriz 2x2 a ser formatada.

    Returns:
        str: String com a representação formatada da matriz.
    """
    return "\n".join([f"[{row[0]:>7.3f} {row[1]:>7.3f}]" for row in M])


# ============================================================================
# FUNÇÃO PRINCIPAL
# ============================================================================

def main() -> None:
    """
    Função principal que orquestra toda a execução do programa.

    Etapas:
      1. Coleta os coeficientes da matriz do usuário
      2. Calcula e interpreta o determinante
      3. Gera uma grade cartesiana
      4. Aplica a transformação linear
      5. Calcula a inversa (se possível)
      6. Exibe as grades graficamente

    Trata exceções e oferece feedback ao usuário em cada etapa.
    """
    print("📐 === Transformação de Grade Cartesiana ===")
    print("🔢 Informe os coeficientes da matriz 2x2:\n")

    try:
        # ETAPA 1: Coleta dos coeficientes
        a = ler_coordenada("a")
        b = ler_coordenada("b")
        c = ler_coordenada("c")
        d = ler_coordenada("d")

        # ETAPA 2: Construção e exibição da matriz
        matriz = construir_matriz(a, b, c, d)
        print("\n📊 Matriz de transformação:")
        print(formatar_matriz(matriz))

        # ETAPA 3: Cálculo do determinante
        det = determinante_2x2(matriz)
        print(f"\n🔍 Determinante: {det:.6f}")
        print(f"📝 Interpretação: {interpretar_determinante(det)}")

        # ETAPA 4: Geração da grade original
        print("\n📐 Gerando grade cartesiana...")
        grade_original = gerar_grade(-5, 5, -5, 5, 1)

        # ETAPA 5: Aplicação da transformação
        print("🔄 Aplicando transformação linear...")
        grade_transformada = transformar_grade(matriz, grade_original)

        # ETAPA 6: Cálculo da transformação inversa (se possível)
        grade_inversa = None
        if abs(det) > 1e-12:
            inversa = matriz_inversa_2x2(matriz)
            print("\n🔄 Matriz inversa calculada:")
            print(formatar_matriz(inversa))
            grade_inversa = transformar_grade(inversa, grade_transformada)
        else:
            print("\n⚠️  Determinante nulo: transformação NÃO invertível.")
            print("   A transformação inversa não pode ser calculada.")

        # ETAPA 7: Exibição gráfica
        print("\n📈 Gerando visualização gráfica...")
        plotar_grade(grade_original, grade_transformada, det, grade_inversa)
        print("✅ Visualização concluída!")

    except KeyboardInterrupt:
        print("\n⏹️  Programa encerrado pelo usuário.")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")


# ============================================================================
# PONTO DE ENTRADA
# ============================================================================

if __name__ == "__main__":
    main()