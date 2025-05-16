import tkinter as tk
import json
import os

CONFIG_FILE = "config.json"

# Vérifier si `config.json` existe, sinon créer une config par défaut
if not os.path.exists(CONFIG_FILE):
    default_config = {
        "langue": "Francais",
        "theme": "Sombre",
        "resolution": "1920x1080",
        "graphismes": "Élevés"
    }
    with open(CONFIG_FILE, "w") as f:
        json.dump(default_config, f, indent=4)

# Fonction pour sauvegarder la configuration
def save_config():
    config = {
        "resolution": resolution_var.get(),
        "langue": langue_var.get(),
        "graphismes": graphismes_var.get(),
        "theme": theme_var.get()
    }

    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

    status_label.config(text="✅ Configuration enregistrée !", fg="green")

    # Fermer la fenêtre de configuration
    root.destroy()

    # Fermer l'ancien launcher et ouvrir le nouveau avec les nouvelles configs
    os.system("python Launcher.py")  # Relance avec la nouvelle configuration
    os.system("taskkill /f /im python.exe")  # Ferme l'ancien launcher
    

# Interface Tkinter
root = tk.Tk()
root.title("Paramètres du Launcher")
root.geometry("400x350")

# Variables des options
resolution_var = tk.StringVar(value="1920x1080")
langue_var = tk.StringVar(value="Francais")
graphismes_var = tk.StringVar(value="Élevés")
theme_var = tk.StringVar(value="Sombre")

# Labels et menus déroulants
tk.Label(root, text="Résolution :", font=("Courier", 14)).pack()
tk.OptionMenu(root, resolution_var, "1920x1080", "1280x720", "800x600").pack()

tk.Label(root, text="Langue :", font=("Courier", 14)).pack()
tk.OptionMenu(root, langue_var, "Francais", "Anglais").pack()

tk.Label(root, text="Graphismes :", font=("Courier", 14)).pack()
tk.OptionMenu(root, graphismes_var, "Élevés", "Moyens", "Bas").pack()

tk.Label(root, text="Thème :", font=("Courier", 14)).pack()
tk.OptionMenu(root, theme_var, "Sombre", "Clair").pack()

# Bouton de sauvegarde + redémarrage du launcher
save_button = tk.Button(root, text="Enregistrer", font=("Courier", 14), command=save_config)
save_button.pack(pady=10)

status_label = tk.Label(root, text="", font=("Courier", 12))
status_label.pack()

root.iconbitmap("deadblock.ico")  # Remplace "deadblock.ico" par ton fichier

# Lancement de l'interface
root.mainloop()
