import tkinter as tk
from tkinter import ttk

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("ChallengeChasers")
        self.geometry("800x600")  # Taille initiale de la fenêtre
        self.resizable(True, True)  # Permettre le redimensionnement

        # Charger et afficher l'image
        image_path = ".\photos\Logo_challenge.png"
        self.image_tk = tk.PhotoImage(file=image_path)
        self.label_image = tk.Label(self, image=self.image_tk)
        self.label_image.pack(fill=tk.BOTH, expand=True)

        # Ajouter d'autres éléments ici selon vos besoins
        self.label_text = ttk.Label(self, text="Bienvenue dans votre application!")
        self.label_text.pack()

        # Lancer la boucle principale
        self.mainloop()

if __name__ == "__main__":
    app = Application()
