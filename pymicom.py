#!/usr/bin/env python
# -*- coding:utf-8 -*-

""" -------------------------------------------------------
	Wrapper python pour interface avec AppMiCom_2025.exe
	Midi Ingenierie (NS) 2025
    Hensoldt Mechatronic Solutions
	noe.serres@hensoldt.fr
    
    version 1: juillet 2025. version initiale avec polling du clipboard.
    version 2: juillet 2025. polling du clipboard remplacé par attente fin d'exécution (plus simple)
	-------------------------------------------------------
""" 
__author__ = "noe.serres@hensoldt.fr"
__version__ = "2.0"

import subprocess
from time import sleep
import pyperclip # installer le module https://pypi.org/project/pyperclip/
import os

# --- Configuration fixe ---
APP_FILE = "AppMiCom_2025.exe" # chemin complet sauf si exécution dans le même répertoire
COMPORT = "COM54"   # voir gestionnaire de peripheriques
TYPE = "MAC23"      # MAC23, MAC34, BMAC, DMAC, MIBL, MIP0505
BAUDRATE = "38400"  # 9600, 19200, 38400, 57600, 115200

# --- Exemple d’utilisation ---
if __name__ == "__main__":
    
    # Vérifier la présence de l'exécutable
    if not os.path.isfile(APP_FILE):
        raise FileNotFoundError(f"[ERROR] Exécutable introuvable: {APP_FILE}")

    #Relecture de la chaine d'identifiant
    try:
        subprocess.run([APP_FILE,TYPE,COMPORT,BAUDRATE,"00qv"], shell=True)
        print(pyperclip.paste())
    except Exception as e:
        print(f"[ERROR] {e}")

    #Commande de mouvement
    try:
        subprocess.run([APP_FILE,TYPE,COMPORT,BAUDRATE,"00gf 4000"], shell=True)
        print(pyperclip.paste())
    except Exception as e:
        print(f"[ERROR] {e}")
    
    #Attente 3 secondes
    sleep(3)
    
    #commande d'arrêt
    try:
        subprocess.run([APP_FILE,TYPE,COMPORT,BAUDRATE,"00ge"], shell=True)
        print(pyperclip.paste())
    except Exception as e:
        print(f"[ERROR] {e}")
    
