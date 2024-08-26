from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import pickle



app = Flask(__name__)

data = pd.read_excel('laporan1.xlsx')
model = pickle.load(open('model.pkl', 'rb'))


def analyze_time_series(data):
    # Analisis time series dan forecast
    # ...
    pass

@app.route('/', methods=['GET'])
def home():

    
    # Membaca data dari file csv atau sumber lainnya
    data = pd.read_excel('laporan1.xlsx')

    # Melakukan analisis time series dan forecast
    result = analyze_time_series(len(data))

    return jsonify(result)

@app.route('/forecast', methods=['GET'])
def forecast():
    # Mengambil model yang telah disimpan sebelumnya
    model = pickle.load(open('model.pkl', 'rb'))

    # Melakukan forecast berdasarkan model yang telah disimpan
    forecast_result = model.predict(len(data))

    return jsonify(forecast_result)

@app.route('/save-model', methods=['POST'])
def save_model():
    # Menerima model melalui request POST
    model = request.get_json()

    # Menyimpan model ke dalam file
    pickle.dump(model, open('model.pkl', 'wb'))

    return jsonify({'message': 'Model berhasil disimpan'})

@app.route('/get-model', methods=['GET'])
def get_model():
    # Mengambil model yang telah disimpan sebelumnya
    model = pickle.load(open('model.pkl', 'rb'))

    return jsonify(model)

if __name__ == '__main__':
    app.run(debug=True)