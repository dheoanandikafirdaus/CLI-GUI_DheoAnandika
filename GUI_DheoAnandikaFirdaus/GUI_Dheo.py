import tkinter as tk                  # impor tkinter untuk GUI
from tkinter import messagebox         # impor messagebox untuk pesan error
import matplotlib.pyplot as plt        # impor matplotlib untuk plotting
from mpl_toolkits.mplot3d import Axes3D # aktifkan fitur 3D matplotlib
import numpy as np                     # impor numpy untuk operasi matematika

# fungsi untuk menampilkan plot 3D
def plot_sinus_3d():
    try:
        freq = float(entry_freq.get())  # ambil nilai frekuensi dari input
        amp = float(entry_amp.get())    # ambil nilai amplitudo dari input

        x = np.linspace(-10, 10, 200)   # buat data x dari -10 sampai 10
        y = np.linspace(-10, 10, 200)   # buat data y dari -10 sampai 10
        X, Y = np.meshgrid(x, y)        # buat grid koordinat X dan Y
        R = np.sqrt(X**2 + Y**2)        # hitung jarak dari pusat (radius)
        Z = amp * np.sin(freq * R)      # rumus fungsi sinus

        fig = plt.figure()              # buat figure baru
        ax = fig.add_subplot(111, projection='3d')  # aktifkan mode 3D
        ax.plot_surface(X, Y, Z, cmap='plasma')     # gambar permukaan 3D
        ax.set_title("Plot 3D Fungsi Sin")   # judul grafik
        ax.set_xlabel("X")              # label sumbu X
        ax.set_ylabel("Y")              # label sumbu Y
        ax.set_zlabel("Z")              # label sumbu Z
        plt.show()                      # tampilkan grafik

    except ValueError:
        messagebox.showerror("Error", "Masukkan angka valid!")  # pesan jika input salah

# buat jendela utama
root = tk.Tk()
root.title("Plot 3D Fungsi Sin")

tk.Label(root, text="Masukkan parameter fungsi z = A·sin(f·√(x² + y²))").pack(pady=10)

frame = tk.Frame(root)        # buat frame input
frame.pack()

tk.Label(frame, text="Frekuensi (f) = ").grid(row=0, column=0)   # label frekuensi
entry_freq = tk.Entry(frame)                                  # input frekuensi
entry_freq.grid(row=0, column=1)

tk.Label(frame, text="Amplitudo (A) = ").grid(row=1, column=0)   # label amplitudo
entry_amp = tk.Entry(frame)                                   # input amplitudo
entry_amp.grid(row=1, column=1)

tk.Button(root, text="Plot 3D", command=plot_sinus_3d).pack(pady=10)  # tombol untuk plot

root.mainloop()  # jalankan GUI
