import click  # mengimpor library click untuk membuat Command Line Interface (CLI) interaktif

# Definisi fungsi-fungsi rumus fisika 

def kecepatan_gelombang(y, f):
    # Rumus kecepatan gelombang: v = λ * f
    return y * f

def hukum_pascal(F1, A1, A2):
    # Rumus Hukum Pascal: F2 = (F1 * A2) / A1
    return (F1 * A2) / A1

def glbb(v0, t, a):
    # Rumus GLBB (jarak): s = v0*t + 0.5*a*t^2
    return v0 * t + 0.5 * a * t**2


#Pembuatan struktur CLI utama

@click.group()
def cli():
    """
    Program CLI Fisika Sederhana by Dheo
    Memuat 3 rumus:
    1. Kecepatan Gelombang (v = λ*f)
    2. Hukum Pascal (F2 = (F1*A2)/A1)
    3. GLBB (s = v0*t + 0.5*a*t^2)
    """
    pass  # tidak melakukan apa-apa, hanya sebagai wadah command


#Sub-command 1: Kecepatan Gelombang 
@cli.command()
@click.argument("y", type=float)  # panjang gelombang (λ)
@click.argument("f", type=float)  # frekuensi (f)
def gelombang(y, f):
    """Hitung kecepatan gelombang (v = y*f)"""
    hasil = kecepatan_gelombang(y, f)  # memanggil fungsi rumus
    click.echo(f"Kecepatan gelombang = {hasil:.2f} m/s")  # menampilkan hasil


#Sub-command 2: Hukum Pascal 
@cli.command()
@click.argument("F1", type=float)  # gaya pertama
@click.argument("A1", type=float)  # luas penampang pertama
@click.argument("A2", type=float)  # luas penampang kedua
def pascal(F1, A1, A2):
    """Hitung Hukum Pascal (F2=(F1*A2)/A1)"""
    hasil = hukum_pascal(F1, A1, A2)  # memanggil fungsi rumus
    click.echo(f"Gaya F2 = {hasil:.2f} N")  # menampilkan hasil


#Sub-command 3: GLBB 
@cli.command(name="glbb")
@click.argument("v0", type=float)  # kecepatan awal
@click.argument("t", type=float)   # waktu
@click.argument("a", type=float)   # percepatan
def glbb_command(v0, t, a):
    """Hitung jarak GLBB (s = v0*t + 0.5*a*t^2)"""
    hasil = glbb(v0, t, a)  # memanggil fungsi rumus
    click.echo(f"Jarak s = {hasil:.2f} m")  # menampilkan hasil


#Pemanggilan utama
if __name__ == "__main__":
    cli()  # menjalankan CLI utama
