# SIMPLE CROP HEALTH PREDICTOR
# Uses AI to predict optimal growing conditions

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
import warnings
warnings.filterwarnings('ignore')

print("=== SIMPLE CROP HEALTH PREDICTOR ===")
print("Training AI model...")

# Load data
try:
    df = pd.read_csv('crop_data.csv')
    print("✅ Data loaded successfully!")
except:
    print("❌ Error: Could not load data")
    exit()

# Prepare the data
print("🔄 Preparing data for AI training...")

# Convert time if available
if 'Time' in df.columns:
    df['Time'] = pd.to_datetime(df['Time'], format='%d/%m/%Y, %H:%M:%S')
    df['Hour'] = df['Time'].dt.hour
    df['DayOfYear'] = df['Time'].dt.dayofyear

# Select features for AI model
feature_columns = []
if 'Humidity (%)' in df.columns:
    feature_columns.append('Humidity (%)')
if 'Light (lux)' in df.columns:
    feature_columns.append('Light (lux)')
if 'Soil Temperature (°C)' in df.columns:
    feature_columns.append('Soil Temperature (°C)')
if 'Ambient Temperature (°C)' in df.columns:
    feature_columns.append('Ambient Temperature (°C)')
if 'Hour' in df.columns:
    feature_columns.append('Hour')
if 'DayOfYear' in df.columns:
    feature_columns.append('DayOfYear')

# Check if we have moisture data to predict
if 'Moisture' not in df.columns:
    print("❌ Error: No 'Moisture' column found for prediction")
    exit()

print(f"🔧 Using features: {feature_columns}")

X = df[feature_columns]
y = df['Moisture']

# Split data for training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"📚 Training data: {len(X_train)} samples")
print(f"🧪 Testing data: {len(X_test)} samples")

# Train the AI model (Random Forest)
print("🤖 Training AI model...")
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Test the model
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

print(f"✅ Model trained successfully!")
print(f"📊 Training accuracy: {train_score:.3f}")
print(f"📊 Testing accuracy: {test_score:.3f}")

# Show feature importance
print("\n🔍 Feature Importance (what the AI learned):")
feature_importance = pd.DataFrame({
    'feature': feature_columns,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)

for _, row in feature_importance.iterrows():
    print(f"  {row['feature']}: {row['importance']:.3f}")

# Save the model
joblib.dump(model, 'crop_predictor_model.joblib')
print("💾 Model saved as 'crop_predictor_model.joblib'")

# Make a sample prediction
print("\n🔮 SAMPLE PREDICTION:")
sample_data = [X.iloc[0].values]  # Use first row as example
prediction = model.predict(sample_data)
actual = y.iloc[0]

print(f"   Actual moisture: {actual}")
print(f"   Predicted moisture: {prediction[0]:.1f}")
print(f"   Difference: {abs(prediction[0] - actual):.1f}")

print("\n" + "="*50)
print("AI TRAINING COMPLETE!")
print("The model can now predict soil moisture")
print("Next: Run the health analyzer")
print("="*50)
