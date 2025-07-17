from flask import Flask, render_template, request
import mysql.connector
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("model.pkl")

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Add password if needed
        database="heart_disease_db"
    )

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = [
            request.form.get("age"),
            request.form.get("sex"),
            request.form.get("cp"),
            request.form.get("trestbps"),
            request.form.get("chol"),
            request.form.get("fbs"),
            request.form.get("restecg"),
            request.form.get("thalach"),
            request.form.get("exang"),
            request.form.get("oldpeak"),
            request.form.get("slope"),
            request.form.get("ca"),
            request.form.get("thal"),
        ]
        features = np.array(data, dtype=float).reshape(1, -1)
        pred = model.predict(features)[0]
        prob = model.predict_proba(features)[0][1]

        name = request.form.get("name")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO patients (name, age, sex, cp, trestbps, chol, fbs, restecg,
                                  thalach, exang, oldpeak, slope, ca, thal)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, tuple([name] + data))
        conn.commit()

        patient_id = cursor.lastrowid
        cursor.execute("""
            INSERT INTO predictions (patient_id, risk_prediction)
            VALUES (%s, %s)
        """, (patient_id, "High" if pred else "Low"))
        conn.commit()

        prediction = "High" if pred else "Low"
        probability = round(prob * 100, 2)

        return render_template("result.html", prediction=prediction, probability=probability)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
