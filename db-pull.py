import os, sys

py = sys.executable

print("""MySQL GIT Pull
""")

script_dir = os.path.abspath(os.path.dirname(__file__))
I = '/' if( os.name == 'posix' )else '\\'
def dbd(arg):
   global script_dir
   os.system(f'{py} {script_dir}{I}env{I}dbd.py {arg}')
   
os.system('git pull')
dbd('import')