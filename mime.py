from pathlib import Path

file_list = ['example.TXT', 'referecnce.txt', 'strangename.tiff', 'resolv.CSS', 'matrix.TiFF', 'lanDsCape.Png', 'extract.cSs']
table =  {'png': 'image/png', 'TIFF': 'image/tiff', 'css': 'text/css', 'TXT': 'text/plain'}

for f in file_list:
    if f.startswith("."):
        f = f.replace(".", "x.")
        
    f = Path(f.lower())
    
    ext = (f.suffix).replace(".", "").lower()
    print(table.get(ext, "UNKNOWN"))

for i in range(q):
    fname = input()  # One file name per line.
    file_list.append(fname)

file_list = [input() for i in range(q)]