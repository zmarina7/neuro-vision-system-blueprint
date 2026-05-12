import random
import time

class NeuroVisionAI:
    def __init__(self):
        self.objects = {
            "Moving Vehicle": {"weight": 10, "color": "RED"},
            "Pedestrian": {"weight": 8, "color": "YELLOW"},
            "Stairs (Down)": {"weight": 9, "color": "RED"},
            "Traffic Light": {"weight": 0, "color": "INFO"},
            "Static Wall": {"weight": 2, "color": "GREEN"}
        }

    def scan(self):
        obj = random.choice(list(self.objects.keys()))
        dist = round(random.uniform(0.3, 7.0), 2)
        return obj, dist

class TacticalEngine:
    def check_signal(self, obj):
        if obj == "Traffic Light":
            return random.choice(["STOP (Red)", "GO (Green)", "CAUTION (Yellow)"])
        return None

    def get_stealth_freq(self, mode="Stealth"):
        return "1550nm (Invisible/Eye-Safe)" if mode == "Stealth" else "905nm (Standard)"

def run_simulation():
    ai = NeuroVisionAI()
    tac = TacticalEngine()
    
    print("="*40)
    print("NEURO-VISION SYSTEM BOOTING...")
    print(f"SENSOR FREQUENCY: {tac.get_stealth_freq()}")
    print("="*40 + "\n")

    for i in range(1, 6):
        obj, dist = ai.scan()
        signal_status = tac.check_signal(obj)
        
        # Calculate Threat Vector
        weight = ai.objects[obj]["weight"]
        threat_vector = round(weight / (max(dist, 0.1)**2), 2)

        print(f"[SCAN {i}] DETECTED: {obj} at {dist}m")
        
        if signal_status:
            print(f" 🚦 SIGNAL ANALYSIS: {signal_status}")
        
        if threat_vector > 15:
            print(f" 🚨 ACTION: Immediate Haptic Pulse (STOP!) [Priority: {threat_vector}]")
        elif threat_vector > 5:
            print(f" ⚠️ ACTION: Gentle Nudge Left/Right [Priority: {threat_vector}]")
        else:
            print(f" ✅ ACTION: Path Clear. Neural Mapping active.")
        
        print("-" * 30)
        time.sleep(1.5)

if __name__ == "__main__":
    run_simulation()
