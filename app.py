
import pickle
import numpy as np
from flask import Flask, request
from flask import render_template

model = None
app = Flask(__name__)


def load_model():
    global model
    # model variable refers to the global variable
    with open('iris_trained_model.pkl', 'rb') as f:
        model = pickle.load(f)



@app.route('/')
def abc():
    return render_template("abc.html")


@app.route('/', methods=['POST'])
def abc_post():
    # Works only for a single sample
    a = request.form['a']
    b = request.form['b']
    c = request.form['c']
    d = request.form['d']
    a=float(a)
    b=float(b)
    c=float(c)
    d=float(d)
    data = np.array([a,b,c,d])[np.newaxis, :]
    prediction = model.predict(data)  # runs globally loaded model on the data
    
    return str(prediction[0])


if __name__ == '__main__':
    load_model()  # load model at the beginning once only
    app.run(host='0.0.0.0', port=80)