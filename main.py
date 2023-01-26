from fastapi import FastAPI
from typing import Any, List, Union
from pydantic import BaseModel
import uvicorn
import mlflow
import pandas as pd
from mlflow.sklearn import load_model

api = FastAPI()


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



# @api.post("/prediction'", response_model=Coupon)
# async def create_item(Coupon: Coupon) -> Any:
#     return Coupon

@api.get('/predict')
def pred() -> Any:
    # Takes and input as list of json and returns output as list
    data = [{"passanger": 1,
             "coupon": 2,
             "CoffeeHouse": 2,
             "destination": 2,
             "expiration": 1,
             "toCoupon_GEQ25min": 0,
             "Bar": 1,
             "gender": 1,
             "Restaurant20To50": 0,
             "temperature": 80
             },
            {"passanger": 0,
             "coupon": 0,
             "CoffeeHouse": 1,
             "destination": 0,
             "expiration": 0,
             "toCoupon_GEQ25min": 0,
             "Bar": 0,
             "gender": 0,
             "Restaurant20To50": 0,
             "temperature": 1}]
    df = pd.json_normalize(data)

    model = load_model(".\model")

    predictions = model.predict(df)
    pred = int(predictions[1])

    res = {"prediction": pred}

    return res


if __name__ == "__main__":
    uvicorn.run( "main:api", host="0.0.0.0", port=1234, reload=True)
