# CAR PRICE PREDICTOR

## Table of Contents
1. [Project Overview](#project-overview)
2. [Key Features](#key-features)
3. [Skills Demonstrated](#skills-demonstrated)
4. [Installation & Setup](#installation--setup)
5. [How It Works](#how-it-works)
6. [Model Performance](#model-performance)




## Project Overview

**CAR PRICE PREDICTOR** is a machine learning-powered web application that predicts car prices based on several features such as **make**, **model**, **mileage**, **condition**, and **year of manufacture**. The app uses a **linear regression** model trained on a custom dataset to provide highly accurate predictions. It’s designed to help users make informed decisions when buying or selling a vehicle based on the data provided.

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

4. **Comprehensive Data Preprocessing**:
   - The data preprocessing cleans and transforms raw data, creating useful features and removing irrelevant information before passing it into the model.
   - The preprocessing steps include converting categorical variables, and scaling numerical features.

---

## Skills Demonstrated
- **Machine Learning:** Applied linear regression to predict car prices based on input features. 
- **Feature Engineering:** Performed advanced feature engineering, including one-hot encoding and feature scaling.
- **Data Preprocessing:** Cleaned and transformed raw data for model readiness.
- **Web Development:** Built a user-friendly web interface with Flask to interact with the machine learning model.
- **Model Evaluation:** Achieved high model accuracy (99%) and evaluated performance.



## Installation & Setup

To deploy and run **CAR PRICE PREDICTOR** locally, follow the steps below.

### 1. Clone the repository

git clone <repository-url>
<br>cd car-price-predictor

### 2. Install dependencies

Create a virtual environment and install the required packages:

<br>pip install -r requirements.txt

### 3. Prepare the data

Run the following command to preprocess the data and generate the required pickle file for model training:

python model/data_processing.py

This will load the dataset, clean it, and save the trained model into a pickle file.

### 4. Train the Model

To train the machine learning model using the preprocessed data, run the following:

python model/model_create.py

This will train the linear regression model and save it as model.plk in the app/model/ folder.

### 5. Run the Application

To start the local server and use the application, run:

python app/app.py

Once the server is up, open your browser and navigate to http://127.0.0.1:5000. You'll see the web interface where you can input car details and get a price prediction.

## How It Works

1. The user inputs car details via the form on the web interface (make, model, condition, mileage, and year).
2. The `process_input` function in the `utils.py` script processes this data, transforming it into a format suitable for the model (including one-hot encoding for categorical features).
3. The linear regression model makes the price prediction based on the transformed data.
4. The result is displayed back to the user as a predicted car price.

## Model Performance

The CAR PRICE PREDICTOR model boasts 99% accuracy, thanks to effective feature engineering and preprocessing. With variables like car age and condition, the model is able to predict prices with impressive reliability.