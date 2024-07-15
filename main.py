# initialisation tkinter
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Système de gestion d'étudiants")
root.geometry("1200x780")

# fonctions CRUD en relation avec les boutons
# définir avant appel

students = []

def add_student():
    # print("Ajout")
    name = name_entry.get()
    age = age_entry.get()
    student_class = class_entry.get()
    if name and age and student_class:
        students.append({"name": name, "age": age, "class": student_class})
        messagebox.showinfo("Succès", "Étudiant ajouté avec succès")
        clear_entries()
    else:
        messagebox.showerror("Erreur", "Tous les champs sont obligatoires")


def view_students():
    # print("Consulation")
    view_window = tk.Toplevel(root)
    view_window.title("Liste des Étudiants")
    for i, student in enumerate(students):
        tk.Label(view_window, text=f"{student['name']} - {student['age']} - {student['class']}").grid(row=i, column=0)

def update_student():
    # print("Mise à jour")
    name = name_entry.get()
    age = age_entry.get()
    student_class = class_entry.get()
    for student in students:
        if student['name'] == name:
            student['age'] = age
            student['class'] = student_class
            messagebox.showinfo("Succès", "Étudiant mis à jour avec succès")
            clear_entries()
            return
    messagebox.showerror("Erreur", "Étudiant non trouvé")

def delete_student():
    # print("Suppression")
    name = name_entry.get()
    for student in students:
        if student['name'] == name:
            students.remove(student)
            messagebox.showinfo("Succès", "Étudiant supprimé avec succès")
            clear_entries()
            return
    messagebox.showerror("Erreur", "Étudiant non trouvé")

def clear_entries():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    class_entry.delete(0, tk.END)

# Ajout des éléments de saisie et étiquettes

tk.Label(root, text="Nom:").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root,  width=100)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Âge:").grid(row=1, column=0, padx=10, pady=10)
age_entry = tk.Entry(root, width=100)
age_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Classe:").grid(row=2, column=0, padx=10, pady=10)
class_entry = tk.Entry(root, width=100)
class_entry.grid(row=2, column=1, padx=10, pady=10)

# Création d'une frame pour les boutons
button_frame = tk.Frame(root)
button_frame.grid(row=3, column=0, columnspan=3, pady=10)

# Ajouter des boutons dans la frame avec pack, alignés à droite
add_button = tk.Button(button_frame, text="Ajouter", command=add_student)
add_button.pack(side=tk.RIGHT, padx=5)

view_button = tk.Button(button_frame, text="Voir", command=view_students)
view_button.pack(side=tk.RIGHT, padx=5)

update_button = tk.Button(button_frame, text="Modifier", command=update_student)
update_button.pack(side=tk.RIGHT, padx=5)

delete_button = tk.Button(button_frame, text="Supprimer", command=delete_student)
delete_button.pack(side=tk.RIGHT, padx=5)


# exécution de la boucle principale
root.mainloop()