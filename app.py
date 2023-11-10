from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the trained model using pickle
with open('decision_tree_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from HTML form
        charge = float(request.form['charge'])
        distance = float(request.form['distance'])
        
        # Make prediction using the loaded model
        prediction = model.predict([[charge, distance]])[0]

        # Construct the prediction message
        prediction_message = f'Predicted Air Over Pressure(in dB): {prediction}'

        # Render the prediction message on the index.html template
        return render_template('index.html', prediction_message=prediction_message)
    except Exception as e:
        return render_template('index.html', prediction_message=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)





