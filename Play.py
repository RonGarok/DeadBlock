import tkinter as tk
import json
import os
import time
from tkinter import messagebox

# Trouver le dossier utilisateur automatiquement
USER_FOLDER = os.path.expanduser("~")  # Cette ligne doit être placée AVANT d'utiliser USER_FOLDER

# Chemins des launchers (adapté à chaque utilisateur)
MINECRAFT_PATH = os.path.join(USER_FOLDER, "AppData", "Roaming", ".minecraft", "launcher.exe")
TLAUNCHER_PATH = os.path.join(USER_FOLDER, "AppData", "Roaming", ".minecraft", "TLauncher.exe")


# Adresse du serveur
SERVER_IP = "play.deadblock.com"

# **Étape 1 : Demander le choix du launcher AVANT les vérifications**
launcher_choice = messagebox.askquestion("Choix du Launcher", "Voulez-vous jouer avec TLauncher ? (Oui = TLauncher, Non = Minecraft Launcher)")

# **Étape 2 : Vérifier le launcher sélectionné**
if launcher_choice == "yes":
    launcher_to_use = TLAUNCHER_PATH
else:
    launcher_to_use = MINECRAFT_PATH

# **Étape 3 : Vérifier que le launcher sélectionné est installé**
if not os.path.exists(launcher_to_use):
    messagebox.showerror("Erreur", f"❌ {launcher_to_use} introuvable ! Installez-le avant de continuer.")
    exit()

# Création de l'interface de chargement
root = tk.Tk()
root.title("Chargement du jeu...")
root.geometry("400x250")
root.configure(bg="black")

progress_label = tk.Label(root, text="Préparation du lancement...", fg="orange", bg="black", font=("Courier", 14))
progress_label.pack(pady=10)

progress_bar = tk.Canvas(root, width=300, height=20, bg="gray")
bar_fill = progress_bar.create_rectangle(0, 0, 0, 20, fill="orange")
progress_bar.pack()

root.update()

# Fonction de mise à jour de la barre de chargement
def update_progress(step, text):
    progress_label.config(text=text)
    progress_bar.coords(bar_fill, 0, 0, step * 60, 20)
    root.update()
    time.sleep(5)  # Pause de 5 secondes par étape

# **Étape 4 : Vérification des fichiers Minecraft**
update_progress(1, "✔️ Vérification des fichiers Minecraft...")

MINECRAFT_FOLDER = os.path.expanduser("~\\AppData\\Roaming\\.minecraft")
if not os.path.exists(MINECRAFT_FOLDER):
    messagebox.showerror("Erreur", "❌ Minecraft n'est pas installé !")
    root.destroy()
    exit()

# **Étape 5 : Chargement des objets du joueur**
ITEMS_FILE = "player_items.json"
if os.path.exists(ITEMS_FILE):
    with open(ITEMS_FILE, "r") as f:
        items = json.load(f)
    update_progress(2, "✔️ Chargement des objets du joueur...")
else:
    update_progress(2, "⚠️ Aucun objet personnalisé trouvé.")

# **Étape 6 : Vérification de la connexion au serveur**
response = os.system(f"ping -n 1 {SERVER_IP}")
if response != 0:
    messagebox.showerror("Erreur", "❌ Serveur injoignable. Vérifiez votre connexion !")
    root.destroy()
    exit()

update_progress(3, "✔️ Connexion au serveur...")

# **Étape 7 : Lancement du jeu avec le launcher sélectionné**
update_progress(4, "✔️ Démarrage du jeu...")
root.destroy()
os.system(f'"{launcher_to_use}" --server {SERVER_IP} --port 25565')
