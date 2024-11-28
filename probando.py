import tkinter as tk
from tkinter import messagebox

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda")

        self.entries = []  # Array para almacenar los datos

        # Configuración de la interfaz
        self.label = tk.Label(root, text="Entrada:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.add_button = tk.Button(root, text="Agregar", command=self.add_entry)
        self.add_button.pack()

        self.delete_button = tk.Button(root, text="Eliminar", command=self.delete_entry)
        self.delete_button.pack()

        self.listbox = tk.Listbox(root)
        self.listbox.pack()

    def add_entry(self):
        entry_text = self.entry.get()
        if entry_text:
            self.entries.append(entry_text)
            self.listbox.insert(tk.END, entry_text)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No puedes agregar una entrada vacía.")

    def delete_entry(self):
        selected_entry = self.listbox.curselection()
        if selected_entry:
            index = selected_entry[0]
            self.listbox.delete(index)
            del self.entries[index]
        else:
            messagebox.showwarning("Advertencia", "Selecciona una entrada para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()

