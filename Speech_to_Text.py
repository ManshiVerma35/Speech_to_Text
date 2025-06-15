import speech_recognition as sr
import datetime
import os

recognizer = sr.Recognizer()

# Save text with timestamp
def save_text(text, filename="Transcription.txt", mode="a"):
    with open(filename, mode, encoding="utf-8") as file:
        file.write(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]:\n{text}\n\n")
    print(f"📁 Saved to {filename}")

# Record and transcribe speech (with longer timeout)
def record_and_transcribe():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("\n🎤 Recording... You have up to 60 seconds to speak.")
        try:
            audio = recognizer.listen(source, timeout=60)
            print("🔍 Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"\n✅ Transcribed Text:\n{text}")
            return text
        except sr.WaitTimeoutError:
            print("⏳ Timeout: No speech detected within 60 seconds.")
        except sr.UnknownValueError:
            print("❌ Could not understand the speech.")
        except sr.RequestError:
            print("🔌 Network error with Google API.")
    return None

# Main interactive loop
def main():
    print("🧠 AI Speech-to-Text Converter")
    print("=============================")
    filename = input("Enter filename to save (default: Transcription.txt): ").strip()
    if filename == "":
        filename = "Transcription.txt"

    mode = "a"
    if os.path.exists(filename):
        choice = input(f"File '{filename}' exists. (A)ppend or (O)verwrite? ").lower()
        mode = "a" if choice == "a" else "w"

    while True:
        start = input("\nPress [Enter] to start recording or type 'exit' to quit: ").lower()
        if start == "exit":
            print("👋 Exiting the program.")
            break

        text = record_and_transcribe()
        if text:
            save_text(text, filename, mode)

        again = input("\n🔁 Do you want to record another entry? (y/n): ").lower()
        if again != "y":
            print("✅ Session completed. All recordings saved.")
            break

# Run the program
if __name__ == "__main__":
    main()

