"""
    Example Controllers
"""

from project import app
from flask import Flask, jsonify, render_template, request,redirect, url_for
import json
import subprocess


@app.route('/_stuff', methods = ['GET'])
def stuff():
    f = open("C:/Users/Agostino/Documents/VS_code_repo/SAD23_project/dist/NAV_HPPOSLLH_json.json")
    f2 = open("C:/Users/Agostino/Documents/VS_code_repo/SAD23_project/dist/NAV_STATUS_json.json")
    f3 = open("C:/Users/Agostino/Documents/VS_code_repo/SAD23_project/dist/NAV_HPPOSECEF_json.json")

    data_temp_HPPOSLLH = json.load(f)
    data_temp_STATUS = json.load(f2)
    data_temp_HPPOSECEF = json.load(f3)
    
    #print(type(data_temp[0]['version']))
    #varq = str(data_temp['NAV_HPPOSLLH']['version'])
    return jsonify(result=data_temp_HPPOSLLH,result2=data_temp_STATUS,result3=data_temp_HPPOSECEF)


@app.route('/')
def index():
    return render_template('index.html')



