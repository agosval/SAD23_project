"""
    Example Controllers
"""

from project import app
from flask import Flask, jsonify, render_template, request,redirect, url_for
import json
import subprocess
import time
import requests
from project.models import todo

todo_HPPOSLLH = todo.TodoHPPOSLLH()
todo_STATUS = todo.TodoSTASUS()
todo_HPPOSECEF = todo.TodoHPPOSECEF()



@app.route('/_stuff')
def stuff():
    response_API = requests.get('http://localhost:8080/_stuff')
    data = response_API.text
    data_temp = json.loads(data)
    todo_HPPOSLLH.create({'version': data_temp['result'][0]['version'], 'invalidLlh': data_temp['result'][0]['invalidLlh'],
                 'iTOW': data_temp['result'][0]['iTOW'], 'lon': data_temp['result'][0]['lon'],
                 'lat': data_temp['result'][0]['lat'],'height': data_temp['result'][0]['height'],
                 'hMSL': data_temp['result'][0]['hMSL'],'hAcc': data_temp['result'][0]['hAcc'],
                 'vAcc': data_temp['result'][0]['vAcc'],})
    
    todo_STATUS.create({'iTOW': data_temp['result2'][0]['iTOW'], 'gpsFix': data_temp['result2'][0]['gpsFix'],
                 'flags': data_temp['result2'][0]['flags'], 'fixStat': data_temp['result2'][0]['fixStat'],
                 'flags2': data_temp['result2'][0]['flags2'],'ttff': data_temp['result2'][0]['ttff'],
                 'msss': data_temp['result2'][0]['msss'],})
    
    #todo_HPPOSECEF.create({'version': data_temp['result3'][0]['version'], 'iTOW': data_temp['result3'][0]['iTOW'],
    #             'ecefX': data_temp['result3'][0]['ecefX'], 'ecefY': data_temp['result3'][0]['ecefY'],
    #             'ecefZ': data_temp['result3'][0]['ecefZ'],'ecefXHp': data_temp['result3'][0]['ecefXHp'],
    #             'ecefYHp': data_temp['result3'][0]['ecefYHp'],'ecefZHp': data_temp['result3'][0]['ecefZHp'],
    #             'invalidEcef': data_temp['result3'][0]['invalidEcef'],'pAcc': data_temp['result3'][0]['pAcc'],
    #             })    


    return jsonify(result_get=data_temp)

@app.route('/_stuff2')
def stuff2():
    data_temp=todo_HPPOSLLH.query1({})
    #print(data_temp)
    return jsonify(result_get=data_temp)

@app.route('/_stuff3')
def stuff3():
    data_temp=todo_HPPOSLLH.query2({})
    print(data_temp)
    return jsonify(result_get=data_temp)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def index2():
    return render_template('index.html')

@app.route('/RealTime.html')
def second_page():
    return render_template('RealTime.html')

@app.route('/StoredData.html')
def third_page():
    return render_template('StoredData.html')

@app.route('/casa.html')
def casa():
    return render_template('casa.html')
