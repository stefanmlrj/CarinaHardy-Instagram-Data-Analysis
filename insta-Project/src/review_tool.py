import argparse
import sys
from pathlib import Path
import pandas as pd

# Add the src directory to the path so we can import modules
sys.path.append(str(Path(__file__).parent))

from design_aesthetics import extract_palette_features

class ImageReviewer:
    def __init__(self):
        # Thresholds derived from README.md insights
        # "Contrast (std_value) was the most influential... posts with stronger light–dark variation tended to draw more attention"
        # "Warmth (warm_ratio) followed closely... images with warmer tones generally perform better"
        # "Color intensity (avg_saturation)... vibrant, saturated images seem to perform slightly better"
        
        # Note: These are heuristic baselines. In a real scenario, we'd calibrate these against the high-performing cluster stats.
        self.thresholds = {
            "std_value": 0.2,       # Minimum contrast
            "warm_ratio": 0.3,      # Minimum warmth
            "avg_saturation": 0.2,  # Minimum saturation
            "avg_value_min": 0.3,   # Minimum brightness
            "avg_value_max": 0.8    # Maximum brightness (avoid overexposure)
        }

    def analyze_image(self, image_path: Path):
        print(f"Analyzing image: {image_path}...")
        features = extract_palette_features(image_path)
        
        if features is None:
            print("Error: Could not extract features from the image.")
            return None
            
        return features

    def generate_feedback(self, features):
        feedback = []
        score = 0
        max_score = 4 # Based on 4 main metrics
        
        # 1. Contrast Analysis
        contrast = features['std_value']
        if contrast >= self.thresholds['std_value']:
            score += 1
            feedback.append(f"✅ Good contrast ({contrast:.2f}). The image has good depth.")
        else:
            feedback.append(f"⚠️ Low contrast ({contrast:.2f}). Consider increasing contrast to make the image pop.")

        # 2. Warmth Analysis
        warmth = features['warm_ratio']
        if warmth >= self.thresholds['warm_ratio']:
            score += 1
            feedback.append(f"✅ Good warmth ({warmth:.2f}). Warm tones are engaging.")
        else:
            feedback.append(f"⚠️ Low warmth ({warmth:.2f}). Consider adding warmer tones (yellows, reds) to increase engagement.")

        # 3. Saturation Analysis
        saturation = features['avg_saturation']
        if saturation >= self.thresholds['avg_saturation']:
            score += 1
            feedback.append(f"✅ Good saturation ({saturation:.2f}). Vibrant colors attract attention.")
        else:
            feedback.append(f"⚠️ Low saturation ({saturation:.2f}). Consider boosting color intensity slightly.")

        # 4. Brightness Analysis
        brightness = features['avg_value']
        if self.thresholds['avg_value_min'] <= brightness <= self.thresholds['avg_value_max']:
            score += 1
            feedback.append(f"✅ Good brightness ({brightness:.2f}). The image is well-lit.")
        else:
            if brightness < self.thresholds['avg_value_min']:
                feedback.append(f"⚠️ Too dark ({brightness:.2f}). Consider brightening the image.")
            else:
                feedback.append(f"⚠️ Too bright ({brightness:.2f}). Watch out for overexposure.")

        return score, max_score, feedback

    def print_report(self, features, score, max_score, feedback):
        print("\n" + "="*40)
        print("📸 INSTAGRAM IMAGE REVIEW REPORT")
        print("="*40)
        
        print("\n📊 Extracted Features:")
        print(f"  - Contrast (std_value):   {features['std_value']:.3f}")
        print(f"  - Warmth (warm_ratio):    {features['warm_ratio']:.3f}")
        print(f"  - Saturation (avg_sat):   {features['avg_saturation']:.3f}")
        print(f"  - Brightness (avg_val):   {features['avg_value']:.3f}")
        
        print("\n📝 Feedback:")
        for item in feedback:
            print(f"  {item}")
            
        final_score_pct = (score / max_score) * 100
        print("\n" + "-"*40)
        print(f"🏆 FINAL SCORE: {score}/{max_score} ({final_score_pct:.0f}%)")
        print("="*40 + "\n")

def main():
    parser = argparse.ArgumentParser(description="Review an image for Instagram posting suitability.")
    parser.add_argument("image_path", type=str, help="Path to the image file")
    args = parser.parse_args()
    
    image_path = Path(args.image_path)
    
    if not image_path.exists():
        print(f"Error: File not found at {image_path}")
        return

    reviewer = ImageReviewer()
    features = reviewer.analyze_image(image_path)
    
    if features:
        score, max_score, feedback = reviewer.generate_feedback(features)
        reviewer.print_report(features, score, max_score, feedback)

if __name__ == "__main__":
    main()
