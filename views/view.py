import tkinter as tk
from tkinter import messagebox, ttk
from controller.controller import TurnosController
from PIL import Image, ImageTk
 
class TurnosApp:
    def __init__(self, root):
        self.controller = TurnosController()

        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)

        archivo_menu = tk.Menu(menu_bar, tearoff=0)
        archivo_menu.add_command(label="Salir", command=root.destroy)
        menu_bar.add_cascade(label="Archivo", menu=archivo_menu)

        root.title("Sistema de Turnos Médicos")
        root.geometry("800x400")

        tk.Label(root, text="Nombre:").pack()
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.pack()

        tk.Label(root, text="Edad:").pack()
        self.entry_edad = tk.Entry(root)
        self.entry_edad.pack()

        tk.Label(root, text="Especialidad:").pack()
        self.combo_especialidad = ttk.Combobox(root, values=["Medicina General", "Pediatría", "Ginecologia", "Dermatología"])
        self.combo_especialidad.pack()

        tk.Button(root, text="Agregar Paciente", command=self.registrar).pack(pady=5)
        tk.Button(root, text="Atender Paciente", command=self.atender).pack(pady=5)
       
        self.lista = tk.Listbox(root, width=80, height=10)
        self.lista.pack(pady=10)

        self.label_tiempo = tk.Label(root, text="Tiempo total estimado: 0 minutos")
        self.label_tiempo.pack()

    def registrar(self):
        nombre = self.entry_nombre.get()
        edad = self.entry_edad.get()
        especialidad = self.combo_especialidad.get()

        if not nombre or not edad or not especialidad:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return

        paciente = self.controller.agregar_paciente(nombre, int(edad), especialidad,)
        self.actualizar_lista()
        self.mostrar_grafico() 
        messagebox.showinfo("Registrado", f"Paciente agregado:\n{paciente}")

    def atender(self):
        paciente = self.controller.atender_paciente()
        if paciente:
            messagebox.showinfo("Atendiendo", f"Se está atendiendo a:\n{paciente}")
        else:
            messagebox.showinfo("Cola vacía", "No hay pacientes en espera")
        self.actualizar_lista()
        self.mostrar_grafico() 


    def actualizar_lista(self):
        self.lista.delete(0, tk.END) 
        for paciente, t_atencion, t_cola in self.controller.obtener_tiempos():
            self.lista.insert(
                tk.END,
                f"{paciente} | Atención: {t_atencion} min | Cola: {t_cola} min"
            )
        self.label_tiempo.config(
            text=f"Tiempo total estimado en cola: {self.controller.tiempo_espera()} min"
        )

    def mostrar_grafico(self):
        img_path = self.controller.graficar_cola()

        ventana = tk.Toplevel()
        ventana.title("Cola de Pacientes")
        
        img = Image.open(img_path)
        img = img.resize((600, 200))
        img_tk = ImageTk.PhotoImage(img)

        lbl = tk.Label(ventana, image=img_tk)
        lbl.image = img_tk
        lbl.pack()