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


def test_2_viajes_2_horas():

	#Verifica que no se produzca transbordo en dos viajes con dos horas de diferencia

	T3 = Tarjeta()
	T3.reload(20)
	#Primer viaje -> 20 - 5.75 = 14.25
	T3.payTicket(C116, datetime.strptime ("01/09/2015 18:20", "%d/%m/%Y %H:%M"))
	#Segundo viaje (normal) -> 14.25 - 5.75 = 8.50
	T3.payTicket(C136, datetime.strptime ("01/09/2015 20:20", "%d/%m/%Y %H:%M"))
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
	lista_aux = T5.list_viajes


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



def test_reload_medio():
	M1 = TarjetaMedioBoleto()
	M1.reload(368)
	M1.reload(50)
	assert M1.money() == 510



def test_transbordo_medio():

	#Verifica funcionamiento del transbordo

	M1 = TarjetaMedioBoleto()
	M1.reload(10)
	#Primer viaje -> 10 - 2.90 = 7.10
	M1.payTicket(C116, datetime.strptime ("03/09/2015 09:30", "%d/%m/%Y %H:%M"))
	#Segundo viaje (transbordo) -> 7.10 - 0.96 = 6.14
	M1.payTicket(C112, datetime.strptime ("03/09/2015 09:40", "%d/%m/%Y %H:%M"))
	assert M1.money() == 6.14




def test_3_viajes_norm():

	#Verifica que haya un solo transbordo en tres viajes

	M2 = TarjetaMedioBoleto()
	M2.reload(20)
	#Primer viaje -> 20 - 2.90 = 17.10
	M2.payTicket(C116, datetime.strptime ("01/09/2015 18:20", "%d/%m/%Y %H:%M"))
	#Segundo viaje (transbordo) -> 17.10 - 0.96 = 16.14
	M2.payTicket(C112, datetime.strptime ("01/09/2015 18:40", "%d/%m/%Y %H:%M"))
	#Tercer viaje (normal) -> 16.14 - 2.90 = 13.24
	M2.payTicket(C116, datetime.strptime ("01/09/2015 19:00", "%d/%m/%Y %H:%M"))
	assert M2.money() == 13.24



def test_2_viajes_1_bondi():

	#Verifica que no se produzca transbordo en dos viajes realizados con el mismo bondi

	M3 = TarjetaMedioBoleto()
	M3.reload(20)
	#Primer viaje -> 20 - 2.90 = 17.10
	M3.payTicket(C116, datetime.strptime ("01/09/2015 18:20", "%d/%m/%Y %H:%M"))
	#Segundo viaje (normal) -> 17.10 - 2.90 = 14.20
	M3.payTicket(C116, datetime.strptime ("01/09/2015 18:50", "%d/%m/%Y %H:%M"))
	assert M3.money() == 14.20



def test_2_viajes_2_horas():

	#Verifica que no se produzca transbordo en dos viajes con dos horas de diferencia

	M3 = TarjetaMedioBoleto()
	M3.reload(20)
	#Primer viaje -> 20 - 2.90 = 17.10
	M3.payTicket(C116, datetime.strptime ("01/09/2015 18:20", "%d/%m/%Y %H:%M"))
	#Segundo viaje (normal) -> 17.10 - 2.90 = 14.20
	M3.payTicket(C136, datetime.strptime ("01/09/2015 20:20", "%d/%m/%Y %H:%M"))
	assert M3.money() == 14.20



def test_sin_saldo_norm():

	#Verifica que no se pueda realizar un viaje sin saldo en tarjeta

	M4 = TarjetaMedioBoleto()
	M4.reload(2.00)
	assert M4.payTicket(C116, datetime.strptime ("01/09/2015 18:20", "%d/%m/%Y %H:%M")) == False
	assert M4.money() == 2.00



def test_viajes_done_norm():


	M5 = TarjetaMedioBoleto()
	M5.reload(10)
	M5.payTicket(C116, datetime.strptime ("01/09/2015 18:20", "%d/%m/%Y %H:%M"))
	M5.payTicket(C136, datetime.strptime ("01/09/2015 18:25", "%d/%m/%Y %H:%M"))
	lista_aux = M5.list_viajes


	assert lista_aux[0].hora == datetime.strptime ("01/09/2015 18:20", "%d/%m/%Y %H:%M")
	assert lista_aux[0].costo == 2.90
	assert lista_aux[0].emp == "Amarillo"
	assert lista_aux[0].line == 116
	assert lista_aux[0].int == 5

	assert lista_aux[1].hora == datetime.strptime ("01/09/2015 18:25", "%d/%m/%Y %H:%M")
	assert lista_aux[1].costo == 0.96
	assert lista_aux[1].emp == "Naranja"
	assert lista_aux[1].line == 136
	assert lista_aux[1].int == 124