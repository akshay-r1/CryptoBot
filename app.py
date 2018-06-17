from flask import Flask
from flask import render_template,jsonify,request
import requests
import pandas as pd
# from models import *
from engine import *
import random

def exportdatabase():
    try:
        data = pd.read_csv('./Data Directory/crypto-markets.csv',parse_dates=['date'], index_col='date')
        return data
    except Exception as e:
        print (e)
        print "Reading Failed"
        return

app = Flask(__name__)
app.secret_key = '12345'



@app.route('/')
def hello_world():
    return render_template('home.html')

get_random_response = lambda intent:random.choice(intent_response_dict[intent])


@app.route('/chat',methods=["POST"])
def chat():
    try:
        data = exportdatabase()
        user_message = request.form["text"]
        response = requests.get("http://localhost:5000/parse",params={"q":user_message})
        response = response.json()
        print (response)
        entities = response.get("entities")
        intent = response.get("intent")
        print("Intent {}, Entities {}".format(intent,entities))
        if intent['name'] == "intro" or intent['name']== "greet" or intent['name']=="goodbye" or intent['name']=="affirm":
            response_text = get_random_response(intent['name']) # intro greet intents
        elif intent['name']== "AttributesKnowledgeBase":
            response_text = AttributesKnowledgeBase(data)
        elif intent['name']== "CryptoList":
            response_text = CryptoList(data)
        elif intent['name']=="GetHighestValueByName":
            response_text = GetHighestValueByName(data,entities[0]['value'])
            response_text = '$' +str(response_text)
        #elif intent['name']=="PlotCurrencyGraph"
        print response_text
        return jsonify({"status":"success","response":response_text})
    except Exception as e:
        print(e)
        return jsonify({"status":"success","response":"Sorry I am not trained to do that yet..."})


app.config["DEBUG"] = True
if __name__ == "__main__":
    app.run(port=8080)
