from flask import Flask, render_template, request, jsonify
import requests
from Downloads.Models import *
from Downloads.helper import *


app = Flask(__name__)
@app.route('/allottToken/', methods=['GET','POST'])
def fetch():
    if request.method == 'POST':
        details = request.form
        userID = details['key']  # use as userid for now
        contest = details['values']    # contest name
        
        token = Token()
        token.createToken(contest,userID)
        er = Error()
        if (not checkUser(userID, contest)):
            er.userExists()        
        if (not tokenAvailable(token)):
            er.tokenNotAvailable()
        if er.errorCode is not None:
            return er.error
        
        insertToDB(token)
        return token.Number
    return render_template("new.html")

if __name__=='__main__':
    app.run(host='127.0.0.1',port = '5055')