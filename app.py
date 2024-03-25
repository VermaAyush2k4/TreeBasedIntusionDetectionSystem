# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np
import os

# Load the Random Forest CLassifier model
filename = 'dt_model.pkl'
model = pickle.load(open(filename, 'rb'))

app = Flask(__name__ )

@app.route('/')
def home():
	return render_template('main.html')


@app.route('/predict', methods=['GET','POST'])

# modelSelected = str(request.form['selectModel'])
def predict():
    if request.method == 'POST':
        bwdPacketLengthStd = float(request.form['bwdPacketLengthStd'])
        bwdPacketLengthMin = float(request.form['bwdPacketLengthMin'])
        averagePacketSize = float(request.form['averagePacketSize'])
        initWinbytesbackward = float(request.form['initWinbytesbackward'])
        initWinbytesforward = float(request.form['initWinbytesforward'])
        pSHFlagCount = float(request.form['pSHFlagCount'])
        bwdPackets = float(request.form['bwdPackets'])
        avgBwdSegmentSize = float(request.form['avgBwdSegmentSize'])
        packetLengthStd = float(request.form['packetLengthStd'])
        bwdPacketLengthMean = float(request.form['bwdPacketLengthMean'])
        fwdHeaderLength = float(request.form['fwdHeaderLength'])
        packetLengthMean = float(request.form['packetLengthMean'])
        bwdHeaderLength = float(request.form['bwdHeaderLength'])
        minsegsizeforward = float(request.form['minsegsizeforward'])
        actdatapktfwd = float(request.form['actdatapktfwd'])
        modelSelected = int(request.form.get('selectModel'))


        data = np.array([[bwdPacketLengthStd,bwdPacketLengthMin,averagePacketSize,initWinbytesbackward,initWinbytesforward,
                          pSHFlagCount,bwdPackets,avgBwdSegmentSize,packetLengthStd,bwdPacketLengthMean,fwdHeaderLength,
                          packetLengthMean,bwdHeaderLength,minsegsizeforward,actdatapktfwd]])
        filedata = ['dt_model.pkl','et_model.pkl', 'rf_model.pkl', 'xg_model.pkl']
        filename = filedata[modelSelected]
        model = pickle.load(open(filename, 'rb'))
        my_prediction = model.predict(data)
        
    return render_template('result.html', prediction=my_prediction , selection = modelSelected)

if __name__ == '__main__':
	app.run(debug=True)
	# port = int(os.environ.get('PORT', 5000))
	# app.run(host='0.0.0.0', port=port, debug=True)