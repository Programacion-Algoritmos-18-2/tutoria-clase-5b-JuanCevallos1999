from paquete_academico.modelado import *
p = Pais()
p.set_nombrep("Ecuador")
p.set_capital("Quito")
est1 = Estudiante_Distancia()
est1.set_nombre("Juan")
est1.set_apellido("Diaz")
est1.set_codigo("11012")
est1.set_num_materias(5)
est1.set_modulo("NOVENO")
est1.set_pais(p)
print(est1.presentar_datos())