class Paciente:
    def __init__(self, nombre, edad, especialidad, tiempo_estimado):
        self.nombre = nombre
        self.edad = edad
        self.especialidad = especialidad
        self.tiempo_estimado = tiempo_estimado
        self.siguiente = None

    def __str__(self):
        return f"Paciente(nombre={self.nombre}, edad={self.edad}, especialidad={self.especialidad}, tiempo_estimado={self.tiempo_estimado})"
