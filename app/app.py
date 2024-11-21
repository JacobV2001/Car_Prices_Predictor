from flask import Flask, request, render_template, jsonify
import numpy as np
import pickle
from model.utils import load_model, process_input

app = Flask(__name__)

# load model
model = load_model('app/model/model.plk')



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        make = request.form['make']
        model_name = request.form['model'] 
        condition = request.form['condition']
        mileage = float(request.form['mileage'])
        year = float(request.form['year'])

        print(f"Make: {make}, Model: {model_name}, Condition: {condition}, Mileage: {mileage}, Year: {year}")


        input_data = process_input(make, model_name, condition, mileage, year)

        print(f"Input data for model prediction: {input_data}")
        
        # 35,Chevrolet,Altima,2013,106330,Excellent,23683.4

        prediciton = model.predict(input_data)

        prediction_text = f'Predicted Price: ${prediciton[0]:,.2f}'

        return jsonify({'prediction': prediction_text})

    except Exception as e:
        return jsonify({'error': str(e)})    

if __name__ == "__main__":
    app.run(debug=True)