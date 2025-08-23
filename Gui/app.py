import tkinter as tk

# Fenster erstellen
root = tk.Tk()
root.title("Tkinter Demo")
root.geometry("300x200")

# Label
label = tk.Label(root, text="Hallo, Tkinter!", font=("Arial", 14))
label.pack(pady=20)

# Button mit Aktion
def klicken():
    label.config(text="Button gedrückt!")

button = tk.Button(root, text="Klick mich", command=klicken)
button.pack()

# Fenster starten
root.mainloop()
