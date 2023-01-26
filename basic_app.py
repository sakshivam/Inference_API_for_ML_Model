#from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pandas as pd
from fastapi import FastAPI, Request
import uvicorn
from mlflow.sklearn import load_model

## API INSTANTIATION
## ----------------------------------------------------------------
# Instantiating FastAPI
api = FastAPI()

## API ENDPOINTS
## ----------------------------------------------------------------
# Defining a test root path and message
@api.get('/')
def root():
  return {'message': 'Hello friends!'}

# Loading in model from sklearn.load_model
model = load_model(".\model")

# Creating the data model for data validation
class Coupon(BaseModel):
      passanger: int
      coupon: int
      CoffeeHouse: int
      destination: int
      expiration: int
      toCoupon_GEQ25min: int
      Bar: int
      gender: int
      Restaurant20To50: int
      temperature: int


## API ENDPOINTS
## ----------------------------------------------------------------
# Defining a test root path and message
@api.get('/')
def root():
  return {'message': 'Hello friends!'}
	
# Defining the prediction endpoint with data validation
@api.post('/predict')
def predict(Coupon: Coupon):

	# Converting input data into Pandas DataFrame
  df = pd.DataFrame([Coupon.dict()])
  print(df)

	# Getting the prediction from the loaded model from pickle file
  predictions = model.predict(df)
  # Return prediction
  pred = int(predictions)

  return pred


if __name__ == '__main__':
    uvicorn.run("basic_app:api", port=5001, host='0.0.0.0', reload=True)