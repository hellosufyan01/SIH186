import matplotlib.pyplot as plt
import numpy as np
import joblib

payload = joblib.load("stress_risk_model.joblib")
model = payload["model"]
features = [f.replace('_', ' ').title() for f in payload["features"]]
importances = model.feature_importances_
indices = np.argsort(importances)

plt.figure(figsize=(8, 4.5))
plt.title("Key Predictive Indicators for Stress Escalation", fontsize=12, fontweight='bold')
plt.barh(range(len(indices)), importances[indices], color='#1e3a8a', align='center')
plt.yticks(range(len(indices)), [features[i] for i in indices])
plt.xlabel("Relative Importance Weight")
plt.tight_layout()
plt.savefig("feature_importance_plot.png", dpi=300)
print("Saved feature_importance_plot.png for presentation deck.")