from flask import Flask, render_template, request, jsonify
import requests
from Downloads.Models import *
from Downloads.helper import *


app = Flask(__name__)
@app.route('/predictWinner/', methods=['GET'])
def predWinner():
    if request.method == 'GET':
        winner = predictWinner()
        return winner
    return render_template("new.html")

if __name__=='__main__':
    app.run(host='127.0.0.1',port = '5055')