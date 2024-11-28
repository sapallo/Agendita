import tkinter as tk

ventana = tk.Tk()
ventana.title("UNA AGENDA loca pero buena")
ventana.geometry("400x500")
label_algo = tk.Label(ventana, text= "Nombre/Apelliedo/Alias/como te lo acuerdes")
label_algo.pack(padx=20, pady=15)
campo_nombre = tk.Entry(ventana, width=30)
campo_nombre.pack(padx=10, pady=5)
label_numero = tk.Label(ventana, text="el numero en cuestion")
label_numero.pack(padx=20, pady=15)
campo_numero = tk.Entry(ventana, width=30)
campo_numero.pack(padx=10, pady=5)

boton_a = tk.Button(ventana, text="Agregar")
boton_a.pack(pady=20,padx=20)
boton_b = tk.Button(ventana, text="Buscar")
boton_b.pack(pady=22)
boton_ed = tk.Button(ventana, text="Editar")
boton_ed.pack(pady=25)
boton_el = tk.Button(ventana, text="Elimar")
boton_el.pack(pady=20)



ventana.mainloop()







