import time
from monitor.keyboard_monitor import get_typing_speed
from monitor.sensors import get_light, get_audio
from backend.predictor import predict
from backend.database import insert_record
from plyer import notification

print("System Started... Monitoring in background")

while True:
    try:
        # ==========================================
        # GET RAW SENSOR VALUES
        # ==========================================
        light = get_light()
        audio = get_audio()
        typing = get_typing_speed()

        # ==========================================
        # DEBUG RAW VALUES
        # ==========================================
        print(f"\nRAW VALUES → Light: {light:.2f}, Audio: {audio:.2f}, Typing: {typing:.2f}")

        # ==========================================
        # CONVERT TO FEATURES (CALIBRATED)
        # ==========================================
        # Adjusted thresholds (IMPORTANT FIX)
        photophobia = 1 if light > 120 else 0
        phonophobia = 1 if audio > 20 else 0

        # Debug mapped values
        print(f"MAPPED → Photophobia: {photophobia}, Phonophobia: {phonophobia}")

        # ==========================================
        # PREDICTION
        # ==========================================
        result = predict(photophobia, phonophobia, typing)

        print(f"RESULT → {result}")

        # ==========================================
        # SAVE TO DATABASE
        # ==========================================
        insert_record(photophobia, phonophobia, typing, result)

        # ==========================================
        # ALERT SYSTEM
        # ==========================================
        if result == "HIGH RISK":
            notification.notify(
                title="⚠ Migraine Alert",
                message="High Migraine Risk Detected! Take precautions.",
                timeout=5
            )

        # ==========================================
        # LOOP DELAY
        # ==========================================
        time.sleep(10)

    except Exception as e:
        print("Error:", e)
        time.sleep(5)