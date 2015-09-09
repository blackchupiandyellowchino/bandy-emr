from TP_EMR import *
from datetime import datetime
import math



C112 = Bondis("Azul",112,1)
C116 = Bondis("Amarillo",116,5)
C136 = Bondis("Naranja",136,124)

#T = Tarjeta()
#M = TarjetaMedioBoleto()



# Tests tarjeta normal


def test_reload_norm():
	T1 = Tarjeta()
	T1.reload(196)
	assert T1.money() == 230
	assert T1.reload("asd") == "No se pueden ingresar letras papwa"
	assert T1.money() == 230

	

def test_transbordo_norm():

	#Verifica funcionamiento del transbordo
	T1 = Tarjeta()
	T1.reload(196)
	#Primer viaje -> 230 - 5.75 = 224.25
	T1.payTicket(C116, datetime.strptime ("01/09/2015 18:20", "%d/%m/%Y %H:%M"))
	#Segundo viaje (transbordo) -> 224.25 - 1.90 = 222.35
	T1.payTicket(C112, datetime.strptime ("01/09/2015 18:40", "%d/%m/%Y %H:%M"))
	assert T1.money() == 222.35



def test_3_viajes_norm():

	#Verifica que haya un solo transbordo en tres viajes

	T2 = Tarjeta()
	T2.reload(30)
	#Primer viaje -> 30 - 5.75 = 24.25
	T2.payTicket(C116, datetime.strptime ("01/09/2015 18:20", "%d/%m/%Y %H:%M"))
	#Segundo viaje (transbordo) -> 24.25 - 1.90 = 22.35
	T2.payTicket(C112, datetime.strptime ("01/09/2015 18:40", "%d/%m/%Y %H:%M"))
	#Tercer viaje (normal) -> 22.35 - 5.75 = 16.60
	T2.payTicket(C116, datetime.strptime ("01/09/2015 19:00", "%d/%m/%Y %H:%M"))
	assert T2.money() == 16.60



def test_2_viajes_1_bondi():

	#Verifica que no se produzca transbordo en dos viajes realizados con el mismo bondi

	T3 = Tarjeta()
	T3.reload(20)
	#Primer viaje -> 20 - 5.75 = 14.25
	T3.payTicket(C116, datetime.strptime ("01/09/2015 18:20", "%d/%m/%Y %H:%M"))
	#Segundo viaje (normal) -> 14.25 - 5.75 = 8.50
	T3.payTicket(C116, datetime.strptime ("01/09/2015 18:50", "%d/%m/%Y %H:%M"))
	assert T3.money() == 8.50


def test_sin_saldo_norm():

	#Verifica que no se pueda realizar un viaje sin saldo en tarjeta

	T4 = Tarjeta()
	T4.reload(4.50)
	assert T4.payTicket(C116, datetime.strptime ("01/09/2015 18:20", "%d/%m/%Y %H:%M")) == False
	assert T4.money() == 4.50



def test_viajes_done_norm():
	T5 = Tarjeta()
	T5.reload(10)
	T5.payTicket(C116, datetime.strptime ("01/09/2015 18:20", "%d/%m/%Y %H:%M"))
	T5.payTicket(C136, datetime.strptime ("01/09/2015 18:25", "%d/%m/%Y %H:%M"))
	lista_aux = T5.doneTravels()
	assert lista_aux[0].hora == datetime.strptime ("01/09/2015 18:20", "%d/%m/%Y %H:%M")
	assert lista_aux[0].costo == 5.75
	assert lista_aux[0].emp == "Amarillo"
	assert lista_aux[0].line == 116
	assert lista_aux[0].int == 5

	assert lista_aux[1].hora == datetime.strptime ("01/09/2015 18:25", "%d/%m/%Y %H:%M")
	assert lista_aux[1].costo == 1.90
	assert lista_aux[1].emp == "Naranja"
	assert lista_aux[1].line == 136
	assert lista_aux[1].int == 124




# Tests tarjeta medio boleto

"""


def test_reload_medio():
	M.reload(368)
	M.reload(50)
	assert M.money() == 510



def test_viajes_medio():

	#Tarjeta medio boleto

	#Primer viaje -> 510 - 2.9 = 507.10
	M.payTicket(C116, datetime.strptime ("01/09/2015 19:00", "%d/%m/%Y %H:%M"))
	assert M.money() == 507.10
	#Segundo viaje (transbordo) -> 507.10 - 0.96 = 506.14
	M.payTicket(C112, datetime.strptime ("01/09/2015 19:20", "%d/%m/%Y %H:%M"))
	assert M.money() == 506.14
	#Tercer viaje (Normal, no medio) -> 506.14 - 5.75 = 500.39
	M.payTicket(C136, datetime.strptime ("01/09/2015 04:40", "%d/%m/%Y %H:%M"))
	#Cuarto viaje (transbordo normal, no medio) -> 500.39 - 1.9 = 498.49
	M.payTicket(C116, datetime.strptime ("01/09/2015 05:00", "%d/%m/%Y %H:%M"))
	assert M.money() == 498.49


"""