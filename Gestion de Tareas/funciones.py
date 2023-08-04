import sqlite3
from tkinter import *



def mostrar_tareas(root):
    # Función para mostrar todas las tareas en la base de datos
    conn = sqlite3.connect('tareas.db')
    cursor = conn.execute('SELECT * FROM tareas')
    tareas = cursor.fetchall()
    conn.close()

    texto_mostrar = Label(root, text='Tareas:')
    texto_mostrar.grid(row=0, column=1)
    for tarea in tareas:
        tarea_id, tarea_desc, completed = tarea
        status = "Completada" if completed else "Pendiente"
        tareas = Label(root, text=f'{tarea_id}. [{status}] {tarea_desc}')
        tareas.grid(row=tarea_id, column=1)


def agregar_tares(root, tarea_desc):
    # Función para agregar una nueva tarea
    conn = sqlite3.connect('tareas.db')
    conn.execute('INSERT INTO tareas (tarea) VALUES (?)', (tarea_desc,))
    conn.commit()
    conn.close()
    completado = Label(root, text='Tarea agregada con éxito.')
    completado.grid(row=5)


def elimanar_tareas(root, tarea_id):
    # Función para eliminar una tarea
    conn = sqlite3.connect('tareas.db')
    conn.execute('DELETE FROM tareas WHERE id = ?', (tarea_id,))
    conn.commit()
    conn.close()
    completado = Label(root,text="Tarea eliminada con éxito.")
    completado.grid()


def modificar_tareas(root, tarea_id):
    # Función para marcar una tarea como completada
    conn = sqlite3.connect('tareas.db')
    conn.execute('UPDATE tareas SET completed = 1 WHERE id = ?', (tarea_id,))
    conn.commit()
    conn.close()
    completado = Label(root,text="Tarea completada con éxito.")
    completado.grid()