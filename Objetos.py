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

class Posto2 ():
    def __init__(self, tarefa, horario, remuneracion, formacion, **outros):
        self.tarefa = tarefa
        self.horario = horario
        self.remuneracion = remuneracion
        self.formacion = formacion

class Traballador2 (Persoa2,Posto2):
    def __init__(self, nome, dni, idade, tarefa, horario, remuneracion, formacion, NUSS):
        super().__init__(nome=nome, dni=dni, idade=idade, tarefa=tarefa, horario=horario, remuneracion=remuneracion, formacion=formacion)
        self.NUSS = NUSS

t2 = Traballador2("Juan", "567U", 45, "Soldador", 7, 2300, "CM", 123455)
print(t2.remuneracion)

p = Persoa ("Manuel", "345L", "34")
print(p.nome)
p.idade = -15
print(p.idade)

#Encapsulacion
class Perso3:
    """Clase para definir unha puta persoa"""

    def __init__(self,nome,dni,idade):
        self.__nome = nome
        self.__dni = dni
        self.__idade = self.comprobarIdade(idade)

    def setIdade(self,id):
        if id>=0 and id < 100:
            self.__idade = id
        else:
            self.__idade = 0

    def getIdade (self):
        return self.__idade

    def __str__(self):
        return "Nome: "+ self.nome + "\nDni: " + self.__dni

    def __eq__(self, other):
        return self.dni == outro.dni



p3 = Perso3 ("Perico", "8900P", 54)
p3.dni = 2+5j
print(p3.dni)
print(p3._Persoa3__dni)
print(p3.__dni)