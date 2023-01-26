## Creating InferenceAPI from model file(pickle file) using FastAPI

# Pre-requisites:
1. A pickle file for a trained ML model

# Steps for this project:
1. Create a directory for the project
2. Create a virtual environment for the project using pip or conda. 
3. Activate that virtual environment
4. Prepare a requirements.txt file for dependencies required to be installed
5. Install all packages from requirements.txt - pip install -r requirements.txt
6. Create a python file to create API

We are using FastAPI since it is faster than Flask. Also It includes built in Swagger docs and built in data validation.

When we have the required model file in pickle format. Now we have to perform the following:

# 1. Instantiating FastAPI with a Basic GET Endpoint

For this we need to install fastapi uvicorn 

Both Flask and FastAPI require a sort of gateway interface. Flask required a WSGI server in the form of something like gunicorn, and uvicorn is essentially the “spiritual” successor to WSGI in what is called an ASGI server. 

from fastapi import FastAPI, Request
#Instantiating FastAPI
api = FastAPI()
#Defining a test root path and message
@api.get('/')
def root():
  return {'message': 'Hello friends!'}

This is a simple and functional API created using FastAPI. 
Testing Our API:
The above code defined all the path operation in the file that we’ll name as basic_app.py.  Now to run this file we’ll open the terminal in our directory and write the following command:-

uvicorn basic_app:api --reload

Now the above command follows the following format:-

basic-app refers to the name of the file we created our API in.
api refers to the FastAPI instance we declared in the file.
–reload tells to restart the server every time we reload.

Now after you run this command and go to http://127.0.0.1:8000/ to see msg in your browser. By default host address is 127.0.0.1:8000

One thing to note is that our message was a Python Dictionary but it was converted to JSON automatically. 

Now when we go to the address: http://127.0.0.1:8000/sakshi i.e we have provided name as sakshi to second endpoint, we get the 
new message on the browser as {"message":"Welcome to MLmodel API!, sakshi"}

To change host and port, we need to execute in terminal:

uvicorn basic_app:api --host 0.0.0.0 --port 5001 --reload
uvicorn main:api --host 0.0.0.0 --port 1234 --reload

it is looking for a Python file entitled basic_app.py and then looking for an instance of FastAPI also entitled api. We then bind this to host 0.0.0.0 on port 5001.

We can see this message on our terminal if we type the following command in second terminal:
curl localhost:5001

# Interactive API docs:

Now to get the above result we had to manually call each endpoint but FastAPI comes with Interactive API docs which can be accessed by adding /docs in our path. To access docs  we’ll go to http://localhost:5001/docs. Here we will get the  page where we can test the endpoints by seeing the output they’ll give for the corresponding inputs if any.

Swagger has already cataloged our basic GET endpoint here.

# The Request Body:

The data sent from the client side to the API is called a request body. The data sent from API to the client is called a response body. 

To define our request body we’ll use BaseModel ,in pydantic module, and define the format of the data we’ll send to the API. To define our request body, we’ll create a class that inherits BaseModel and define the features as the attributes of that class along with their type hints. What pydantic does is that it defines these type hints during runtime and generates an error when data is invalid. So let’s create our request_body class

e.g.
from pydantic import BaseModel
class Coupon(BaseModel):
      passanger: int
      coupon: int
      CoffeeHouse: int
      destination: int

# The Endpoint:
After mentioning request_body as class, all that’s left to do is to add an endpoint that’ll predict the class and return it as a response.

# 2. Creating Basic Inference Endpoint around the trained model.
we’re now ready to start building an endpoint around the model we already trained and saved as pickle.
let’s first import the other Python libraries we’ll need as well as loading up the model itself

import pandas as pd
import pickle

#Loading in model from serialized .pkl file

pkl_filename = "model.pkl"
with open(pkl_filename, 'rb') as file:
  model = pickle.load(file)

Also we can load the model using sklearn.load_model using following commands:
from mlflow.sklearn import load_model
model = load_model(".\model")

Finally we will create a new post endpoint that will receive our test data to model. In this endpoint 

#Defining the prediction endpoint with data validation

@api.post('/predict')
def predict(Coupon: Coupon):

	# Converting input data into Pandas DataFrame

  df = pd.DataFrame([Coupon.dict()])
  print(df)

	# Getting the prediction from the loaded model from pickle file

  predictions = model.predict(df)
  #print(predictions)
  pred = int(predictions)

  return pred

we’ll pass data into that model for inferences by calling the model’s .predict() function.
we take the JSON from the body of the request, turn it into a Pandas DataFrame, pass the DataFrame into the  model to produce an inference, and finally return that inference back to the user.

Now to tryout, we can use some shell scripts:

e.g running a shell script through command: bash script_name.sh

or we can use single line command on the terminal to give input in json format to call API to predict data:

curl -X POST http://localhost:5001/predict -d @data\test_data.json --header "Content-Type: application/json"
