from flask import Flask, render_template, request
from sentimental import getVanderSentiment,vander_score, remove_char
import pandas as pd
import joblib
from custom_tokenizer_function import CustomTokenizer

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/predict',methods=["get",'POST'])
def predict():
    model = joblib.load('sentiment_model.pkl')
    new_review = [[str(x) for x in request.form.values()]]
    data = pd.DataFrame(new_review)
    data.columns = ['new_review']
    predictions = model.predict(new_review)[0]
    return render_template('index.html',prediction_text=predictions)


@app.route('/sentimental', methods=['post','get'])
def handle_form():
	data = request.form
	for key,val in data:
		print(key,val)
	return data
    # companyname = request.args.get('companyname')
    # output = request.args.get('output');print(output)
    # return getVanderSentiment(output)

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug = True)