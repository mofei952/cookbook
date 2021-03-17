import os
import shutil
from pathlib import Path

os.mkdir('Python-3.3.0')
Path('Python-3.3.0\\aa.txt').touch()
shutil.make_archive('py33', 'zip', 'Python-3.3.0')
shutil.unpack_archive('py33.zip')

shutil.rmtree('Python-3.3.0')
os.remove('aa.txt')
os.remove('py33.zip')
