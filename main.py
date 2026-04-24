import getpass
import enchant

DICO = enchant.Dict("fr_FR")
PASSWD = getpass.getpass('Votre mot de passe: ')
SPECIAL_CARACT = "!@#$%^&*()_+-=[]{}|;:,.<>?"


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
    pass

def main_check(password):
    print("\n ---Conseils---")
    score = 0
    if check_chiffre(password):
        score += 20
    else:
        print("Vous devriez mettre des chiffres dans votre mot de passe")

    if check_len(password):
        score += 20
    else:
        print("Votre mot de passe est trop court")

    if check_minus(password):
        score += 20
    else:
        print("Vous devriez mettre des lettre minuscule")

    if check_special(password):
        score += 20
    else:
        print("Vous devriez mettre des caractères spéciaux")

    if check_maj(password):
        score += 20
    else:
        print("Vous devriez mettre des majuscules")

    print("---Fin Conseils--- \n")

    return f"Le score de votre mot de passe est de {score}%"

if len(PASSWD) == 0:
    quit()

#print(main_check(PASSWD))

if "" in DICO:
    print("Le mot est dans le dico")