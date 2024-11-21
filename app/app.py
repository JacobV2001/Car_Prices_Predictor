from flask import Flask, request, render_template, jsonify
from model.utils import load_model, process_input

app = Flask(__name__)

# load model
model = load_model('app/model/model.plk')


@app.route('/')
def home():
    # render homepage
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # get input data from form
        make = request.form['make']
        model_name = request.form['model'] 
        condition = request.form['condition']
        mileage = float(request.form['mileage'])
        year = float(request.form['year'])

        # process data
        input_data = process_input(make, model_name, condition, mileage, year)

        # get prediction
        prediction = model.predict(input_data)

        # return
        return jsonify({'prediction': f'Predicted Price: ${prediction[0]:,.2f}'})

    except Exception as e:
        return jsonify({'error': str(e)})    

if __name__ == "__main__":
    app.run()