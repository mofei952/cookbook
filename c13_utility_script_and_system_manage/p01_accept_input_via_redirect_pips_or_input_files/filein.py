import fileinput

# for line in fileinput.input():
#     print(line)


f = fileinput.input()
for line in f:
    print(f.filename(), f.lineno(), line)


# dir | .\filein.py
# .\filein.py C:\Windows\system.ini
