from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('kamal_2020.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        sf = int(request.form['Sqrft'])
        sm=int(request.form['smeter'])
        loc=int(request.form['location'])
        prediction=model.predict([[sf,loc]])
        output=round(prediction[0],2)
        
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            #return output
            return render_template('index.html',prediction_text="You Can Rent in this price approximatly {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=False)

