"""
Transformação de Grade Cartesiana - Interface de Console

Este módulo fornece uma interface de linha de comando para demonstrar
a transformação de uma grade cartesiana através de uma matriz 2x2.

"""

from algebra import determinante_2x2, matriz_inversa_2x2
from grade import gerar_grade, transformar_grade
from visualizacao import plotar_grade, interpretar_determinante


def ler_coordenada(nome: str) -> float:
    """
    Solicita ao usuário um valor numérico para um coeficiente da matriz.

    Args:
        nome (str): Nome do coeficiente (a, b, c, d).

    Returns:
        float: Valor numérico inserido pelo usuário.

    Raises:
        KeyboardInterrupt: Se o usuário interromper a execução.
    """
    while True:
        try:
            valor = float(input(f"Digite o valor de {nome}: ").strip())
            return valor
        except ValueError:
            print("❌ Entrada inválida. Use um número real, por exemplo 1.0 ou -2.5.")
        except KeyboardInterrupt:
            print("\n⏹️  Execução interrompida pelo usuário.")
            raise


def construir_matriz(a: float, b: float, c: float, d: float) -> list[list[float]]:
    """
    Constrói uma matriz 2x2 a partir dos coeficientes fornecidos.

    Args:
        a, b, c, d (float): Coeficientes da matriz.

    Returns:
        list[list[float]]: Matriz 2x2 representada como lista de listas.
    """
    return [[a, b], [c, d]]


def formatar_matriz(M: list[list[float]]) -> str:
    """
    Formata uma matriz 2x2 para exibição no console.

    Args:
        M (list[list[float]]): Matriz 2x2 a ser formatada.

    Returns:
        str: Representação formatada da matriz.
    """
    return "\n".join([f"[{row[0]:>7.3f} {row[1]:>7.3f}]" for row in M])


def main() -> None:
    """
    Função principal que orquestra a execução do programa.

    Solicita os coeficientes da matriz ao usuário, calcula o determinante,
    gera e transforma a grade cartesiana, e exibe os resultados.
    """
    print("📐 === Transformação de Grade Cartesiana ===")
    print("🔢 Informe os coeficientes da matriz 2x2:")

    try:
        # Coleta dos coeficientes
        a = ler_coordenada("a")
        b = ler_coordenada("b")
        c = ler_coordenada("c")
        d = ler_coordenada("d")

        # Construção e exibição da matriz
        matriz = construir_matriz(a, b, c, d)
        print("\n📊 Matriz de transformação:")
        print(formatar_matriz(matriz))

        # Cálculo do determinante
        det = determinante_2x2(matriz)
        print(f"\n🔍 Determinante: {det:.6f}")
        print(f"📝 Interpretação: {interpretar_determinante(det)}")

        # Geração da grade original
        grade_original = gerar_grade(-5, 5, -5, 5, 1)

        # Aplicação da transformação
        grade_transformada = transformar_grade(matriz, grade_original)

        # Verificação da invertibilidade e cálculo da transformação inversa
        grade_inversa = None
        if abs(det) > 1e-12:
            inversa = matriz_inversa_2x2(matriz)
            print("\n🔄 Matriz inversa:")
            print(formatar_matriz(inversa))
            grade_inversa = transformar_grade(inversa, grade_transformada)
        else:
            print("\n⚠️  A matriz não é invertível e a transformação inversa não pode ser calculada.")

        # Exibição gráfica
        print("\n📈 Gerando visualização gráfica...")
        plotar_grade(grade_original, grade_transformada, det, grade_inversa)
        print("✅ Visualização concluída!")

    except KeyboardInterrupt:
        print("\n⏹️  Programa encerrado pelo usuário.")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")


if __name__ == "__main__":
    main()

    plotar_grade(grade_original, grade_transformada, det, grade_inversa)


if __name__ == "__main__":
    main()