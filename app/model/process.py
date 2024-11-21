import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# function to process input data for prediction
def process_data(data):

    # features added
    makes = ['Chevrolet', 'Ford', 'Honda', 'Nissan', 'Toyota']
    models = ['Altima', 'Camry', 'Civic', 'F-150', 'Silverado']

    # map the make feature
    for make in makes:
        data[f'Make_{make}'] = data['Make'].apply(lambda x: x == make)
    
    # map the model feature
    for model in models:
        data[f'Model_{model}'] = data['Model'].apply(lambda x: x == model)
    
    # drop make & model
    data.drop(columns=['Make', 'Model'], inplace=True)    

    # map condition variable
    condition_mapping = {'Excellent': 2, 'Good': 1, 'Fair': 0}
    data['Condition'] = data['Condition'].map(condition_mapping)

    # convert year to age
    data['Age'] = 2024 - data['Year']
    data.drop(columns=['Year'], inplace=True)

    # reorder columns
    make_columns = [col for col in data.columns if col.startswith('Make_')]
    model_columns = [col for col in data.columns if col.startswith('Model_')]
    other_columns = [col for col in data.columns if col not in make_columns and col not in model_columns]

    # final order
    final_column_order = make_columns + model_columns + ['Mileage', 'Age', 'Condition']
    data = data[final_column_order]

    return data