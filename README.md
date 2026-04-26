# PasswordAnalyser

PasswordAnalyser est un programme qui permet de vérifier si un mot de passe est robuste, il crée aussi des mots de passe parfait en fonction des conseils de l'ANSSI.  
Il permet de vérifier si le mot de passe contient bien une majuscule, une minuscule, un chiffre, un caractère spécial.  
Il vérifie si le mot de passe ne contient pas de mot de la langue française ainsi que de suite logique.


Pour crée un exe: 

    
    pip install pyinstaller
    pyinstaller --noconfirm --onefile --windowed --add-data "dictionary.txt:." --collect-all customtkinter main.py

packet nécessaire:
    
    xclip





CREDIT: https://github.com/tarraschk/richelieu pour les mots de passe français courant