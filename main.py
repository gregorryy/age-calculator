import tkinter as tk
from tkinter.messagebox import showinfo
import time
from threading import Thread

agec = tk.Tk()
agec.geometry("350x150")
agec.title("Age calculator")

def show_loading():
    loading = tk.Toplevel()  # Crée une nouvelle fenêtre (Toplevel)
    loading.title("Loading...")
    loading.geometry("300x100")
    label = tk.Label(loading, text="Loading, please wait...")
    label.pack(expand=True)
    # Ferme la fenêtre de chargement après 3 secondes
    loading.after(1500, loading.destroy)
    # Empêche l'utilisateur d'interagir avec la fenêtre principale
    loading.transient(agec)
    loading.grab_set()
    agec.wait_window(loading)

# Fonction simulant une tâche longue
def long_task():
    show_loading()  # Affiche la fenêtre de chargement
    time.sleep(1)
    res = myEntry.get()    # Simule une tâche prenant du temps
    showinfo("Age calculator", f"You have {res} years old !")  # Message de fin de tâche

# Fonction pour exécuter la tâche dans un thread séparé
def start_task():
    # Lancer la tâche longue dans un thread pour éviter de bloquer l'interface
    thread = Thread(target=long_task)
    thread.start()

myLabel = tk.Label(agec, text="Enter your age :", font=("Arial", 16))
myLabel.pack()    
    
myEntry = tk.Entry(agec, width=40)
myEntry.pack(pady=20)

btn = tk.Button(agec, height=1, width=10, text="Calculate", command=long_task, fg="white", bg="red")
btn.pack()
      
agec.mainloop()