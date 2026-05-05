"""
Interface Gráfica para Transformação de Grade Cartesiana

Este módulo fornece uma interface gráfica interativa usando Tkinter
para entrada de coeficientes da matriz de transformação e visualização
em tempo real das grades original e transformada.

Características:
- Entrada intuitiva dos coeficientes a, b, c, d
- Validação de entrada em tempo real
- Visualização integrada com Matplotlib
- Design moderno e responsivo

Autor: GitHub Copilot
Data: 2026
Licença: MIT
"""

import tkinter as tk
from tkinter import ttk, messagebox
from typing import Dict, Optional
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.axes import Axes

from algebra import determinante_2x2, matriz_inversa_2x2
from grade import gerar_grade, transformar_grade
from visualizacao import interpretar_determinante


class TransformacaoApp:
    """
    Classe principal da aplicação GUI para transformação de grade cartesiana.

    Fornece uma interface completa para entrada de parâmetros e visualização
    dos resultados da transformação linear.
    """

    def __init__(self, root: tk.Tk) -> None:
        """
        Inicializa a aplicação GUI.

        Args:
            root (tk.Tk): Janela principal do Tkinter.
        """
        self.root = root
        self.root.title("📐 Transformação de Grade Cartesiana")
        self.root.geometry("1200x800")
        self.root.configure(bg="#84b1fa")
        self.root.resizable(True, True)

        # Configuração de estilos
        self._configurar_estilos()

        # Criação dos widgets
        self._criar_widgets()

        # Referência para o canvas do matplotlib
        self.canvas: Optional[FigureCanvasTkAgg] = None

    def _configurar_estilos(self) -> None:
        """Configura os estilos visuais da aplicação."""
        style = ttk.Style()

        # Estilo geral
        style.configure(
            "TLabel",
            font=("Segoe UI", 12),
            background="#eaf2ff",
            foreground="#333333"
        )
        style.configure(
            "TButton",
            font=("Segoe UI", 12, "bold"),
            padding=12,
            relief="flat"
        )
        style.configure(
            "Accent.TButton",
            background="#1e81b0",
            foreground="white",
            borderwidth=0,
            focusthickness=3,
            focuscolor="#ffffff"
        )
        style.map(
            "Accent.TButton",
            background=[("active", "#17648a"), ("disabled", "#a0c4d6")]
        )
        style.configure(
            "TEntry",
            font=("Segoe UI", 12),
            padding=6
        )
        style.configure(
            "Card.TFrame",
            background="#ffffff",
            borderwidth=1,
            relief="raised"
        )

    def _criar_widgets(self) -> None:
        """Cria e organiza todos os widgets da interface."""
        # Frame principal para entrada
        input_frame = ttk.Frame(self.root, padding=20, style="Card.TFrame")
        input_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        # Título da seção de entrada
        title_label = ttk.Label(
            input_frame,
            text="🔢 Coeficientes da Matriz 2×2",
            font=("Segoe UI", 14, "bold")
        )
        title_label.grid(row=0, column=0, columnspan=4, pady=(0, 15))

        # Campos de entrada
        self.entries: Dict[str, ttk.Entry] = {}
        labels = ['a', 'b', 'c', 'd']
        default_values = {'a': '1', 'b': '0', 'c': '0', 'd': '1'}  # Matriz identidade

        for i, label in enumerate(labels):
            # Label do coeficiente
            ttk.Label(input_frame, text=f"{label}:").grid(
                row=1, column=i, padx=8, pady=5, sticky="e"
            )

            # Campo de entrada
            entry = ttk.Entry(input_frame, width=12, justify="center")
            entry.grid(row=2, column=i, padx=8, pady=5)
            entry.insert(0, default_values.get(label, '0'))

            # Validação em tempo real
            entry.bind('<KeyRelease>', self._validar_entrada)

            self.entries[label] = entry

        # Botão de cálculo
        self.btn_compute = ttk.Button(
            input_frame,
            text="📊 Calcular e Plotar",
            command=self.compute,
            style="Accent.TButton"
        )
        self.btn_compute.grid(row=3, column=0, columnspan=4, pady=20)

        # Status label
        self.status_label = ttk.Label(
            input_frame,
            text="✅ Pronto para calcular",
            foreground="#28a745"
        )
        self.status_label.grid(row=4, column=0, columnspan=4, pady=(0, 10))

        # Frame para o plot
        plot_frame = ttk.Frame(self.root, padding=10)
        plot_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # Label informativo
        info_label = ttk.Label(
            plot_frame,
            text="💡 Dica: Experimente diferentes matrizes para ver como a grade se transforma!",
            font=("Segoe UI", 10),
            foreground="#666666"
        )
        info_label.pack(side=tk.TOP, pady=(0, 10))

    def _validar_entrada(self, event: tk.Event) -> None:
        """Valida a entrada em tempo real e atualiza o status."""
        try:
            for entry in self.entries.values():
                float(entry.get())
            self.status_label.config(text="✅ Entrada válida", foreground="#28a745")
            self.btn_compute.config(state="normal")
        except ValueError:
            self.status_label.config(text="❌ Entrada inválida", foreground="#dc3545")
            self.btn_compute.config(state="disabled")

    def compute(self) -> None:
        """
        Executa o cálculo da transformação e atualiza a visualização.

        Coleta os valores dos campos de entrada, calcula o determinante,
        gera as grades e exibe o resultado gráfico.
        """
        try:
            # Coleta dos coeficientes
            a = float(self.entries['a'].get())
            b = float(self.entries['b'].get())
            c = float(self.entries['c'].get())
            d = float(self.entries['d'].get())

            # Construção da matriz
            matriz = [[a, b], [c, d]]

            # Cálculo do determinante
            det = determinante_2x2(matriz)

            # Geração da grade original
            grade_original = gerar_grade(-5, 5, -5, 5, 1)

            # Aplicação da transformação
            grade_transformada = transformar_grade(matriz, grade_original)

            # Verificação da invertibilidade
            grade_inversa = None
            if abs(det) > 1e-12:
                inversa = matriz_inversa_2x2(matriz)
                grade_inversa = transformar_grade(inversa, grade_transformada)

            # Atualização da visualização
            self._plot(grade_original, grade_transformada, det, grade_inversa)
            self.status_label.config(text="✅ Cálculo concluído", foreground="#28a745")

        except ValueError as e:
            messagebox.showerror("Erro de Validação", f"Entrada inválida: {e}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro inesperado: {e}")

    def _plot(
        self,
        original: tuple,
        transformada: tuple,
        det: float,
        inversa: Optional[tuple] = None
    ) -> None:
        """
        Cria e exibe o plot das grades no canvas integrado.

        Args:
            original: Grade cartesiana original.
            transformada: Grade após transformação.
            det: Determinante da matriz.
            inversa: Grade inversa, se aplicável.
        """
        # Remove canvas anterior se existir
        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        # Cria nova figura
        fig, axes = plt.subplots(1, 2, figsize=(10, 5), dpi=100)
        fig.patch.set_facecolor("#f3f7ff")
        fig.suptitle(
            "Transformação de Grade Cartesiana",
            fontsize=16,
            fontweight="bold",
            color="#1a3f66",
            y=0.98
        )

        def desenhar_grade(ax: Axes, grade: tuple, cor: str, titulo: str) -> None:
            """Função auxiliar para desenhar uma grade em um eixo."""
            linhas_verticais, linhas_horizontais = grade
            for linha in linhas_verticais + linhas_horizontais:
                xs = [p[0] for p in linha]
                ys = [p[1] for p in linha]
                ax.plot(xs, ys, color=cor, linewidth=1.5, alpha=0.8)

            # Eixos cartesianos
            ax.axhline(0, color="#333333", linewidth=1.2, alpha=0.7)
            ax.axvline(0, color="#333333", linewidth=1.2, alpha=0.7)

            # Configurações
            ax.set_aspect("equal", adjustable="box")
            ax.set_xlim(-10, 10)
            ax.set_ylim(-10, 10)
            ax.set_title(titulo, fontsize=14, fontweight="bold", color="#1f4e79")
            ax.grid(True, linestyle="--", color="#b3c7e6", alpha=0.7)
            ax.set_facecolor("#f5f8ff")
            ax.spines["top"].set_visible(False)
            ax.spines["right"].set_visible(False)
            ax.spines["bottom"].set_color("#777777")
            ax.spines["left"].set_color("#777777")
            ax.set_xlabel("X", fontsize=11, color="#333333")
            ax.set_ylabel("Y", fontsize=11, color="#333333")

        # Desenha as grades
        desenhar_grade(axes[0], original, "#1976d2", "Grade Original")      # Azul mais vivo
        desenhar_grade(axes[1], transformada, "#ef476f", "Grade Transformada")  # Vermelho vibrante

        # Adiciona grade inversa se disponível
        if inversa is not None:
            linhas_verticais, linhas_horizontais = inversa
            for linha in linhas_verticais + linhas_horizontais:
                xs = [p[0] for p in linha]
                ys = [p[1] for p in linha]
                axes[1].plot(xs, ys, color="#2ca02c", linestyle="--", linewidth=1.2, alpha=0.8)

            # Legenda para grade inversa
            axes[1].text(
                0.02, 0.88,
                "🔴 Transformada\n🟢 Inversa (tracejado)",
                transform=axes[1].transAxes,
                fontsize=10,
                va="top",
                bbox={
                    "facecolor": "white",
                    "alpha": 0.95,
                    "edgecolor": "#cccccc",
                    "boxstyle": "round,pad=0.5"
                },
            )

        # Informações do determinante
        det_text = f"Determinante = {det:.3f}\n{interpretar_determinante(det)}"
        axes[1].text(
            0.98, 0.02,
            det_text,
            transform=axes[1].transAxes,
            fontsize=11,
            ha="right",
            va="bottom",
            bbox={
                "facecolor": "white",
                "alpha": 0.95,
                "edgecolor": "#cccccc",
                "boxstyle": "round,pad=0.5"
            },
        )

        # Layout e integração com Tkinter
        plt.tight_layout(rect=[0, 0, 1, 0.94])

        # Cria canvas no Tkinter
        self.canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.canvas.draw()


def main() -> None:
    """Função principal para executar a aplicação GUI."""
    root = tk.Tk()
    app = TransformacaoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()