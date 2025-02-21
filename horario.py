class Horario:
    total_horarios = 0  # Contador de instancias

    def __init__(self, curso, dia, hora_inicio, hora_fin):
        self.curso = curso
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        Horario.total_horarios += 1  # Aumenta el contador cada vez que se crea un horario

    def mostrar_horario(self):
        print(f'Curso: {self.curso},Dia: {self.dia}, Hora inicio:{self.hora_inicio},Hora fin: {self.hora_fin}')

    #def modificar_horario(self, nuevo_horario):
     #   nuevo_horario = {}



horario1 = Horario(1,2,3,4)
horario1.mostrar_horario()

horario2 = Horario(1, 5, 9, 4)
horario2.mostrar_horario()