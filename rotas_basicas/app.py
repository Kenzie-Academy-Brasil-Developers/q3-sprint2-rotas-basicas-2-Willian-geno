from flask import Flask, jsonify
from datetime import datetime
from http import HTTPStatus

app = Flask(__name__)

@app.get('/')
def home():
    return {"data": "Hello Flask!"}, HTTPStatus.OK


@app.get("/current_datetime")
def current_datetime():
    msg=""
    time = datetime.now()
    hours = time.strftime("%H")
    hours=int(hours)
    if hours < 12:  
        msg="Bom dia!"
    if hours >= 12 and hours < 18:
        msg ="Boa tarde!"
    if hours >= 18:
        msg = "Boa noite!"

    return ({"current_datetime":f'{time.strftime("%d/%m/%y %I:%M:%S %p")}',
    "message":f'{msg}'}), HTTPStatus.OK

