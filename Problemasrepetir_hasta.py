#Nombre del programa : Suponga que tiene quew usted una tienda y desea registrar las ventas en una computadora . Diseñe pseudocodigo que lea por cada cliente , el monto total de su compra . Al final del dia escriba la cantidad total de las ventas y el numero de clientes atendidos 
#Fecha : 14/05/2026


from tkinter import *

ventas = 0
clientes = 0

# Guardar
def guardar():

    global ventas
    global clientes

    precio = float(caja_precio.get())

    ventas = ventas + precio
    clientes = clientes + 1

    total.config(text="Total: $" + str(ventas))
    cantidad.config(text="Clientes: " + str(clientes))

# Limpiar
def nuevo():

    caja_nombre.delete(0, END)
    caja_producto.delete(0, END)
    caja_precio.delete(0, END)

# Cerrar
def cerrar():

    ventana.destroy()

# Ventana
ventana = Tk()
ventana.title("Tienda")
ventana.geometry("500x350")
ventana.config(bg="fuchsia")

# Título
titulo = Label(
    ventana,
    text="TIENDA CHABRY",
    font=("Arial", 20),
    bg="fuchsia"
)

titulo.pack(pady=10)

# Nombre
Label(
    ventana,
    text="Nombre Del Cliente :",
    font=("Arial", 12),
    bg="fuchsia"
).place(x=50, y=80)

caja_nombre = Entry(ventana)
caja_nombre.place(x=210, y=80)

# Producto
Label(
    ventana,
    text="Producto:",
    font=("Arial", 12),
    bg="fuchsia"
).place(x=50, y=130)

caja_producto = Entry(ventana)
caja_producto.place(x=210, y=130)

# Precio
Label(
    ventana,
    text="Precio:",
    font=("Arial", 12),
    bg="fuchsia"
).place(x=50, y=180)

caja_precio = Entry(ventana)
caja_precio.place(x=210, y=180)

# Botones
Button(
    ventana,
    text="Guardar",
    font=("Arial", 12),
    command=guardar
).place(x=20, y=250)

Button(
    ventana,
    text="Borrar",
    font=("Arial", 12),
    command=nuevo
).place(x=120, y=250)

Button(
    ventana,
    text="Agregar Otro Cliente",
    font=("Arial", 12),
    command=nuevo
).place(x=200, y=250)

Button(
    ventana,
    text="Cerrar",
    font=("Arial", 12),
    command=cerrar
).place(x=400, y=250)

# Resultados
total = Label(
    ventana,
    text="Total: $0",
    font=("Arial", 12),
    bg="fuchsia"
)

total.place(x=70, y=310)

cantidad = Label(
    ventana,
    text="Clientes: 0",
    font=("Arial", 12),
    bg="fuchsia"
)

cantidad.place(x=280, y=310)

# Ejecutar
ventana.mainloop()