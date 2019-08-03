#!python
#!C:\Python37\python.exe

import subprocess

# if the script don't need output.
subprocess.call("php C:\Python37/anitoki.py/inc/maki.txt")

# if you want output
proc = subprocess.Popen("php C:\Python37/anitoki.py/inc/maki.txt", shell=True, stdout=subprocess.PIPE)
script_response = proc.stdout.read()