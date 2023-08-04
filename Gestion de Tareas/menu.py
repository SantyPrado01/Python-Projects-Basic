import sqlite3
from funciones import *
from tkinter import *

# Conexión a la base de datos (creará un archivo si no existe)
base_datos = sqlite3.connect('tareas.db')

# Crear tabla de tareas si no existe
base_datos.execute('''
    CREATE TABLE IF NOT EXISTS tareas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tarea TEXT NOT NULL,
        completed INTEGER NOT NULL DEFAULT 0
    )
''')

base_datos.commit()
base_datos.close()

#-------------------------------------------- TKINTER -------------------------------------------------

root = Tk()

root.title('Control de Tareas')


tareas_txt = Label(root, text='Esta aplicacion te permite llevar un control de tus tareas. Agregando, Eliminando y Completando tareas.').grid()

boton_tareas_mostrar = Button(root, text='Mostrar Tareas', command= lambda:mostrar_tareas(root))
boton_tareas_mostrar.grid()

agregar_txt = Label(root, text='Que tarea deseas agregar?').grid()
desc_agregar = Entry(root)
desc_agregar.grid(row=4, column=0)

boton_tareas_agregar = Button(root, text='Agregar Tarea', command= lambda:agregar_tares(root, desc_agregar.get()))
boton_tareas_agregar.grid(row=5, column=0)

eliminar_txt = Label(root, text='Eliminar Tareas. Escriba el numero de la tarea a eliminar.').grid()
eliminar_entry = Entry(root)
eliminar_entry.grid()
boton_tareas_eliminar = Button(root, text='Eliminar Tarea', command= lambda:elimanar_tareas(root, eliminar_entry.get()))
boton_tareas_eliminar.grid()


completar_txt = Label(root, text='Completar Tareas. Escriba el numero de la tarea a eliminar.').grid()
completar_entry =Entry(root)
completar_entry.grid()
boton_tareas_completar = Button(root, text='Completar Tarea', command= lambda:modificar_tareas(root, completar_entry.get()))
boton_tareas_completar.grid()



root=mainloop()


