import getpass

DICO_PATH = "dictionary.txt"
PASSWD = getpass.getpass('Votre mot de passe: ')
SPECIAL_CARACT = "!@#$%^&*()_+-=[]{}|;:,.<>?"

with open(DICO_PATH, "r", encoding="utf-8") as f:
    DICO = set(ligne.strip().lower() for ligne in f if ligne.strip())


def check_len(password):
    """
    Vérifie si la taille du mot de passe est supérieur à 12 caracteres
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
    for caract in password:
        if caract.isdigit():
            return True

    return False

def check_maj(password):
    """
    Vérifie que le mot de passe contient une majuscule
    :param password:
    :return bool:
    """
    for caract in password:
        if caract.isupper():
            return True

    return False

def check_minus(password):
    """
    Vérifie que le mot de passe contient une minuscule
    :param password:
    :return bool:
    """
    for caract in password:
        if caract.islower():
            return True

    return False

def check_special(password):
    """
    Vérifie que le mot de passe contient au moins un caractère spécial
    :param password:
    :return bool:
    """
    for caract in password:
        if caract in SPECIAL_CARACT:
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
    Vérifie que le mot de passe contient ne contient pas de liste suite
    :param password:
    :return bool:
    """
    for i in range(len(password) - 2):
        char1 = ord(password[i])
        char2 = ord(password[i + 1])
        char3 = ord(password[i + 2])

        if char2 == char1 + 1 and char3 == char2 + 1:
            return False

    return True

def main_check(password):
    """
    Applique tous les checks au mot de passe pour lui attribuer un score
    :param password:
    :return str:
    """
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

    if not check_suite(password):
        score -= 50
        print("Votre mot de passe contient une suite")

    print("---Fin Conseils--- \n")

    print(f"Votre score de mot de passe est de {max(0, score)}%")

    return score


if __name__ == "__main__":
    if len(PASSWD) == 0:
        print("Rentrer un mot de passe")
        quit()
    main_check(PASSWD)