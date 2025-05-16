import tkinter as tk
import json
import os
from tkinter import messagebox

# Charger la configuration depuis `config.json`
CONFIG_FILE = "config.json"
try:
    with open(CONFIG_FILE, "r") as f:
        config = json.load(f)
except FileNotFoundError:
    config = {"langue": "Francais", "theme": "Sombre"}  # Valeurs par défaut

# Définir le logo en fonction de la langue
logo_file = "logo.png" if config["langue"] == "Francais" else "logo2.png"

# Définir les couleurs selon le thème
bg_color = "black" if config.get("theme") == "Sombre" else "white"
fg_color = "orange" if config.get("theme") == "Sombre" else "black"

# Définir les textes selon la langue
TEXTES = {
    "Francais": {  
        "title": "DeadBlock Launcher Alpha",
        "play": "Jouer",
        "options": "Options",
        "update": "Mise à jour",
        "quit": "Quitter",
        "status": "⚠️ Actuellement Inaccessible ⚠️"
    },
    "Anglais": {
        "title": "DeadBlock Launcher Alpha",
        "play": "Play",
        "options": "Settings",
        "update": "Update",
        "quit": "Exit",
        "status": "⚠️ Currently Unavailable ⚠️"
    }
}

# Création de la fenêtre principale
root = tk.Tk()
root.title(TEXTES[config.get("langue", "Francais")]["title"])
root.geometry("600x400")
root.configure(bg=bg_color)

# Ajout du bon logo selon la langue
try:
    logo = tk.PhotoImage(file=logo_file)
    logo_label = tk.Label(root, image=logo, bg=bg_color)
    logo_label.pack(pady=10)
except tk.TclError:
    error_label = tk.Label(root, text="❌ Logo introuvable !", fg="red", bg=bg_color, font=("Courier", 16))
    error_label.pack()

# Message de statut
status_label = tk.Label(root, text=TEXTES[config["langue"]]["status"], fg=fg_color, bg=bg_color, font=("Courier", 16))
status_label.pack(pady=5)

# Fonction pour afficher un popup "Actuellement en construction"
def show_popup():
    messagebox.showwarning(TEXTES[config["langue"]]["title"], TEXTES[config["langue"]]["status"])

# Fonction pour lancer Play.py
def launch_game():
    try:
        os.system("python Play.py")  # Exécuter Play.py
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible de lancer le jeu : {e}")


# Fonction pour lancer config.py
def open_config():
    os.system("python config.py")  # Assure-toi que config.py existe

# Création des boutons avec style Minecraft
button_style = {"fg": "black", "bg": "orange", "font": ("Courier", 14), "width": 15, "height": 2}

play_button = tk.Button(root, text="Jouer", **button_style, command=launch_game)
update_button = tk.Button(root, text=TEXTES[config["langue"]]["update"], **button_style, command=show_popup)
options_button = tk.Button(root, text=TEXTES[config["langue"]]["options"], **button_style, command=open_config)
quit_button = tk.Button(root, text=TEXTES[config["langue"]]["quit"], **button_style, command=root.quit)

# Placement des boutons
play_button.pack(pady=5)
update_button.pack(pady=5)
options_button.pack(pady=5)
quit_button.pack(pady=5)

root.iconbitmap("deadblock.ico")  # Remplace "deadblock.ico" par ton fichier

# Lancement de la fenêtre
root.mainloop()
