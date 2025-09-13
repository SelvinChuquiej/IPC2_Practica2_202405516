from model.paciente import Paciente
from model.cola_turnos import ColaTurnos   
from graphviz import Digraph

class TurnosController:
    def __init__(self):
        self.cola = ColaTurnos()
    
    def agregar_paciente(self, nombre, edad, especialidad):
        paciente = Paciente(nombre, edad, especialidad)
        self.cola.registrar(paciente)
        return paciente
    
    def atender_paciente(self):
        return self.cola.atender()
    
    def obtener_turnos(self):
        return self.cola.obtener_todos()
    
    def tiempo_espera(self):
        return self.cola.tiempo_espera_total()
    
    def obtener_tiempos(self):
        tiempos = []
        actual_cola = 0
        for paciente in self.cola.obtener_todos():
            tiempo_atencion = paciente.tiempo_atencion()
            tiempos.append((paciente, tiempo_atencion, actual_cola))
            actual_cola += tiempo_atencion
        return tiempos
    
    def graficar_cola(self, filename="cola"):
        dot = Digraph(comment="Cola de Pacientes", format="png")
        dot.attr(rankdir="LR", size="8")

        turnos = self.obtener_turnos()
        if not turnos:
            dot.node("Vacio", "Cola Vacía")
        else:
            for i, paciente in enumerate(turnos):
                etiqueta = f"{paciente.nombre}\n{paciente.especialidad}\n{paciente.tiempo_atencion()} min"
                dot.node(str(i), etiqueta, shape="box", style="filled", color="lightblue")

                if i > 0:
                    dot.edge(str(i-1), str(i))

        dot.render(filename, cleanup=True)
        return filename + ".png"