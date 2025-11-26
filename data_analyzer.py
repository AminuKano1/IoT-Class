# SIMPLE DATA ANALYZER FOR CROP HEALTH
# This program helps you understand your data

import pandas as pd
import matplotlib.pyplot as plt

print("=== CROP DATA ANALYZER ===")
print("Loading your data...")

# Load the CSV file
try:
    df = pd.read_csv('crop_data.csv')
    print(" Data loaded successfully!")
except:
    print(" Error: Could not find 'crop_data.csv'")
    print("Please make sure the file is in the same folder")
    exit()

# Show basic information
print(f"\n Dataset has {len(df)} rows and {len(df.columns)} columns")
print("\nColumn names:")
for col in df.columns:
    print(f"  - {col}")

print("\n First 5 rows of data:")
print(df.head())

print("\n Basic statistics:")
print(df.describe())

# Convert time column if it exists
if 'Time' in df.columns:
    df['Time'] = pd.to_datetime(df['Time'], format='%d/%m/%Y, %H:%M:%S')
    print("\n Time data converted successfully!")

# Create simple plots
print("\n Creating basic charts...")

plt.figure(figsize=(12, 8))

# Plot 1: Soil Temperature over time
plt.subplot(2, 2, 1)
if 'Soil Temperature (°C)' in df.columns:
    plt.plot(df['Soil Temperature (°C)'])
    plt.title('Soil Temperature')
    plt.ylabel('Temperature (°C)')

# Plot 2: Moisture levels
plt.subplot(2, 2, 2)
if 'Moisture' in df.columns:
    plt.plot(df['Moisture'])
    plt.title('Soil Moisture')
    plt.ylabel('Moisture')

# Plot 3: Humidity
plt.subplot(2, 2, 3)
if 'Humidity (%)' in df.columns:
    plt.plot(df['Humidity (%)'])
    plt.title('Humidity')
    plt.ylabel('Humidity (%)')

# Plot 4: Light levels
plt.subplot(2, 2, 4)
if 'Light (lux)' in df.columns:
    plt.plot(df['Light (lux)'])
    plt.title('Light Intensity')
    plt.ylabel('Light (lux)')

plt.tight_layout()
plt.savefig('data_overview.png')
print(" Charts saved as 'data_overview.png'")

print("\n" + "="*50)
print("ANALYSIS COMPLETE!")
print("Check the charts and statistics above")
print("Next: Run the prediction program")
print("="*50)
