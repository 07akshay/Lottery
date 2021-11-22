from flask import Flask, render_template, request, jsonify
import requests
from Downloads.Models import *
from Downloads.helper import *


app = Flask(__name__)
@app.route('/removeContest/', methods=['GET','POST'])
def removeContest():
    if request.method == 'POST':
        details = request.form
        name = details['contest_name']  # contest name
        deadline = details['deadline']  # contest deadline
        remContest(name,deadline)
        return "success"
            
    return render_template("addContest.html")

if __name__=='__main__':
    app.run(host='127.0.0.1',port = '5050')