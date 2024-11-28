#PASO 1:
#psycopg2 es el adaptador de PostgreSQL para Python. Puedes instalarlo usando pip:
#pip install psycopg2-binary

#PASO 2:  Crear la Base de Datos y Tabla
#Vamos a crear una base de datos y una tabla en PostgreSQL. 
#Puedes hacerlo desde la línea de comandos de PostgreSQL (psql)
#o usando una herramienta gráfica como pgAdmin.

#-- Crear base de datos
#CREATE DATABASE agenda_db;

#-- Conectar a la base de datos
#\c agenda_db

#-- Crear tabla de contactos
#CREATE TABLE contactos (
#    id SERIAL PRIMARY KEY,
#    nombre VARCHAR(100) NOT NULL,
#    telefono VARCHAR(20) NOT NULL
#);

#Paso 3: Modificar el Código para Usar PostgreSQL
#Actualiza las funciones en tu código para conectarse a la base de datos PostgreSQL.
"""
import psycopg2
import tkinter as tk
from tkinter import messagebox

# Configuración de la conexión a PostgreSQL
def conectar_db():
    return psycopg2.connect(
        dbname='agenda_db',
        user='tu_usuario',
        password='tu_contraseña',
        host='localhost'
    )

# Función para agregar un contacto
def agregar_contacto():
    nombre = entrada_nombre.get()
    telefono = entrada_telefono.get()
    
    if nombre and telefono:
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute('INSERT INTO contactos (nombre, telefono) VALUES (%s, %s)', (nombre, telefono))
        conexion.commit()
        conexion.close()
        entrada_nombre.delete(0, tk.END)
        entrada_telefono.delete(0, tk.END)
        messagebox.showinfo("Éxito", "Contacto agregado correctamente.")
    else:
        messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")

# Función para buscar un contacto
def buscar_contacto():
    nombre = entrada_nombre.get()
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute('SELECT telefono FROM contactos WHERE nombre = %s', (nombre,))
    resultado = cursor.fetchone()
    conexion.close()
    
    if resultado:
        entrada_telefono.delete(0, tk.END)
        entrada_telefono.insert(0, resultado[0])
    else:
        messagebox.showwarning("No encontrado", "Contacto no encontrado.")

# Función para editar un contacto
def editar_contacto():
    nombre = entrada_nombre.get()
    telefono = entrada_telefono.get()
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute('UPDATE contactos SET telefono = %s WHERE nombre = %s', (telefono, nombre))
    conexion.commit()
    conexion.close()
    
    if cursor.rowcount:
        messagebox.showinfo("Éxito", "Contacto editado correctamente.")
    else:
        messagebox.showwarning("No encontrado", "Contacto no encontrado.")

# Función para eliminar un contacto
def eliminar_contacto():
    nombre = entrada_nombre.get()
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute('DELETE FROM contactos WHERE nombre = %s', (nombre,))
    conexion.commit()
    conexion.close()
    
    if cursor.rowcount:
        entrada_telefono.delete(0, tk.END)
        messagebox.showinfo("Éxito", "Contacto eliminado correctamente.")
    else:
        messagebox.showwarning("No encontrado", "Contacto no encontrado.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Agenda Personal")

# Etiquetas y campos de entrada
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.pack(padx=10, pady=5)
entrada_nombre = tk.Entry(ventana, width=50)
entrada_nombre.pack(padx=10, pady=5)

label_telefono = tk.Label(ventana, text="Teléfono:")
label_telefono.pack(padx=10, pady=5)
entrada_telefono = tk.Entry(ventana, width=50)
entrada_telefono.pack(padx=10, pady=5)

# Botones
boton_agregar = tk.Button(ventana, text="Agregar Contacto", command=agregar_contacto)
boton_agregar.pack(pady=10)

boton_buscar = tk.Button(ventana, text="Buscar Contacto", command=buscar_contacto)
boton_buscar.pack(pady=10)

boton_editar = tk.Button(ventana, text="Editar Contacto", command=editar_contacto)
boton_editar.pack(pady=10)

boton_eliminar = tk.Button(ventana, text="Eliminar Contacto", command=eliminar_contacto)
boton_eliminar.pack(pady=10)

# Ejecutar el loop principal de la interfaz
ventana.mainloop()
"""





