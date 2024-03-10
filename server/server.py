from flask import Flask, render_template, request
import pandas as pd
import pickle
import json

app = Flask(__name__)

model = pickle.load(open('C:/Users/mohammad asfraf/OneDrive/Desktop/Machine Learning/projects/BHP/server/artifacts/BHP.pkl', 'rb'))

with open('C:/Users/mohammad asfraf/OneDrive/Desktop/Machine Learning/projects/BHP/server/artifacts/BHP_Columns.json', 'r') as json_data:
    data = json.load(json_data)
    locations = data['data_locations']

@app.route('/')
def home():
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    location = request.form['location']
    total_sqft = float(request.form['total_sqft'])
    bath = float(request.form['bath'])
    bhk = int(request.form['bhk'])

    prediction = model.predict([[location, total_sqft, bath, bhk]])

    return render_template('index.html', prediction_text='Predicted price: {}'.format(prediction))

if __name__ == "__main__":
    app.run(debug=True)