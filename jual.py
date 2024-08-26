import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt
import pickle


df = pd.read_excel('laporan1.xlsx')
penjualan = df.loc[df['itemName'] == 'CELANA PENDEK PRIA DEWASA MOTIF SALUR GARIS']
penjualan = penjualan.interpolate(method='linear')

plot_acf(penjualan)
plot_pacf(penjualan)
plt.show()

model = SARIMAX(penjualan, order=(p, d, q), seasonal_order=(P, D, Q, s))
results = model.fit(disp=False)

print(results.summary())

forecast = results.get_forecast(steps=n)
pred_uc = forecast.predicted_mean
pred_ci = forecast.conf_int()

pickle.dump(model, open('model1.pkl', 'wb'))