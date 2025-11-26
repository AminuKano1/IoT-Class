# COMPLETE CROP HEALTH SYSTEM
# Runs all components together

import os
import subprocess
import time

print("🌱 COMPLETE CROP HEALTH PREDICTION SYSTEM")
print("=" * 50)

def run_program(program_name, description):
    print(f"\n▶️ RUNNING: {description}")
    print("-" * 40)
    
    try:
        # Run the program and capture output
        result = subprocess.run(['python3', program_name], 
                             capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Completed successfully!")
            # Print the output
            print(result.stdout)
        else:
            print(f"❌ Error running {program_name}")
            print(result.stderr)
            
    except Exception as e:
        print(f"❌ Failed to run {program_name}: {e}")
    
    time.sleep(2)  # Pause between programs

def check_file_exists(filename):
    if os.path.exists(filename):
        return True
    else:
        print(f"❌ Missing: {filename}")
        return False

# Check if data file exists
if not check_file_exists('crop_data.csv'):
    print("\n📝 Please make sure 'crop_data.csv' is in this folder")
    print("   You can:")
    print("   1. Copy your CSV file here")
    print("   2. Rename it to 'crop_data.csv'")
    exit()

print("✅ All files found!")

# Run the system step by step
print("\n🎯 STARTING ANALYSIS PIPELINE...")

# Step 1: Data Analysis
run_program('data_analyzer.py', 'Data Analysis and Visualization')

# Step 2: AI Prediction Model
run_program('simple_predictor.py', 'AI Model Training')

# Step 3: Health Analysis
run_program('health_analyzer.py', 'Crop Health Recommendations')

print("\n" + "=" * 50)
print("🎉 SYSTEM RUN COMPLETE!")
print("=" * 50)
print("\n📁 FILES CREATED:")
files_created = []
if os.path.exists('data_overview.png'):
    files_created.append('📊 data_overview.png (Data charts)')
if os.path.exists('crop_predictor_model.joblib'):
    files_created.append('🤖 crop_predictor_model.joblib (AI model)')

if files_created:
    for file in files_created:
        print(f"   {file}")
else:
    print("   No new files created")

print("\n➡️ NEXT STEPS:")
print("   1. Check the charts in 'data_overview.png'")
print("   2. Review the crop recommendations")
print("   3. Use the AI model for new predictions")
print("   4. Share your findings!")

print("\n🔁 To run again, type: python3 run_system.py")
print("=" * 50)
