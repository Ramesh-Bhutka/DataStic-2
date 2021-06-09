# Importing essential libraries and modules

from flask import Flask, render_template, request, Markup
import numpy as np
import requests
import pickle
import io
import sklearn
from sklearn.preprocessing import StandardScaler
# ==============================================================================================

# -------------------------LOADING THE TRAINED MODELS -----------------------------------------------

# Loading plant disease classification model


# Loading crop recommendation model

diamond_price_prediction_model_path = 'models/Diamond-XGBRegressor.pkl'
diamond_price_prediction_model = pickle.load(
    open(diamond_price_prediction_model_path, 'rb'))


# =========================================================================================

# Custom functions for calculations

# ------------------------------------ FLASK APP -------------------------------------------------


app = Flask(__name__)

# render home page


@ app.route('/',methods=['GET'])
def home():
    title = 'D@taStics'
    return render_template('index.html', title=title)

@ app.route('/contact')
def contact():
    title = 'D@taStics'
    return render_template('contact.html', title=title)


@ app.route('/diamond-price-recommend')
def diamond_price_recommend():
    title = 'D@taStics'
    return render_template('diamond.html', title=title)


# ===============================================================================================


@ app.route('/diamond-price-predict', methods=['POST'])
def diamond_price_prediction():
    title = 'D@taStics'
    if  request.method=="POST":
        carat = float(request.form['carat'])
        cut = int(request.form['cut'])
        color = int(request.form['color'])
        clarity = int(request.form['clarity'])
        depth = float(request.form['depth'])
        table = float(request.form['table'])
        length = float(request.form['length'])
        width = float(request.form['width'])
        depth1 = float(request.form['depth1'])
    data = np.array([[carat,cut,color,clarity,depth,table,length,width,depth1]])
        # data = np.array([[company,kilometer_driven,fuel_type,transmission_type,owner,engine_size,maxpower,seats,mileage,year]])
    prediction=diamond_price_prediction_model.predict(data)

    return render_template('diamond-result.html', prediction=prediction, title="D@taStics")


# ===============================================================================================
if __name__ == '__main__':
    app.run(debug=False)