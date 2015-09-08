from TP_EMR import *
from datetime import datetime
import math


C112 = Bondis("Azul",112,1)
C116 = Bondis("Amarillo",116,5)
C136 = Bondis("Naranja",136,124)

T = Tarjeta()
M = TarjetaMedioBoleto()


def test_reload_norm():
	T.reload(196)
	assert T.money() == 230


def test_reload_medio():
	M.reload(368)
	M.reload(50)
	assert M.money() == 510
	

def test_viajes_done_norm():

	#Tarjeta normal

	#Primer viaje -> 230 - 5.75 = 224.25
	T.payTicket(C116, datetime.strptime ("01/09/2015 18:20", "%d/%m/%Y %H:%M"))
	#Segundo viaje (transbordo) -> 224.25 - 1.90 = 222.35
	T.payTicket(C112, datetime.strptime ("01/09/2015 18:40", "%d/%m/%Y %H:%M"))
	assert T.money() == 222.35


def test_viajes_done_medio():

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