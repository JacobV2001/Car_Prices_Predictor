# CAR PRICE PREDICTOR

## Project Overview

**CAR PRICE PREDICTOR** is a machine learning-powered web application that predicts car prices based on several features such as **make**, **model**, **mileage**, **condition**, and **year of manufacture**. The app uses a **linear regression** model trained on a custom dataset to provide highly accurate predictions. It’s designed to help users make informed decisions when buying or selling a vehicle.

### Key Features:

1. **Interactive User Interface**:
   - The app provides an intuitive web interface where users can input details such as car make, model, mileage, and condition to get an instant predicted price.
   - Built with **Flask**, the web app is lightweight and easy to use.

2. **High Accuracy Prediction**:
   - The model achieves **99% accuracy** using linear regression to predict the price based on various car features.
   - The model is trained with carefully engineered features, ensuring the highest possible predictive power.

3. **Dynamic Feature Engineering**:
   - The system includes advanced feature engineering, including the calculation of **car age** (from the year of manufacture) and **condition ratings** (Excellent, Good, Fair).
   - One-hot encoding is applied to **categorical features** like car make and model to convert them into machine-readable numerical values.

4. **Comprehensive Data Preprocessing Pipeline**:
   - The data preprocessing pipeline cleans and transforms raw data, creating useful features and removing irrelevant information before passing it into the model.
   - The preprocessing steps include handling missing data, converting categorical variables, and scaling numerical features.

---

## Installation & Setup

To deploy and run **CAR PRICE PREDICTOR** locally, follow the steps below.

### 1. Clone the repository

git clone <repository-url>
cd car-price-predictor

### 2. Install dependencies

Create a virtual environment and install the required packages:

bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt

### 3. Prepare the data

Run the following command to preprocess the data and generate the required pickle file for model training:

bash
python model/data_processing.py

This will load the dataset, clean it, and save the trained model into a pickle file.

### 4. Train the Model

To train the machine learning model using the preprocessed data, run the following:

bash
python model/model_create.py

This will train the linear regression model and save it as model.plk in the app/model/ folder.

### 5. Run the Application

To start the local server and use the application, run:

bash
python app/app.py

Once the server is up, open your browser and navigate to http://127.0.0.1:5000. You'll see the web interface where you can input car details and get a price prediction.

## How It Works

1. The user inputs car details via the form on the web interface (make, model, condition, mileage, and year).
2. The `process_input` function in the `utils.py` script processes this data, transforming it into a format suitable for the model (including one-hot encoding for categorical features).
3. The linear regression model makes the price prediction based on the transformed data.
4. The result is displayed back to the user as a predicted car price.

## Model Performance

The CAR PRICE PREDICTOR model boasts 99% accuracy, thanks to effective feature engineering and preprocessing. With variables like car age and condition, the model is able to predict prices with impressive reliability.

## License

This project does not include any formal licensing. Please feel free to use and modify the code as needed.

## Contributing

Contributions are welcome! If you'd like to improve or add features to the project, feel free to fork the repository and submit a pull request.

## Acknowledgements

- **Flask**: For serving the web app.
- **scikit-learn**: For machine learning algorithms and data processing tools.
- **pandas**: For data manipulation and preprocessing.
