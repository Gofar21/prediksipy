import pickle
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
from altair import vegalite as vl
import io
import base64
from flask import Flask, render_template, request, Response, jsonify
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX




app = Flask(__name__)

# Load the model
model = pickle.load(open('model1.pkl', 'rb'))

# with open('model.pkl', 'rb') as file:
#     model = pickle.load(file)


# Load the dataset
df = pd.read_excel("laporan1.xlsx")
celana = df.loc[df['itemName'] == 'CELANA PENDEK PRIA DEWASA MOTIF SALUR GARIS']
celana['createTime'].min(), celana['createTime'].max()

cols = ['orderItemId','sellerSku', 'customerName', 'payMethod', 'billingAddr3', 'billingAddr4', 'billingAddr5', 'billingPhone', 'billingCountry', 'itemName', 'variation']
celana.drop(cols, axis=1, inplace=True)
celana = celana.sort_values('createTime')
celana.isnull().sum()

@app.route('/')
def home():
    return """
    <html>
        <head>
            <titl>forecesting penjualan</title>
        </head>
        <body>
            <form method="post" action="/predict">
                <label for="year">Tentukan Tahun:</label>
                <input type="number" id="year" name="year" min="1" max="30" step="1" required>
                <input type="submit" value="Predict">
            </form>
        </body>
    </html>
    """

@app.route('/predict', methods=['POST'])
def predict():
    input = request.form['year']

    hasil = model.predict(input)
    return hasil
    
    # year = int(request.form['createTime'])

    # # Make prediction
    # pred = model.forecast(year)
    # pred = pd.DataFrame(pred, columns=['paidPrice'])

    # # Plotting
    # fig, ax = plt.subplots()
    # df['paidPrice'].plot(style='--', color='gray', legend=True, label='known')
    # pred['paidPrice'].plot(color='b', legend=True, label='Prediction')
    # plt.title('Forecasting penjualan')
    
    # # Save the plot to a bytes object
    # img = io.BytesIO()
    # plt.savefig(img, format='png')
    # img.seek(0)
    # plot_url = base64.b64encode(img.getvalue()).decode()

    # return f"""
    # <html>
    #     <head>
    #         <title>Hasil Prediksi</title>
    #     </head>
    #     <body>
    #         <div>
    #             <h2>Hasil Prediksi:</h2>
    #             {pred.to_html()}
    #         </div>
    #         <div>
    #             <img src="data:image/png;base64, {plot_url}" alt="Prediction Plot">
    #         </div>
    #     </body>
    # </html>
    # """

# model = pickle.load(open('prediksi_co2.sav','rb'))

# @app.route('/')
# def home():
#     df = pd.read_excel("CO2 dataset.xlsx")
#     df['Year'] = pd.to_datetime(df['Year'], format='%Y')
#     df.set_index(['Year'], inplace=True)
#     return 'Tampil'

# st.title('Forecasting Kualitas Udara')
# year = st.slider("Tentukan Tahun",1,30, step=1)

# pred = model.forecast(year)
# pred = pd.DataFrame(pred, columns=['CO2'])

# if st.button("Predict"):

#     col1, col2 = st.columns([2,3])
#     with col1:
#         st.dataframe(pred)
#     with col2:
#         fig, ax = plt.subplots()
#         df['CO2'].plot(style='--', color='gray', legend=True, label='known')
#         pred['CO2'].plot(color='b', legend=True, label='Prediction')
#         st.pyplot(fig)


if __name__ == "__main__":
    app.run(debug=True)