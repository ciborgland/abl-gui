from tkinter import *
from tkinter import ttk
import controller as c

root = Tk()
root.geometry('850x450')
root.title('Ciborgland - ABL')
frame = Frame(root)
frame.config(bd=15)
frame.config(relief='groove')
frame.pack(fill=BOTH)
frame_2 = Frame(root)
frame_2.pack(fill=BOTH)
frame_3 = Frame(root)
frame_3.pack()

def insertar_db():
    nombre = e_nombre.get()
    apellido = e_apellido.get()
    celular = e_celular.get()
    email = e_email.get()
    
    c.insertRow(nombre, apellido, celular, email)
    borrar_todo()
    mostrar()
    
    e_nombre.delete(0, END)
    e_apellido.delete(0, END)
    e_celular.delete(0, END)
    e_email.delete(0, END)

e_nombre = ttk.Entry(frame, width=50)
e_nombre.grid(row=1, column=1, padx=20, pady=4)
e_apellido = ttk.Entry(frame, width=50)
e_apellido.grid(row=2, column=1)
e_celular = ttk.Entry(frame, width=50)
e_celular.grid(row=3, column=1)
e_email = ttk.Entry(frame, width=50)
e_email.grid(row=4, column=1, pady=4)

l_nombre = ttk.Label(frame, text='Nombre')
l_nombre.grid(row=1, column=0)
l_apellido = ttk.Label(frame, text='Apellido')
l_apellido.grid(row=2, column=0)
l_celular = ttk.Label(frame, text='Celular')
l_celular.grid(row=3, column=0)
l_email = ttk.Label(frame, text='Email')
l_email.grid(row=4, column=0)

tree = ttk.Treeview(frame_2, column=('#1','#2','#3','#4'))
tree.heading('#0', text= 'Id')
tree.heading('#1', text= 'Nombre')
tree.heading('#2', text= 'Apellido')
tree.heading('#3', text= 'Celular')
tree.heading('#4', text= 'Email')
tree.column('#0', width=40)
tree.column('#1', width=200)
tree.column('#2', width=200)
tree.column('#3', width=150)
tree.column('#4', width=250)

def mostrar():
    resul = c.search()
    for i in resul:
        tree.insert('',END, text=str(i[0]), values=(i[1],i[2],i[3],i[4]))
    tree.pack(pady=20)
mostrar()

def borrar_todo():
    for record in tree.get_children():
        tree.delete(record)

def eliminar():
    item = tree.item(tree.selection())['text']
    c.deleteRow(item)
    borrar_todo()
    mostrar()

def salir():
    exit()

boton1 = ttk.Button(frame, text = 'Insertar', width='35', command = insertar_db)
boton1.grid(row=2, column=3)

boton3 = ttk.Button(frame, text = 'Eliminar', width='35', command = eliminar)
boton3.grid(row=3, column=3)

boton4 = ttk.Button(frame_3, text = 'Salir', width='35', command = salir)
boton4.grid(row=10, column=2)

root.mainloop()