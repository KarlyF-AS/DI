from site import ENABLE_USER_SITE


class Persoa:
    """Clase para definir unha puta persoa"""

    def __init__(self,nome,dni,idade):
        self.nome = nome
        self.dni = dni
        self.idade = self.comprobarIdade(idade)

    def comprobarIdade(self,id):
        if id >=0 and id < 100:
            return id
        else:
            return 0

class Traballador (Persoa,Posto):
    def __init__(self, nome, dni, idade, NUSS, salario, formacion):
    super().__init__(nome, dni, idade)
    self.NUSS = NUSS
    self.salario = salario
    self.formacion = formacion

class Posto ():
    def __init__(self, tarefa, horario, remuneracion, formacion):
        self.tarefa = tarefa
        self.horario = horario
        self.remuneracion = remuneracion
        self.formacion = formacion

p = Persoa ("Manuel", "345L", "34")
print(p.nome)
p.idade = -15
print(p.idade)