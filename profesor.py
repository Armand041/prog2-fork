class Profesor:
    total_profesores = 0  # Contador de instancias

    def __init__(self, nombre, especialidad, cursos_asignados):
        self.nombre = nombre
        self.especialidad = especialidad
        self.cursos_asignados = cursos_asignados
        Profesor.total_profesores += 1  # Aumenta el contador cada vez que se crea un profesor

    def asignar_curso(self, curso):
        print('Hola')
    def mostrar_informacion(self):
        print('Hola')

    def __str__(self):
        return f"{self.nombre}, {self.especialidad},{self.cursos_asignados}"
    def __repr__(self):
        return (f"nombre = {self.nombre}",
                f"especialidad = {self.especialidad},
                f"cursos_asignados = {self.cursos_asignados})
