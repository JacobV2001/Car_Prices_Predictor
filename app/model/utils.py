import pickle
import pandas as pd
import numpy as np
from model.process import process_data

# function to load model from pickle file
def load_model(model_path):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model

# function to frame and return data from input
def process_input(make, model_name, condition, mileage, year):
    input_data = pd.DataFrame({
        'Make': [make],
        'Model': [model_name],
        'Condition': [condition],
        'Mileage': [mileage],
        'Year': [year]
    })

    # send data to be processed
    input_data = process_data(input_data)

    # return array of data
    return np.array(input_data)