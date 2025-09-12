class Paciente:
    def __init__(self, nombre, edad, especialidad):
        self.nombre = nombre
        self.edad = edad
        self.especialidad = especialidad

        self.tiempos = {
            "Medicina General": 10,
            "Pediatría": 15,
            "Ginecología": 20,
            "Dermatología": 25
        }

    def tiempo_atencion(self):
        return self.tiempos.get(self.especialidad, 10)
    
    def __str__(self):
        return f"{self.nombre} ({self.edad} años) - {self.especialidad}"