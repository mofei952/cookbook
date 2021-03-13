import os
import shutil
from pathlib import Path

Path('src.txt').touch()
os.mkdir('srcdir')
Path('srcdir/aaa.txt').touch()

shutil.copy('src.txt', 'dst1.txt')
shutil.copy2('src.txt', 'dst2.txt')
shutil.copytree('srcdir', 'dstdir')
shutil.move('dstdir', 'dstdir2')

os.remove('src.txt')
os.remove('dst1.txt')
os.remove('dst2.txt')
shutil.rmtree('srcdir')
shutil.rmtree('dstdir2')
