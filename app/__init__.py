# -*- coding: UTF-8 -*-
import app.model as model
import numpy as np

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['GET'])
def getResult():
    input = np.array([[1, 66, 80, 118, 40, 57, 15, 6.3, 118, 98.3, 0, 91, 173, 30.4, 131, 85.6, 172, 2.45, 2.8, 0]])
    result = model.predict(input)
    return jsonify({'result': str(result)})

@app.route('/predict', methods=['POST'])
def postInput():
    # 取得前端傳過來的數值
    insertValues = request.get_json()
    x1=insertValues['gender']
    x2=insertValues['anchor_age']
    x3=insertValues['HR']
    x4=insertValues['NBPs']
    x5=insertValues['NBPd']
    x6=insertValues['NBPm']
    x7=insertValues['RR']
    x8=insertValues['Hemoglobin']
    x9=insertValues['Glucose (serum)']
    x10=insertValues['Temperature F']
    x11=insertValues['Unintentional weight loss >10 lbs.']
    x12=insertValues['Admission Weight (Kg)']
    x13=insertValues['Height (cm)']
    x14=insertValues['BMI']
    x15=insertValues['AST']
    x16=insertValues['ALT']
    x17=insertValues['Alkaline Phosphate(ALP)']
    x18=insertValues['Total Bilirubin']
    x19=insertValues['Albumin']
    x20=insertValues['Family_history']

    input = np.array([[x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20,]])
    # 進行預測
    result = model.predict(input)

    return jsonify({'result': str(result)})