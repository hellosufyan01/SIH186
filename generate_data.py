import numpy as np
import pandas as pd

np.random.seed(42)
n_samples = 1500

# Synthetic feature generation mirroring military stressors
personnel_id = [f"CAPF_{1000 + i}" for i in range(n_samples)]
consecutive_duty_days = np.random.randint(5, 65, n_samples)
leave_denials_past_year = np.random.poisson(lam=1.5, size=n_samples)
night_shifts_last_month = np.random.randint(0, 20, n_samples)
post_trauma_exposure = np.random.choice([0, 1], size=n_samples, p=[0.75, 0.25])
resting_hr = np.random.normal(loc=72, scale=10, size=n_samples).clip(55, 115)
hrv_rmssd = np.random.normal(loc=42, scale=12, size=n_samples).clip(15, 80)
self_reported_fatigue = np.random.randint(1, 10, n_samples)  # Mobile survey score (1-10)

# Calculate a deterministic baseline stress score with noise
stress_signal = (
    0.25 * (consecutive_duty_days / 60) +
    0.20 * (leave_denials_past_year / 5) +
    0.15 * (night_shifts_last_month / 20) +
    0.20 * post_trauma_exposure +
    0.10 * (resting_hr / 100) -
    0.15 * (hrv_rmssd / 70) +
    0.15 * (self_reported_fatigue / 10) +
    np.random.normal(0, 0.05, n_samples)
)

# Stratify into 4 risk tiers (0: Green, 1: Yellow, 2: Orange, 3: Red)
quantiles = np.quantile(stress_signal, [0.50, 0.75, 0.90])
risk_tier = np.digitize(stress_signal, quantiles)

df = pd.DataFrame({
    'personnel_id': personnel_id,
    'consecutive_duty_days': consecutive_duty_days,
    'leave_denials_past_year': leave_denials_past_year,
    'night_shifts_last_month': night_shifts_last_month,
    'post_trauma_exposure': post_trauma_exposure,
    'resting_hr': np.round(resting_hr, 1),
    'hrv_rmssd': np.round(hrv_rmssd, 1),
    'self_reported_fatigue': self_reported_fatigue,
    'risk_tier': risk_tier
})

df.to_csv("personnel_stress_dataset.csv", index=False)
print("Benchmark dataset successfully generated.")