from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from data_processing import process_data
import pickle

def train_model():

    # load processed data
    X, y = process_data()

    # train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12)

    # initialize and train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # predict based on test set
    pred = model.predict(X_test)

    # evaluate model
    mse = mean_absolute_error(y_test, pred)
    rmse = mse ** 0.5
    r2 = r2_score(y_test, pred)

    print(f'Mean Squared Error (MSE): {mse}')
    print(f'Root Mean Squared Error (MSE): {rmse}')
    print(f'R-squared (R2): {r2}')

    # create model save
    with open('app/model/model.plk', 'wb') as f:
        pickle.dump(model, f)

if __name__ == '__main__':
    train_model()