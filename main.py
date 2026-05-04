import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

def plot_transformation(matrix, title="Transformação Linear"):
    # 1. Criar a grade de pontos (x, y)
    x = np.linspace(-5, 5, 11)
    y = np.linspace(-5, 5, 11)
    X, Y = np.meshgrid(x, y)
    
    # Achatar as matrizes para operar nos pontos individualmente
    points = np.vstack([X.flatten(), Y.flatten()])
    
    # 2. Aplicar a transformação matricial: P' = M * P
    transformed_points = matrix @ points
    
    # Remodelar de volta para o formato de grade
    X_trans = transformed_points[0, :].reshape(X.shape)
    Y_trans = transformed_points[1, :].reshape(Y.shape)
    
    # 3. Visualização
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    
    # Grade Original
    for i in range(len(x)):
        ax[0].plot(X[i, :], Y[i, :], color='blue', alpha=0.3) # Linhas horizontais
        ax[0].plot(X[:, i], Y[:, i], color='blue', alpha=0.3) # Linhas verticais
    ax[0].set_title("Grade Original (Identidade)")
    ax[0].grid(True, linestyle='--')
    
    # Grade Transformada
    for i in range(len(x)):
        ax[1].plot(X_trans[i, :], Y_trans[i, :], color='red')
        ax[1].plot(X_trans[:, i], Y_trans[:, i], color='red')
    ax[1].set_title(f"Grade Transformada\n{matrix}")
    ax[1].grid(True, linestyle='--')
    
    for a in ax:
        a.set_xlim([-10, 10])
        a.set_ylim([-10, 10])
        a.axhline(0, color='black', lw=1)
        a.axvline(0, color='black', lw=1)
        a.set_aspect('equal')

    plt.tight_layout()
    plt.show()

def create_gui():
    root = tk.Tk()
    root.title("Input Matrix for Transformation")
    
    # Labels
    tk.Label(root, text="Enter 2x2 Matrix Elements:").grid(row=0, column=0, columnspan=4)
    
    entries = []
    for i in range(2):
        row = []
        for j in range(2):
            e = tk.Entry(root, width=10)
            e.grid(row=i+1, column=j*2, columnspan=2, padx=5, pady=5)
            row.append(e)
        entries.append(row)
    
    def plot():
        try:
            a = float(entries[0][0].get())
            b = float(entries[0][1].get())
            c = float(entries[1][0].get())
            d = float(entries[1][1].get())
            matrix = np.array([[a, b], [c, d]])
            plot_transformation(matrix)
        except ValueError:
            error_label.config(text="Please enter valid numbers")
    
    tk.Button(root, text="Plot Transformation", command=plot).grid(row=3, column=0, columnspan=4)
    
    error_label = tk.Label(root, text="", fg="red")
    error_label.grid(row=4, column=0, columnspan=4)
    
    root.mainloop()

# --- Exemplos de Matrizes ---

# 1. Cisalhamento (Shear)
M_shear = np.array([[2, 2], 
                    [0, 2]])

# 2. Rotação (Ex: 45 graus)
theta = np.radians(45)
M_rotation = np.array([[np.cos(theta), -np.sin(theta)],
                       [np.sin(theta),  np.cos(theta)]])

# Execução
if __name__ == "__main__":
    create_gui()