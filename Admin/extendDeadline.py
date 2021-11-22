from flask import Flask, render_template, request, jsonify
import requests
from Downloads.Models import *
from Downloads.helper import *


app = Flask(__name__)
@app.route('/extendDeadline/', methods=['GET','POST'])
def extendDeadline():
    if request.method == 'POST':
        details = request.form
        name = details['contest_name']  # contest name
        deadline = details['deadline']  # contest deadline

        extendDead(name,deadline)
        return "success"
            
    return render_template("addContest.html")

if __name__=='__main__':
    app.run(host='127.0.0.1',port = '5050')
