class Persona(object):

	def __init__(self):
		self.nombre = " "
		self.apellido = " "
		self.pais = Pais()

	def set_nombre (self, n):
		self.nombre = n

	def get_nombre(self):
		return self.nombre

	def set_apellido(self, a):
		self.apellido = a

	def get_apellido(self):
		return self.apellido

	def set_pais(self, m):
		self.pais = m

	def get_pais(self):
		return self.pais

	def presentar_datos(self):
		c = "Informacion:\n Nombres completos:%s-%s"%(self.get_nombre(),self.get_apellido())
		return c


class Estudiante(Persona):
	def __init__(self):
		super(Estudiante, self).__init__() #Obtenemos el init de la clase Persona
		self.codigo = " "  #Agregamos los nuevos atributos de nuestra nueva clase

	def set_codigo(self, c):
		self.codigo = c

	def get_codigo(self):
		return self.codigo

	def presentar_datos(self):
		c = "%s\n Código: %s\n Procedencia: Pais: %s \t Capital: %s"%(super(Estudiante, self).presentar_datos(), self.get_codigo(), self.pais.get_nombrep(), self.pais.get_capital())
		return c


class Estudiante_Presencial(Estudiante):
	def __init__(self):
		super(Estudiante_Presencial, self).__init__() #Obtenemos el init de la clase Persona
		self.num_creditos = 0
		self.ciclo = " "

	def set_num_creditos(self, nc):
		self.num_creditos = nc

	def get_num_creditos(self):
		return self.num_creditos

	def set_ciclo(self, cc):
		self.ciclo = cc

	def get_ciclo(self):
		return self.ciclo
		

class Estudiante_Distancia(Estudiante):
	def __init__(self):
		super(Estudiante_Distancia, self).__init__() #Obtenemos el init de la clase Persona
		self.num_materias = 0
		self.modulo = ""

	def set_num_materias(self, nm):
		self.num_materias = nm

	def get_num_materias(self):
		return self.num_materias

	def set_modulo(self, m):
		self.modulo = m

	def get_modulo(self):
		return self.modulo

	def presentar_datos(self):
		c = "%s\n Módulo: %s\n Numero de materias:%s "%(super(Estudiante_Distancia, self).presentar_datos(), self.get_modulo(),self.get_num_materias())
		return c

class Pais(object):

	def __init__(self):
		self.nombrep = ""
		self.capital = ""

	def set_nombrep(self, np):
		self.nombrep = np

	def get_nombrep(self):
		return self.nombrep 

	def set_capital(self , c):
		self.capital = c

	def get_capital(self):
		return self.capital