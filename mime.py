from pathlib import Path

# file_list = ['example.TXT', 'referecnce.txt', 'strangename.tiff', 'resolv.CSS', 'matrix.TiFF', 'lanDsCape.Png', 'extract.cSs']
# table =  {'png': 'image/png', 'TIFF': 'image/tiff', 'css': 'text/css', 'TXT': 'text/plain'}

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
table = {}

for i in range(n):
    ext, mt = input().split()
    table[ext.lower()] = mt

file_list = [input() for _ in range(q)]

for f in file_list:
    if f.startswith("."):
        f = f.replace(".", "x.")
    f = Path(f.lower())
    ext = (f.suffix).replace(".", "").lower()
    print(table.get(ext, "UNKNOWN"))

