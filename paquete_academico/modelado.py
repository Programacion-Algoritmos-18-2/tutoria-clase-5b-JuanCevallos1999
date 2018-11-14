class Persona(object):  #Creamos la clase Persona que es la clase Padre

	def __init__(self): #Ponemos los atributos de la clase padre
		self.nombre = " "
		self.apellido = " "
		self.pais = Pais() #Creamos un atributo de clase pais
#Setters y getters
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
#Método presentar datos
	def presentar_datos(self):
		c = "Informacion:\n Nombres completos:%s-%s"%(self.get_nombre(),self.get_apellido())
		return c

#Creamos la clase Estudiante que hereda atributos de estudiante
class Estudiante(Persona):
	def __init__(self):
		super(Estudiante, self).__init__() #Obtenemos el init de la clase Persona
		self.codigo = " "  #Agregamos los nuevos atributos de nuestra nueva clase

	def set_codigo(self, c):
		self.codigo = c

	def get_codigo(self):
		return self.codigo
#Metodo presentamos los datos que requiera esta clase
	def presentar_datos(self):
		c = "%s\n Código: %s\n Procedencia: Pais: %s \t Capital: %s"%(super(Estudiante, self).presentar_datos(), self.get_codigo(), self.pais.get_nombrep(), self.pais.get_capital())
		return c

#Creamos la clase Estudiante Presencial que hereda atributos de Estudiante
class Estudiante_Presencial(Estudiante):
	def __init__(self):
		super(Estudiante_Presencial, self).__init__() #Obtenemos el init de la clase Persona
		self.num_creditos = 0
		self.ciclo = " "
##Setters y getters
	def set_num_creditos(self, nc):
		self.num_creditos = nc

	def get_num_creditos(self):
		return self.num_creditos

	def set_ciclo(self, cc):
		self.ciclo = cc

	def get_ciclo(self):
		return self.ciclo
		
#Creamos la clase 
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
#Creamos el metodo presentar datos que heredara la cadena anterior y presentara los atributos nuevos
	def presentar_datos(self):
		c = "%s\n Módulo: %s\n Numero de materias:%s "%(super(Estudiante_Distancia, self).presentar_datos(), self.get_modulo(),self.get_num_materias())
		return c
#Creamos la clase pais que hereda automaicamente de object
class Pais(object):
#Creamos los atributos de esta clase 
	def __init__(self):
		self.nombrep = ""
		self.capital = ""
#Set y get
	def set_nombrep(self, np):
		self.nombrep = np

	def get_nombrep(self):
		return self.nombrep 

	def set_capital(self , c):
		self.capital = c

	def get_capital(self):
		return self.capital