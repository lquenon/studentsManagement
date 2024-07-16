# initialisation tkinter
import tkinter as tk
from tkinter import messagebox

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Configuration de la base de données
engine = create_engine('sqlite:///students.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# initialisation de la fenêtre principale de l'application
root = tk.Tk()
root.title("Système de gestion d'étudiants")
root.geometry("600x400")

# fonctions CRUD en relation avec les boutons
# définir avant appel

# students = []

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    student_class = Column(String(20), nullable=False)

# Créez la base de données et les tables
Base.metadata.create_all(engine)

def add_student():
    # print("Ajout")
    name = name_entry.get()
    age = age_entry.get()
    student_class = class_entry.get()
    if name and age and student_class:
    #     students.append({"name": name, "age": age, "class": student_class})
    #     messagebox.showinfo("Succès", "Étudiant ajouté avec succès")
    #     clear_entries()
    # else:
    #     messagebox.showerror("Erreur", "Tous les champs sont obligatoires")
        new_student = Student(name=name, age=int(age), student_class=student_class)
        session.add(new_student)
        session.commit()
        tk.messagebox.showinfo("Succès", "Étudiant ajouté avec succès")
        clear_entries()
    else:
        tk.messagebox.showerror("Erreur", "Tous les champs sont obligatoires")

def view_students():
    # print("Consulation")
    students = session.query(Student).all()
    view_window = tk.Toplevel(root)
    view_window.title("Liste des Étudiants")
    for i, student in enumerate(students):
        tk.Label(view_window, text=f"{student.name} - {student.age} - {student.student_class}").grid(row=i, column=0)


def update_student():
    # print("Mise à jour")
    # name = name_entry.get()
    # age = age_entry.get()
    # student_class = class_entry.get()
    # for student in students:
    #     if student['name'] == name:
    #         student['age'] = age
    #         student['class'] = student_class
    #         messagebox.showinfo("Succès", "Étudiant mis à jour avec succès")
    #         clear_entries()
    #         return
    # messagebox.showerror("Erreur", "Étudiant non trouvé")
    name = name_entry.get()
    age = age_entry.get()
    student_class = class_entry.get()
    student = session.query(Student).filter_by(name=name).first()
    if student:
        student.age = int(age)
        student.student_class = student_class
        session.commit()
        tk.messagebox.showinfo("Succès", "Étudiant mis à jour avec succès")
        clear_entries()
    else:
        tk.messagebox.showerror("Erreur", "Étudiant non trouvé")

def delete_student():
    # # print("Suppression")
    # name = name_entry.get()
    # for student in students:
    #     if student['name'] == name:
    #         students.remove(student)
    #         messagebox.showinfo("Succès", "Étudiant supprimé avec succès")
    #         clear_entries()
    #         return
    # messagebox.showerror("Erreur", "Étudiant non trouvé")
    name = name_entry.get()
    student = session.query(Student).filter_by(name=name).first()
    if student:
        session.delete(student)
        session.commit()
        tk.messagebox.showinfo("Succès", "Étudiant supprimé avec succès")
        clear_entries()
    else:
        tk.messagebox.showerror("Erreur", "Étudiant non trouvé")

def clear_entries():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    class_entry.delete(0, tk.END)

# Ajout des éléments de saisie et étiquettes

tk.Label(root, text="Nom:").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root,  width=75)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Âge:").grid(row=1, column=0, padx=10, pady=10)
age_entry = tk.Entry(root, width=75)
age_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Classe:").grid(row=2, column=0, padx=10, pady=10)
class_entry = tk.Entry(root, width=75)
class_entry.grid(row=2, column=1, padx=10, pady=10)

# Création d'une frame pour les boutons
button_frame = tk.Frame(root)
button_frame.grid(row=3, column=0, columnspan=3, pady=10, sticky="E")

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