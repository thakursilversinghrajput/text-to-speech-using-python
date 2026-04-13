import pyttsx3
from pathlib import Path

print("=== TTS TOOL STARTED ===")

SCRIPT_FILE = Path("script.txt")
OUTPUT_FILE = Path("output_audio.wav")

engine = pyttsx3.init()

# 🔊 NORMAL HUMAN-LIKE SPEED
engine.setProperty("rate", 80)

voices = engine.getProperty("voices")

print("\nAvailable Voices:")
for i, v in enumerate(voices[:3]):
    print(f"{i+1}: {v.name}")

choice = input("\nVoice choose karo (1/2/3): ")

try:
    index = int(choice) - 1
    engine.setProperty("voice", voices[index].id)
except:
    print("Galat choice, default voice use ho rahi hai")

if not SCRIPT_FILE.exists():
    print("❌ script.txt file nahi mili")
    exit()

text = SCRIPT_FILE.read_text(encoding="utf-8").strip()

if not text:
    print("❌ script.txt khali hai")
    exit()

print("\nAudio generate ho raha hai...")
engine.save_to_file(text, str(OUTPUT_FILE))
engine.runAndWait()

print("\n✅ DONE: output_audio.wav ban gayi (NORMAL SPEED)")
