# -*- coding: UTF-8 -*-
import app.model as model
import numpy as np

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['GET'])
def getResult():
    input = np.array([[1, 66, 80, 126, 51, 74, 118, 40, 57, 15, 6.3, 118, 98.3, 0, 167, 91, 173, 30.4, 131, 85.6, 172, 2.45, 2.8, 0]])
    result = model.predict(input)
    return jsonify({'result': str(result)})

@app.route('/predict', methods=['POST'])
def postInput():
    # 取得前端傳過來的數值
    insertValues = request.get_json()
    x1=insertValues['gender']
    x2=insertValues['anchor_age']
    x3=insertValues['HR']
    x4=insertValues['ABPs']
    x5=insertValues['ABPd']
    x6=insertValues['ABPm']
    x7=insertValues['NBPs']
    x8=insertValues['NBPd']
    x9=insertValues['NBPm']
    x10=insertValues['RR']
    x11=insertValues['Hemoglobin']
    x12=insertValues['Glucose (serum)']
    x13=insertValues['Temperature F']
    x14=insertValues['Unintentional weight loss >10 lbs.']
    x15=insertValues['Glucose finger stick (range 70-100)']
    x16=insertValues['Admission Weight (Kg)']
    x17=insertValues['Height (cm)']
    x18=insertValues['BMI']
    x19=insertValues['AST']
    x20=insertValues['ALT']
    x21=insertValues['Alkaline Phosphate(ALP)']
    x22=insertValues['Total Bilirubin']
    x23=insertValues['Albumin']
    x24=insertValues['Family_history']

    input = np.array([[x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24]])
    # 進行預測
    result = model.predict(input)

    return jsonify({'result': str(result)})