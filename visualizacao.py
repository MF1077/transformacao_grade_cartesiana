"""
Módulo de Visualização Gráfica

Este módulo fornece funções para interpretar determinantes e criar
visualizações gráficas das grades cartesianas usando Matplotlib.

As funções geram plots interativos mostrando a grade original,
transformada e, quando possível, a transformação inversa.

"""

import matplotlib.pyplot as plt
from typing import List, Optional, Tuple


def interpretar_determinante(det: float) -> str:
    """
    Interpreta o valor do determinante em termos geométricos.

    Args:
        det (float): Valor do determinante da matriz de transformação.

    Returns:
        str: Descrição do efeito da transformação baseado no determinante.

    Examples:
        >>> interpretar_determinante(2.0)
        'Área preservada com orientação mantida: expansão ou contração sem inversão.'

        >>> interpretar_determinante(0.0)
        'Área colapsada: transformação não invertível.'
    """
    if abs(det) < 1e-12:
        return "Área colapsada: transformação não invertível."
    elif det > 0:
        return "Área preservada com orientação mantida: expansão ou contração sem inversão."
    else:
        return "Área preservada com orientação invertida: reflexão ou inversão de orientação."


def plotar_grade(
    original: Tuple[List[List[List[float]]], List[List[List[float]]]],
    transformada: Tuple[List[List[List[float]]], List[List[List[float]]]],
    det: float,
    inversa: Optional[Tuple[List[List[List[float]]], List[List[List[float]]]]] = None
) -> None:
    """
    Cria e exibe um plot comparativo das grades original e transformada.

    Args:
        original (Tuple[List[List[List[float]]], List[List[List[float]]]]):
            Grade cartesiana original.
        transformada (Tuple[List[List[List[float]]], List[List[List[float]]]]):
            Grade após aplicação da transformação.
        det (float): Determinante da matriz de transformação.
        inversa (Optional[Tuple[List[List[List[float]]], List[List[List[float]]]]]):
            Grade após transformação inversa, se aplicável.

    Returns:
        None: Exibe o plot usando plt.show().

    Note:
        O plot mostra dois subplots lado a lado com a grade original (azul)
        e transformada (vermelha). Se a inversa for fornecida, é sobreposta
        em verde tracejado no segundo subplot.
    """
    # Configuração da figura
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle("Transformação de Grade Cartesiana", fontsize=16, fontweight="bold")

    def desenhar_grade(
        ax: plt.Axes,
        grade: Tuple[List[List[List[float]]], List[List[List[float]]]],
        cor: str,
        titulo: str
    ) -> None:
        """
        Função auxiliar para desenhar uma grade em um eixo específico.

        Args:
            ax (plt.Axes): Eixo do matplotlib onde desenhar.
            grade (Tuple[List[List[List[float]]], List[List[List[float]]]]): Grade a desenhar.
            cor (str): Cor das linhas da grade.
            titulo (str): Título do subplot.
        """
        linhas_verticais, linhas_horizontais = grade

        # Desenha todas as linhas (verticais e horizontais)
        for linha in linhas_verticais + linhas_horizontais:
            xs = [p[0] for p in linha]
            ys = [p[1] for p in linha]
            ax.plot(xs, ys, color=cor, linewidth=1.2, alpha=0.8)

        # Eixos cartesianos
        ax.axhline(0, color="black", linewidth=1.0, alpha=0.7)
        ax.axvline(0, color="black", linewidth=1.0, alpha=0.7)

        # Configurações do plot
        ax.set_aspect("equal", adjustable="box")
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.set_title(titulo, fontsize=14, fontweight="bold")
        ax.grid(True, linestyle="--", alpha=0.4)
        ax.set_xlabel("X", fontsize=12)
        ax.set_ylabel("Y", fontsize=12)

    # Desenha as grades
    desenhar_grade(axes[0], original, "#1f77b4", "Grade Original")      # Azul
    desenhar_grade(axes[1], transformada, "#d62728", "Grade Transformada")  # Vermelho

    # Adiciona a grade inversa se disponível
    if inversa is not None:
        linhas_verticais, linhas_horizontais = inversa
        for linha in linhas_verticais + linhas_horizontais:
            xs = [p[0] for p in linha]
            ys = [p[1] for p in linha]
            axes[1].plot(xs, ys, color="#2ca02c", linestyle="--", linewidth=1.0, alpha=0.7)  # Verde

        # Legenda para a grade inversa
        axes[1].text(
            0.02, 0.98,
            "🔴 Grade transformada\n🟢 Grade inversa (tracejado)",
            transform=axes[1].transAxes,
            fontsize=10,
            va="top",
            bbox={"facecolor": "white", "alpha": 0.9, "edgecolor": "#cccccc", "boxstyle": "round,pad=0.5"},
        )

    # Informações do determinante
    det_text = f"Determinante = {det:.3f}\n{interpretar_determinante(det)}"
    axes[1].text(
        0.02, 0.04,
        det_text,
        transform=axes[1].transAxes,
        fontsize=11,
        va="bottom",
        bbox={"facecolor": "white", "alpha": 0.9, "edgecolor": "#cccccc", "boxstyle": "round,pad=0.5"},
    )

    # Layout e exibição
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()
