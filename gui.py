"""
================================================================================
APLICAÇÃO: TRANSFORMAÇÃO DE GRADE CARTESIANA - INTERFACE GRÁFICA (GUI)
================================================================================

Interface Tkinter interativa para visualizar transformações lineares em
tempo real. Permite ao usuário ajustar os coeficientes da matriz 2x2 e
ver imediatamente o efeito geométrico na grade cartesiana.

Características principais:
  • Entrada interativa dos coeficientes (a, b, c, d)
  • Validação de entrada em tempo real
  • Cálculo dinâmico de transformações
  • Visualização integrada com Matplotlib
  • Exibição da matriz inversa (quando existe)
  • Interpretação geométrica do determinante

================================================================================
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


# ============================================================================
# CLASSE PRINCIPAL DA APLICAÇÃO GUI
# ============================================================================

class TransformacaoApp:
    """
    Aplicação GUI para visualizar transformações de grade cartesiana.

    Fornece uma interface interativa com Tkinter para entrada de parâmetros
    e visualização em tempo real dos resultados usando Matplotlib integrado.

    Atributos:
        root (tk.Tk): Janela principal da aplicação
        entries (Dict[str, ttk.Entry]): Campos de entrada dos coeficientes
        canvas (Optional[FigureCanvasTkAgg]): Canvas do Matplotlib
        status_label (ttk.Label): Label para mensagens de status
        btn_compute (tk.Button): Botão para calcular e plotar
    """

    def __init__(self, root: tk.Tk) -> None:
        """
        Inicializa a aplicação GUI.

        Configura a janela principal, estilos visuais e cria todos os widgets.

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
        """
        Configura os estilos visuais da aplicação.

        Define temas para:
          • Labels
          • Botões (normal e ênfase)
          • Campos de texto
          • Frames de cartão
        """
        style = ttk.Style()
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        # Estilo padrão para labels
        style.configure(
            "TLabel",
            font=("Segoe UI", 12),
            background="#eaf2ff",
            foreground="#333333"
        )

        # Estilo para botões normais
        style.configure(
            "TButton",
            font=("Segoe UI", 12, "bold"),
            padding=12,
            relief="flat"
        )

        # Estilo para botões de ênfase
        style.configure(
            "Accent.TButton",
            background="#1e81b0",
            foreground="#ffffff",
            borderwidth=0,
            focusthickness=3,
            focuscolor="#ffffff"
        )
        style.map(
            "Accent.TButton",
            background=[
                ("active", "#17648a"),
                ("disabled", "#a0c4d6"),
                ("!disabled", "#1e81b0")
            ],
            foreground=[
                ("active", "#ffffff"),
                ("disabled", "#e6eef8"),
                ("!disabled", "#ffffff")
            ]
        )

        # Estilo para campos de entrada
        style.configure(
            "TEntry",
            font=("Segoe UI", 12),
            padding=6
        )

        # Estilo para frames de cartão
        style.configure(
            "Card.TFrame",
            background="#ffffff",
            borderwidth=1,
            relief="raised"
        )

    def _criar_widgets(self) -> None:
        """
        Cria e organiza todos os widgets da interface.

        Estrutura:
          1. Frame de entrada com campos para a, b, c, d
          2. Botão "Calcular e Plotar"
          3. Label de status
          4. Frame para o gráfico do Matplotlib
        """
        # ====================================================================
        # FRAME DE ENTRADA
        # ====================================================================
        input_frame = ttk.Frame(self.root, padding=20, style="Card.TFrame")
        input_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        # Título da seção de entrada
        title_label = ttk.Label(
            input_frame,
            text="🔢 Coeficientes da Matriz 2×2",
            font=("Segoe UI", 14, "bold")
        )
        title_label.grid(row=0, column=0, columnspan=4, pady=(0, 15))

        # Criação dos campos de entrada para os coeficientes
        self.entries: Dict[str, ttk.Entry] = {}
        labels = ['a', 'b', 'c', 'd']
        default_values = {'a': '1', 'b': '0', 'c': '0', 'd': '1'}

        for i, label in enumerate(labels):
            # Label do coeficiente
            ttk.Label(input_frame, text=f"{label}:").grid(
                row=1, column=i, padx=8, pady=5, sticky="e"
            )

            # Campo de entrada
            entry = ttk.Entry(input_frame, width=12, justify="center")
            entry.grid(row=2, column=i, padx=8, pady=5)
            entry.insert(0, default_values.get(label, '0'))

            # Validação em tempo real ao digitar
            entry.bind('<KeyRelease>', self._validar_entrada)

            self.entries[label] = entry

        # ====================================================================
        # BOTÃO DE CÁLCULO
        # ====================================================================
        self.btn_compute = tk.Button(
            input_frame,
            text="📊 Calcular e Plotar",
            command=self.compute,
            font=("Segoe UI", 12, "bold"),
            bg="#1e81b0",
            fg="#ffffff",
            activebackground="#17648a",
            activeforeground="#ffffff",
            bd=0,
            relief="flat",
            padx=12,
            pady=8,
            cursor="hand2"
        )
        self.btn_compute.grid(row=3, column=0, columnspan=4, pady=20)

        # ====================================================================
        # LABEL DE STATUS
        # ====================================================================
        self.status_label = ttk.Label(
            input_frame,
            text="✅ Pronto para calcular",
            foreground="#28a745"
        )
        self.status_label.grid(row=4, column=0, columnspan=4, pady=(0, 10))

        # ====================================================================
        # FRAME PARA O PLOT
        # ====================================================================
        plot_frame = ttk.Frame(self.root, padding=10)
        plot_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # Label informativo
        info_label = ttk.Label(
            plot_frame,
            text="💡 Dica: Experimente diferentes valores para ver como a grade se transforma!",
            font=("Segoe UI", 10),
            foreground="#666666"
        )
        info_label.pack(side=tk.TOP, pady=(0, 10))

    def _validar_entrada(self, event: tk.Event) -> None:
        """
        Valida a entrada dos campos em tempo real.

        Verifica se todos os campos contêm números válidos e atualiza:
          • Cor do status (verde para válido, vermelho para inválido)
          • Estado do botão (habilitado/desabilitado)

        Args:
            event (tk.Event): Evento de liberação de tecla.
        """
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

        Etapas:
          1. Coleta os coeficientes dos campos de entrada
          2. Calcula o determinante
          3. Gera a grade original
          4. Aplica a transformação linear
          5. Calcula a transformação inversa (se possível)
          6. Atualiza o gráfico

        Trata erros de entrada e exibe mensagens ao usuário.
        """
        try:
            # ETAPA 1: Coleta dos coeficientes
            a = float(self.entries['a'].get())
            b = float(self.entries['b'].get())
            c = float(self.entries['c'].get())
            d = float(self.entries['d'].get())

            # ETAPA 2: Construção da matriz
            matriz = [[a, b], [c, d]]

            # ETAPA 3: Cálculo do determinante
            det = determinante_2x2(matriz)

            # ETAPA 4: Geração da grade original
            grade_original = gerar_grade(-5, 5, -5, 5, 1)

            # ETAPA 5: Aplicação da transformação
            grade_transformada = transformar_grade(matriz, grade_original)

            # ETAPA 6: Verificação da invertibilidade
            grade_inversa = None
            if abs(det) > 1e-12:
                inversa = matriz_inversa_2x2(matriz)
                grade_inversa = transformar_grade(inversa, grade_transformada)

            # ETAPA 7: Atualização da visualização
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

        Desenha dois subplots lado a lado:
          • À esquerda: Grade original (azul)
          • À direita: Grade transformada (vermelha)
        
        Se a inversa estiver disponível, sobrepõe em verde tracejado.

        Args:
            original (tuple): Grade cartesiana original (linhas vert. e horiz.)
            transformada (tuple): Grade após transformação.
            det (float): Determinante da matriz de transformação.
            inversa (Optional[tuple]): Grade inversa, se aplicável.
        """
        # Remove canvas anterior se existir
        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        # Cria nova figura Matplotlib
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
            """
            Função auxiliar para desenhar uma grade em um eixo específico.

            Desenha todas as linhas (verticais e horizontais) com a cor
            especificada e configura os eixos.

            Args:
                ax (Axes): Eixo do Matplotlib onde desenhar.
                grade (tuple): Tupla (linhas_vert, linhas_horiz).
                cor (str): Cor RGB ou nome da cor para as linhas.
                titulo (str): Título do subplot.
            """
            linhas_verticais, linhas_horizontais = grade

            # Desenha todas as linhas
            for linha in linhas_verticais + linhas_horizontais:
                xs = [p[0] for p in linha]
                ys = [p[1] for p in linha]
                ax.plot(xs, ys, color=cor, linewidth=1.5, alpha=0.8)

            # Desenha os eixos cartesianos
            ax.axhline(0, color="#333333", linewidth=1.2, alpha=0.7)
            ax.axvline(0, color="#333333", linewidth=1.2, alpha=0.7)

            # Configurações do subplot
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

        # Desenha as grades original e transformada
        desenhar_grade(axes[0], original, "#1976d2", "Grade Original")
        desenhar_grade(axes[1], transformada, "#ef476f", "Grade Transformada")

        # Adiciona a grade inversa se disponível
        if inversa is not None:
            linhas_verticais, linhas_horizontais = inversa
            for linha in linhas_verticais + linhas_horizontais:
                xs = [p[0] for p in linha]
                ys = [p[1] for p in linha]
                axes[1].plot(xs, ys, color="#2ca02c", linestyle="--", linewidth=1.2, alpha=0.8)

            # Legenda para a grade inversa
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

        # Informações sobre o determinante
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

        # Ajusta o layout e integra com Tkinter
        plt.tight_layout(rect=[0, 0, 1, 0.94])

        # Cria e exibe o canvas do Matplotlib no Tkinter
        self.canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.canvas.draw()


# ============================================================================
# FUNÇÃO PRINCIPAL
# ============================================================================

def main() -> None:
    """Função principal para executar a aplicação GUI."""
    root = tk.Tk()
    app = TransformacaoApp(root)
    root.mainloop()


# ============================================================================
# PONTO DE ENTRADA
# ============================================================================

if __name__ == "__main__":
    main()