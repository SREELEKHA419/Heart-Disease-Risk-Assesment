import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the sample data
df = pd.read_csv("sample_patients.csv")

# Prepare features and dummy labels
X = df.drop(columns=["name"])
y = [0, 1] * (len(X) // 2) + [0] * (len(X) % 2)  # Alternating 0 and 1

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save the model
joblib.dump(model, "model.pkl")
print("✅ model.pkl generated successfully!")
