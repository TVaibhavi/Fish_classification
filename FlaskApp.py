# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 14:45:03 2022

@author: Vaibhavi
"""


import numpy as np
import pickle
import pandas as pd
from flask import Flask, request
from flask import Flask, request, jsonify, render_template

app=Flask(__name__)
pickle_in = open(r"E:\Semester-2\Noopa Prof\Huroku-Mar19\Lab4\fish_classifier.pkl",'rb')
classifier=pickle.load(pickle_in)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = classifier.predict(final_features)

    print(final_features)
    print(prediction)

    return render_template('index.html', prediction_text='The fish belong to species {}'.format(prediction))
    
    


if __name__=='__main__':
    app.run()