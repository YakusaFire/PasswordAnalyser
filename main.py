import os
import sys
import pyperclip
from math import log2
import customtkinter as ctk
from secrets import choice, SystemRandom
from string import ascii_lowercase, ascii_uppercase, digits



def resource_path(relative_path):
    """ Récupère le chemin absolu des ressources (pour PyInstaller) """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Modifie ta variable DICO_PATH ainsi :
DICO_PATH = resource_path("dictionary.txt")
SPECIAL_CHART = "!@#$%^&*()_+-=[]{}|;:,.<>?"


with open(DICO_PATH, "r", encoding="utf-8") as f:
    DICO = set(ligne.strip().lower() for ligne in f if ligne.strip())


def check_len(password):
    """
    Vérifie si la taille du mot de passe est supérieur à 12 caractères
    :param password:
    :return bool:
    """
    if len(password) < 12:
        return False
    else:
        return True

def check_chiffre(password):
    """
    Vérifie que le mot de passe contient au moins un chiffre
    :param password:
    :return bool:
    """
    for chart in password:
        if chart.isdigit():
            return True

    return False

def check_maj(password):
    """
    Vérifie que le mot de passe contient une majuscule
    :param password:
    :return bool:
    """
    for chart in password:
        if chart.isupper():
            return True

    return False

def check_minus(password):
    """
    Vérifie que le mot de passe contient une minuscule
    :param password:
    :return bool:
    """
    for chart in password:
        if chart.islower():
            return True

    return False

def check_special(password):
    """
    Vérifie que le mot de passe contient au moins un caractère spécial
    :param password:
    :return bool:
    """
    for chart in password:
        if chart in SPECIAL_CHART:
            return True

    return False

def check_dico(password):
    """
    Vérifie que le mot de passe ne contient pas de mot du dictionnaire
    :param password:
    :return score(int):
    """
    for mot in DICO:
        if len(mot) < 3:
            continue
        if mot in password.lower():
            return False

    return True

def check_suite(password):
    """
    Vérifie que le mot de passe contient ne contient pas de liste suite par rapport à leur position dans la table ASCI
    :param password:
    :return bool:
    """
    for i in range(len(password) - 2):
        char1 = ord(password[i])
        char2 = ord(password[i + 1])
        char3 = ord(password[i + 2])

        if (char2 == char1 + 1 and char3 == char2 + 1) or (char2 == char1 - 1 and char3 == char2 - 1):
            return False

    return True

def calcul_entropie(password):
    """
    Permet de calculer la force mathématique de votre mot de passe
    :param password:
    :return float:
    """
    L = len(password)
    R = 90
    entropie = L * log2(R)
    return round(entropie, 2)

def generate_perfect_password(length=16):
    """
    Permet de générer le mot de passe parfait
    :param length:
    :return str:
    """
    minuscules = ascii_lowercase
    majuscules = ascii_uppercase
    chiffres = digits
    speciaux = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    # Met au minimum un caractère de chaque type
    password = [
        choice(minuscules),
        choice(majuscules),
        choice(chiffres),
        choice(speciaux)
    ]

    tous_les_caracteres = minuscules + majuscules + chiffres + speciaux
    for _ in range(length - 4):
        password.append(choice(tous_les_caracteres))


    SystemRandom().shuffle(password)

    return "".join(password)

# Interface graphique
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title = "PasswordAnalyser"
        self.geometry = "500x600"

        #Titre
        self.label = ctk.CTkLabel(self, text="Password Analyser", font=("Roboto", 24, "bold"))
        self.label.pack(pady=20)

        #Mot de passe
        self.entry = ctk.CTkEntry(self, placeholder_text="Entrer le mot de passe", width=350, show="*")
        self.entry.pack(pady=10)
        self.entry.bind("<KeyRelease>", self.update_analysis)

        # Barre de progression du score
        self.progressbar = ctk.CTkProgressBar(self, width=350)
        self.progressbar.set(0)
        self.progressbar.pack(pady=10)

        # Zone de texte pour les conseils
        self.result_text = ctk.CTkTextbox(self, width=350, height=150)
        self.result_text.pack(pady=10)

        # Labels pour l'entropie
        self.entropy_label = ctk.CTkLabel(self, text="Entropie : 0 bits", font=("Roboto", 14))
        self.entropy_label.pack(pady=5)


        # Titre section mot de passe généré
        self.title2_label = ctk.CTkLabel(self, text="Générer mot de passe parfait", font=("Roboto", 24))
        self.title2_label.pack(pady=(20, 10))

        # Zone de texte mot de passe généré
        self.gen_text = ctk.CTkTextbox(self, width=350, height=20)
        self.gen_text.pack(pady=(5, 5))

        # Label taille mot de passe généré
        self.slider_label = ctk.CTkLabel(self, text="Longueur : 16", font=("Roboto", 14))
        self.slider_label.pack(pady=5)

        # Slider mot de passe généré
        self.len_slider = ctk.CTkSlider(self, from_=8, to=32, number_of_steps=24, command=self.update_slider_label)
        self.len_slider.set(16)
        self.len_slider.pack(pady=5)

        # Bouton de génération
        self.gen_button = ctk.CTkButton(self, text="Générer un mot de passe parfait", command=self.fill_generated)
        self.gen_button.pack(pady=5)

        # Bouton copier mot de passe
        self.copy_button = ctk.CTkButton(self, text="Copier mot de passe parfait", command=self.copy_mdp)
        self.copy_button.pack(pady=5)

    def update_slider_label(self, valeur):
        """
        Met à jour le label qui affiche la longueur du slider
        """
        self.slider_label.configure(text=f"Longueur : {int(valeur)}")

    def copy_mdp(self):
        """
        Permet de copier ce que contient la TextBox dans le clipboard
        """
        password = self.gen_text.get(1.0, "end-1c")
        pyperclip.copy(password)
        self.gen_text.delete("1.0", "end")
        self.gen_text.insert("1.0", "✅ Mot de passe copié !")

    def update_analysis(self, event=None):
        """
        Permet de mettre à jour l'analyse du mot de passe en continu
        """
        password = self.entry.get()
        if not password:
            self.progressbar.set(0)
            return

        score = 0
        feedback = []

        # Application des tests
        if check_chiffre(password):
            score += 20
        else:
            feedback.append("- Ajoutez des chiffres")

        if check_len(password):
            score += 40
        else:
            feedback.append("- Trop court (12 min)")

        if check_minus(password):
            score += 10
        else:
            feedback.append("- Manque minuscules")

        if check_maj(password):
            score += 10
        else:
            feedback.append("- Manque majuscules")

        if check_special(password):
            score += 20
        else:
            feedback.append("- Manque caractères spéciaux")

        if not check_dico(password):
            score -= 50
            feedback.append("MOT DU DICTIONNAIRE DÉTECTÉ")

        if not check_suite(password):
            score -= 50
            feedback.append("SUITE LOGIQUE DÉTECTÉE")

        actual_score = max(0, score)

        # Mise à jour de l'UI
        self.progressbar.set(actual_score / 100)

        # Couleur de la barre selon le score
        if actual_score < 50:
            self.progressbar.configure(progress_color="red")
        elif actual_score < 90:
            self.progressbar.configure(progress_color="orange")
        else:
            self.progressbar.configure(progress_color="green")

        self.entropy_label.configure(text=f"Entropie : {calcul_entropie(password)} bits")

        self.result_text.delete("1.0", "end")
        if not feedback:
            self.result_text.insert("1.0", "Mot de passe excellent !")
        else:
            self.result_text.insert("1.0", "\n".join(feedback))

    def fill_generated(self):
        """
        Permet de générer un mot de passe parfait
        """
        new_pass = generate_perfect_password(int(self.len_slider.get()))
        self.gen_text.delete(1.0, "end")
        self.gen_text.insert(1.0, new_pass)

if __name__ == "__main__":
     app = App()
     app.mainloop()
