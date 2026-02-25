from flask import Flask, render_template, request
import pickle
import re
import  numpy  as np

app = Flask(__name__)

# load model
model = pickle.load(open("model.pkl","rb"))
vectorizer = pickle.load(open("vectorizer.pkl","rb"))

# preprocessing (same as training!)
def preprocess(text):
    text = text.lower()
    
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'#', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/predict', methods=['POST'])
def predict():
    user_input = request.form['message']

    clean = preprocess(user_input)
    vector = vectorizer.transform([clean])
    prediction = model.predict(vector)[0]

    if prediction == 1:
        result = "Unsafe"
    else:
        result = "Safe"

    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)


import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))