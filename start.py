import os, sys

py = sys.executable

print("""Let's start!
Now you gonna to configure this tool to connect to DB.
""")

I = '/' if( os.name == 'posix' )else '\\'
script_dir = os.path.dirname(__file__)
def dbd(arg):
   os.system(f'{py} .{script_dir}{I}env{I}dbd.py {arg}')
   
dbd('relogin')

print(f"""
Great! Now you can you these commands:

{py} db-pull.py
   git pull + mysql import
{py} db-push.py
   mysql export (to sqldump folder) + git commit (sqldump folder) + git push

Use it to sync your db via github ;)""")