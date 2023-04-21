import os

if __name__ == '__main__':
    print("Welcome to my Robo Speaker")
    while True:
        txt=input("Enter what you want me to speak\n")
        if(txt=="q"):
            os.system(f"Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('Thank you,Have a nice day')")
            break
        command= f"Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{txt}')"
        os.system(command)
