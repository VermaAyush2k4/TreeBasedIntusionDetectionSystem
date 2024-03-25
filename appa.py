# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np
import os
import pandas as pd 
import csv

# Load the Random Forest CLassifier model
filename = 'dt_model.pkl'
model = pickle.load(open(filename, 'rb'))

app = Flask(__name__ )

@app.route('/')
def home():
	return render_template('main1.html')


@app.route('/predict', methods=['GET','POST'])

# modelSelected = str(request.form['selectModel'])
def predict():
    if request.method == 'POST':
        inputselected = int(request.form.get('selectinput'))
        modelSelected = int(request.form.get('selectModel'))
        inputdata = ['input1.csv','input2.csv']
        inputname = inputdata[inputselected]
        data=pd.read_csv(inputname)
        print(data)
        data=np.array(data)
        data=data.reshape(1,-1)
        filedata = ['dt_model.pkl','et_model.pkl', 'rf_model.pkl', 'xg_model.pkl']
        filename = filedata[modelSelected]
        model = pickle.load(open(filename, 'rb'))
        my_prediction = model.predict(data)
        
    return render_template('result1.html', prediction=my_prediction , selection = modelSelected)

if __name__ == '__main__':
	app.run(debug=True)
	# port = int(os.environ.get('PORT', 5000))
	# app.run(host='0.0.0.0', port=port, debug=True)