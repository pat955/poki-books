import sys
from setuptools import setup

setup(
   name='PokiBooks',
   version='0.1.8',
   description='Simple eReader',
   author='pat955',
   author_email='patricija.pivoraite@gmail.com',
   packages=['PokiBooks'],  #same as name
   scripts=[
            'scripts/make_exe.sh',
            'scripts/run.sh',
           ]
)
try:
   from semantic_release import setup_hook
   setup_hook(sys.argv)
except ImportError:
   print('import error')