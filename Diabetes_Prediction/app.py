from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load('diabetes_model.pkl')


# Open login page
@app.route('/')
def home():
    return render_template('login.html')


# Login function
@app.route('/login', methods=['POST'])
def login():

    username = request.form['username']
    password = request.form['password']

    if username == "admin" and password == "admin123":
        return render_template('predict.html')

    return "Invalid Username or Password"


# Prediction page
@app.route('/predict-page')
def predict_page():
    return render_template('predict.html')


# Predict diabetes
@app.route('/predict', methods=['POST'])
def predict():

    Pregnancies = float(request.form['Pregnancies'])
    Glucose = float(request.form['Glucose'])
    BloodPressure = float(request.form['BloodPressure'])
    SkinThickness = float(request.form['SkinThickness'])
    Insulin = float(request.form['Insulin'])
    BMI = float(request.form['BMI'])
    DiabetesPedigreeFunction = float(request.form['DiabetesPedigreeFunction'])
    Age = float(request.form['Age'])

    data = np.array([[Pregnancies,
                      Glucose,
                      BloodPressure,
                      SkinThickness,
                      Insulin,
                      BMI,
                      DiabetesPedigreeFunction,
                      Age]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        result = "Patient Has Diabetes"
    else:
        result = "Patient Does Not Have Diabetes"

    return render_template(
        'result.html',
        prediction_text=result
    )


if __name__ == "__main__":
    app.run(debug=True)