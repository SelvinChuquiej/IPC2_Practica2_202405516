from model.nodo import Nodo

class ColaTurnos:
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamano = 0

    def registrar(self, paciente):
        nuevo = Nodo(paciente)
        if self.esta_vacia():
            self.frente = nuevo
            self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo
        self.tamano += 1

    def atender(self):
        if self.esta_vacia():
            return None
        paciente = self.frente.paciente
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        self.tamano -= 1
        return paciente
    
    def esta_vacia(self):
        return self.frente is None
    
    def tiempo_espera_total(self):
        actual = self.frente
        total = 0
        while actual:
            total += actual.paciente.tiempo_atencion()
            actual = actual.siguiente
        return total
    
    def obtener_todos(self):
        pacientes = []
        actual = self.frente
        while actual:
            pacientes.append(actual.paciente)
            actual = actual.siguiente
        return pacientes