
 ❤️ Heart Disease Risk Assessment App

A machine learning web application that predicts the likelihood of heart disease based on user-provided health data. Built with Flask, the app uses a trained model to assess medical risk and display results in a user-friendly interface.

---

 Project Structure

```

heart-disease-risk-app/
├── app.py                # Flask backend for input and prediction
├── train\_model.py        # Script to train and export the model
├── model.pkl             # Trained machine learning model (e.g., Random Forest)
├── sample\_patients.xlsx  # Sample patient data for reference
├── requirements.txt      # Required Python libraries
├── static/               # Optional CSS styling
│   └── style.css
├── templates/            # HTML templates
│   ├── index.html        # Input form for user data
│   └── result.html       # Displays prediction results
├── OUTPUTS/              # Folder to store optional result files or screenshots
└── README.md             # Project documentation

````

---

 How to Run the App

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/heart-disease-risk-app.git
   cd heart-disease-risk-app
````

2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

3. Train the model (optional if `model.pkl` already exists)

   ```bash
   python train_model.py
   ```

4. Run the Flask app

   ```bash
   python app.py
   ```

5. Visit the application in your browser

   ```
   http://localhost:5000
   ```

---

 Tech Stack

* Python
* Flask
* Scikit-learn
* HTML/CSS (Jinja2 templates)
* pandas, joblib

---

 License

This project is licensed under the [MIT License](LICENSE).

---

AUTHOR:

Sreelekha A S
B.Tech CSE | B.S. Abdur Rahman Crescent Institute of Science and Technology,Chennai
