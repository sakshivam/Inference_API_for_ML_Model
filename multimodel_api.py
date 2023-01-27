#from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pandas as pd
from fastapi import FastAPI, Request
import uvicorn
from mlflow.sklearn import load_model
from utils.comFunctions import (config_read)

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
      co : str


## API ENDPOINTS
## ----------------------------------------------------------------
# Defining a test root path and message
@api.get('/')
def root():
  return {'message': 'Hello friends!'}
	
# Defining the prediction endpoint with data validation
@api.post('/predict')
def predict(Coupon: Coupon):
  ml_config = config_read('./mlops_config.yml')
  print("Selected model is", ml_config[Coupon.co] )  
  # Loading in model from sklearn.load_model
  model = load_model(".\multimodel\{}".format(ml_config[Coupon.co]))

  # Converting input data into Pandas DataFrame
  df = pd.DataFrame([Coupon.dict()])
  df_new = df.drop('co', axis=1)
  # print(df_new)
	# Getting the prediction from the loaded model from pickle file
  predictions = model.predict(df_new)
  # Return prediction
  pred = int(predictions)
  print("Predicted ouput is", pred)

  return { "Predicted output" : pred }


if __name__ == '__main__':
    uvicorn.run("multimodel_api:api", port=5002, host='0.0.0.0', reload=True)