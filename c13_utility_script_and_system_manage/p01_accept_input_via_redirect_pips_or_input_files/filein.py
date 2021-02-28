#!/usr/bin/env python3
import fileinput

with fileinput.input() as f_input:
    for line in f_input:
        print(line, end='')


# ls | ./filein.py
# ./filein.py /etc/passwd
# ./filein.py < /etc/passwd