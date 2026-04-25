# PasswordAnalyser

PasswordAnalyser est un programme qui permet de vérifier si un mot de passe est robuste, il crée aussi des mot de passe parfait.

Pour crée un exe: 

    
    pip install pyinstaller
    pyinstaller --noconfirm --onefile --windowed --add-data "dictionary.txt:." --collect-all customtkinter main.py