import os
import urllib.request

DICO_PATH = "dictionary.txt"
if not os.path.exists(DICO_PATH):
    print("Téléchargement du dictionnaire...")
    url = "https://raw.githubusercontent.com/chrplr/openlexicon/master/datasets-info/Liste-de-mots-francais-Gutenberg/liste.de.mots.francais.frgut.txt"
    urllib.request.urlretrieve(url, DICO_PATH)
    print("Téléchargement terminé.")

with open(DICO_PATH, "r", encoding="utf-8") as f:
    DICO = set(ligne.strip().lower() for ligne in f if ligne.strip())

print(f"{len(DICO)} mots chargés")