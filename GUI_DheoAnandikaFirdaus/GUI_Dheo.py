import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

def plot_kuadrat():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        x = np.linspace(-10, 10, 200)
        y = a*x**2 + b*x + c

        plt.plot(x, y, label=f"{a}x² + {b}x + {c}")
        plt.title("Plot Fungsi Kuadrat")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.grid(True)
        plt.show()

    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

# GUI window
root = tk.Tk()
root.title("Plot Fungsi Kuadrat")

tk.Label(root, text="Masukkan koefisien fungsi y = ax² + bx + c").pack(pady=10)

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="a:").grid(row=0, column=0)
entry_a = tk.Entry(frame)
entry_a.grid(row=0, column=1)

tk.Label(frame, text="b:").grid(row=1, column=0)
entry_b = tk.Entry(frame)
entry_b.grid(row=1, column=1)

tk.Label(frame, text="c:").grid(row=2, column=0)
entry_c = tk.Entry(frame)
entry_c.grid(row=2, column=1)

tk.Button(root, text="Plot", command=plot_kuadrat).pack(pady=10)

root.mainloop()
