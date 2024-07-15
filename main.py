# initialisation tkinter
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Système de gestion d'étudiants")
root.geometry("1200x780")

# fonctions CRUD en relation avec les boutons
# définir avant appel

def add_student():
    print("Ajout")

def view_students():
    print("Consulation")

def update_student():
    print("Mise à jour")

def delete_student():
    print("Suppression")

# Ajout des éléments de saisie et étiquettes

tk.Label(root, text="Nom:").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Âge:").grid(row=1, column=0, padx=10, pady=10)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Classe:").grid(row=2, column=0, padx=10, pady=10)
class_entry = tk.Entry(root)
class_entry.grid(row=2, column=1, padx=10, pady=10)

# ajout des boutons

add_button = tk.Button(root, text="Ajouter", command=add_student)
add_button.grid(row=3, column=0, padx=10, pady=10)

view_button = tk.Button(root, text="Voir", command=view_students)
view_button.grid(row=3, column=1, padx=10, pady=10)

update_button = tk.Button(root, text="Modifier", command=update_student)
update_button.grid(row=3, column=2, padx=10, pady=10)

delete_button = tk.Button(root, text="Supprimer", command=delete_student)
delete_button.grid(row=3, column=3, padx=10, pady=10)


# exécution de la boucle principale
root.mainloop()