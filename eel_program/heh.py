import eel
import subprocess, os

# Initialize Eel with the web folder
eel.init('web')

# Expose a Python function to the JavaScript frontend
@eel.expose
def run_script(val):
    #if val:
    print(val)
    result = subprocess.Popen(val, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
    output = result.stdout
    error = result.stderr
    res = output.read()
    if res == '':
        res = error.read()
    print(res)
    folder = os.getcwd().split('\\')
    folder = folder[len(folder)-1]
    return [res, folder]

# Start the Eel application
eel.start('shell.html', size=(700, 500))
