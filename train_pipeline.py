import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, f1_score
from sklearn.model_selection import train_test_split

df = pd.read_csv("personnel_stress_dataset.csv")

feature_cols = [
    'consecutive_duty_days', 'leave_denials_past_year',
    'night_shifts_last_month', 'post_trauma_exposure',
    'resting_hr', 'hrv_rmssd', 'self_reported_fatigue'
]
X = df[feature_cols]
y = df['risk_tier']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train a robust baseline model
clf = RandomForestClassifier(
    n_estimators=120,
    max_depth=6,
    random_state=42,
    class_weight='balanced'
)
clf.fit(X_train, y_train)

# Evaluation
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred, target_names=["Low (Green)", "Moderate (Yellow)", "Elevated (Orange)", "High (Red)"]))

# Save model and metadata
pipeline_payload = {
    "model": clf,
    "features": feature_cols,
    "risk_labels": {0: "Green (Low)", 1: "Yellow (Moderate)", 2: "Orange (Elevated)", 3: "Red (Critical)"}
}
joblib.dump(pipeline_payload, "stress_risk_model.joblib")
print("Model saved as stress_risk_model.joblib")