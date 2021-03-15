import os
import os.path
import shutil
from pathlib import Path

Path('src.txt').touch()
os.mkdir('srcdir')
Path('srcdir/aaa.txt').touch()
Path('srcdir/bbb.pyc').touch()

shutil.copy('src.txt', 'dst1.txt')
shutil.copy2('src.txt', 'dst2.txt')
shutil.copytree('srcdir', 'dstdir')
shutil.move('dstdir', 'dstdir2')


def ignore_pyc_files(dirname, filenames):
    return [name for name in filenames if name.endswith('pyc')]


shutil.copytree('srcdir', 'dstdir3', ignore=ignore_pyc_files)


shutil.copytree('srcdir', 'dstdir4', ignore=shutil.ignore_patterns('*.pyc', 'a*'))


# 删除测试文件
os.remove('src.txt')
os.remove('dst1.txt')
os.remove('dst2.txt')
shutil.rmtree('srcdir')
shutil.rmtree('dstdir2')
shutil.rmtree('dstdir3')
shutil.rmtree('dstdir4')


filename = '/Users/guido/programs/spam.py'
os.path.basename(filename)
os.path.dirname(filename)
os.path.split(filename)
os.path.join('/new/dir', os.path.basename(filename))
os.path.expanduser('~/guido/programs/spam.py')
