import getpass
#import enchant


#DICO = enchant.Dict("fr_FR")
DICO_PATH = "dictionary.txt"
PASSWD = getpass.getpass('Votre mot de passe: ')
SPECIAL_CARACT = "!@#$%^&*()_+-=[]{}|;:,.<>?"

with open(DICO_PATH, "r", encoding="utf-8") as f:
    DICO = set(ligne.strip().lower() for ligne in f if ligne.strip())


def check_len(password):
    if len(password) < 12:
        return False
    else:
        return True

def check_chiffre(password):
    for caract in password:
        if caract.isdigit():
            return True
    return False

def check_maj(password):
    for caract in password:
        if caract.isupper():
            return True
    return False

def check_minus(password):
    for caract in password:
        if caract.islower():
            return True
    return False

def check_special(password):
    for caract in password:
        if caract in SPECIAL_CARACT:
            return True
    return False

def check_dico(password):
    for mot in DICO:
        if len(mot) < 3:
            continue
        if mot in password.lower():
            return False, mot
    return True

def main_check(password):
    print("\n ---Conseils---")
    score = 0
    if check_chiffre(password):
        score += 20
    else:
        print("Vous devriez mettre des chiffres dans votre mot de passe")

    if check_len(password):
        score += 40
    else:
        print("Votre mot de passe est trop court")

    if check_minus(password):
        score += 10
    else:
        print("Vous devriez mettre des lettre minuscule")

    if check_special(password):
        score += 20
    else:
        print("Vous devriez mettre des caractères spéciaux")

    if check_maj(password):
        score += 10
    else:
        print("Vous devriez mettre des majuscules")

    if not check_dico(password):
        score -= 50
        print("Vous devirez pas mettre de mot du dictionnaire dans votre mot de passe")

    print("---Fin Conseils--- \n")

    return f"Le score de votre mot de passe est de {score}%"


if len(PASSWD) == 0:
    quit()

print(main_check(PASSWD))
