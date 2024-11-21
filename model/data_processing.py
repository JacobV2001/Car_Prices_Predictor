import pandas as pd

def process_data():

    # load dataset
    data = pd.read_csv('data/CarPricesPrediction.csv')

    # drop meaningless column
    data.drop(columns=['Unnamed: 0'], inplace=True)

    # change categorical non-ordinal cols with one-hot-encoding ('Make', 'Model')
    categorical_nonord = data[['Make', 'Model']]
    categorical_nonord = pd.get_dummies(categorical_nonord)

    # change ordinal 'Condition' into mapped numerical
    condition_mapping = {'Excellent': 2, 'Good': 1, 'Fair': 0}
    data['Condition'] = data['Condition'].map(condition_mapping)

    # create 'Age' feature based on current year
    data['Age'] = 2024 - data['Year']
    data.drop(columns=['Year'], inplace=True)

    # define X and y
    X = pd.concat([categorical_nonord, data[['Mileage', 'Age', 'Condition']]], axis = 1)
    y = data['Price']

    # Create CSV for each (optional)
    #X.to_csv('data/processed_X.csv', index=False)
    #y.to_csv('data/processed_y.csv', index=False)

    return X, y