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
    
    