# CROP HEALTH ANALYZER
# Analyzes conditions and gives recommendations

import pandas as pd
import numpy as np
import joblib

print("=== CROP HEALTH ANALYZER ===")

class SimpleCropAdvisor:
    def __init__(self):
        self.crop_guides = {
            'Tomatoes': {
                'ideal_temp': (18, 24),
                'ideal_humidity': (60, 70),
                'ideal_moisture': (1200, 1400),
                'tips': [
                    "Keep soil consistently moist",
                    "Provide plenty of sunlight",
                    "Watch for yellow leaves"
                ]
            },
            'Lettuce': {
                'ideal_temp': (15, 20),
                'ideal_humidity': (70, 80),
                'ideal_moisture': (1300, 1500),
                'tips': [
                    "Keep soil moist but not waterlogged",
                    "Prefers cooler temperatures",
                    "Harvest outer leaves first"
                ]
            },
            'Potatoes': {
                'ideal_temp': (15, 20),
                'ideal_humidity': (50, 70),
                'ideal_moisture': (1100, 1300),
                'tips': [
                    "Water deeply but infrequently",
                    "Hill soil around plants",
                    "Harvest after flowers appear"
                ]
            },
            'General': {
                'ideal_temp': (15, 25),
                'ideal_humidity': (50, 80),
                'ideal_moisture': (1000, 1500),
                'tips': [
                    "Monitor soil moisture regularly",
                    "Watch for pest damage",
                    "Rotate crops yearly"
                ]
            }
        }
    
    def analyze_conditions(self, temp, humidity, moisture, crop_type='General'):
        print(f"\n🌱 Analyzing conditions for {crop_type}...")
        
        if crop_type not in self.crop_guides:
            crop_type = 'General'
        
        guide = self.crop_guides[crop_type]
        issues = []
        recommendations = []
        
        # Temperature analysis
        if temp < guide['ideal_temp'][0]:
            issues.append(f"❄️ Too cold ({temp}°C)")
            recommendations.append("→ Consider using a greenhouse or row covers")
        elif temp > guide['ideal_temp'][1]:
            issues.append(f"🔥 Too hot ({temp}°C)")
            recommendations.append("→ Provide shade during hottest hours")
        else:
            recommendations.append("✅ Temperature is perfect!")
        
        # Humidity analysis
        if humidity < guide['ideal_humidity'][0]:
            issues.append(f"🏜️ Low humidity ({humidity}%)")
            recommendations.append("→ Increase watering frequency")
        elif humidity > guide['ideal_humidity'][1]:
            issues.append(f"💧 High humidity ({humidity}%)")
            recommendations.append("→ Improve air circulation")
        else:
            recommendations.append("✅ Humidity is perfect!")
        
        # Moisture analysis
        if moisture < guide['ideal_moisture'][0]:
            issues.append(f"🏜️ Dry soil (moisture: {moisture})")
            recommendations.append("→ Water plants immediately")
        elif moisture > guide['ideal_moisture'][1]:
            issues.append(f"🌊 Waterlogged soil (moisture: {moisture})")
            recommendations.append("→ Reduce watering and improve drainage")
        else:
            recommendations.append("✅ Soil moisture is perfect!")
        
        return issues, recommendations, guide['tips']
    
    def suggest_best_crops(self, temp, humidity):
        print("\n🌾 CROP SUGGESTIONS for your conditions:")
        
        scores = {}
        for crop, guide in self.crop_guides.items():
            if crop == 'General':
                continue
                
            score = 0
            # Temperature score
            if guide['ideal_temp'][0] <= temp <= guide['ideal_temp'][1]:
                score += 2
            elif abs(temp - np.mean(guide['ideal_temp'])) <= 5:
                score += 1
            
            # Humidity score
            if guide['ideal_humidity'][0] <= humidity <= guide['ideal_humidity'][1]:
                score += 1
            
            scores[crop] = score
        
        # Sort by score
        sorted_crops = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        
        for crop, score in sorted_crops:
            stars = "★" * score + "☆" * (3 - score)
            print(f"  {stars} {crop} (score: {score}/3)")

# Load data for analysis
try:
    df = pd.read_csv('crop_data.csv')
    print("✅ Data loaded successfully!")
    
    # Use the most recent data point
    latest = df.iloc[-1]
    
    # Extract values (with error handling)
    temp = latest.get('Soil Temperature (°C)', 20)
    humidity = latest.get('Humidity (%)', 60)
    moisture = latest.get('Moisture', 1200)
    
    print(f"\n📊 CURRENT CONDITIONS:")
    print(f"   Soil Temperature: {temp}°C")
    print(f"   Humidity: {humidity}%")
    print(f"   Moisture: {moisture}")
    
except Exception as e:
    print("⚠️ Using sample data for demonstration")
    temp = 20
    humidity = 65
    moisture = 1250

# Analyze conditions
advisor = SimpleCropAdvisor()

# Get crop suggestions
advisor.suggest_best_crops(temp, humidity)

# Analyze for specific crops
crops_to_analyze = ['Tomatoes', 'Lettuce', 'Potatoes']

for crop in crops_to_analyze:
    issues, recommendations, tips = advisor.analyze_conditions(temp, humidity, moisture, crop)
    
    if issues:
        print(f"\n⚠️ ISSUES for {crop}:")
        for issue in issues:
            print(f"   {issue}")
    else:
        print(f"\n✅ {crop} conditions are EXCELLENT!")
    
    print(f"💡 RECOMMENDATIONS for {crop}:")
    for rec in recommendations:
        print(f"   {rec}")
    
    print(f"🌱 GROWING TIPS for {crop}:")
    for tip in tips[:2]:  # Show first 2 tips
        print(f"   {tip}")

print("\n" + "="*50)
print("HEALTH ANALYSIS COMPLETE!")
print("Use these recommendations to improve your crops!")
print("="*50)
