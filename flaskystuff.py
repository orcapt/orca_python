#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 08:33:34 2017

@author: Pranavtadepalli
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
    return render_template('yourfile.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form['Curtain_OPENTIME']
        #print(result)
        return "thank you for filling out this form"
    else:
        print(0)

if __name__ == '__main__':
    app.run(debug = True,port=4300)
    