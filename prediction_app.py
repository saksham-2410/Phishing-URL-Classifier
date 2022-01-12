import uvicorn
from fastapi import FastAPI
import pickle

app = FastAPI()

#pkl
phish_model_ls = pickle.load(open('phishing.pkl', 'rb'))

# ML Aspect
@app.get('/predict/{feature}')
async def predict(features):
	X_predict = []
	X_predict.append(str(features))
	y_Predict = phish_model_ls.predict(X_predict)
	if y_Predict == 'bad':
		result = "This is a Phishing Site"
	else:
		result = "This is not a Phishing Site"

	return (features, result)
if __name__ == '__main__':
	uvicorn.run(app,host="127.0.0.1",port=8000)