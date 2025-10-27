"""
Program CLI rumus fisika sederhana

Usage:
  fisika_docopt.py gelombang <y> <f>
  fisika_docopt.py pascal <F1> <A1> <A2>
  fisika_docopt.py glbb <v0> <t> <a>
  fisika_docopt.py (-h | --help)

Options:
  -h --help   Tampilkan bantuan.
"""

from docopt import docopt  # import library docopt

#Definisi fungsi rumus
def kecepatan_gelombang(y, f):
    return y * f

def hukum_pascal(F1, A1, A2):
    return (F1 * A2) / A1

def glbb(v0, t, a):
    return v0 * t + 0.5 * a * t**2

#Program utama
if __name__ == "__main__":
    args = docopt(__doc__)  # ambil argumen dari command line

    if args["gelombang"]:
        y = float(args["<y>"])
        f = float(args["<f>"])
        print(f"Kecepatan gelombang = {kecepatan_gelombang(y, f):.2f} m/s")

    elif args["pascal"]:
        F1 = float(args["<F1>"])
        A1 = float(args["<A1>"])
        A2 = float(args["<A2>"])
        print(f"Gaya F2 = {hukum_pascal(F1, A1, A2):.2f} N")

    elif args["glbb"]:
        v0 = float(args["<v0>"])
        t = float(args["<t>"])
        a = float(args["<a>"])
        print(f"Jarak s = {glbb(v0, t, a):.2f} m")
