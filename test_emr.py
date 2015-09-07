from TP_EMR import *
from datetime import datetime


C112 = Bondis("Azul",112,1)
C116 = Bondis("Amarillo",116,5)
C136 = Bondis("Naranja",136,124)

T = Tarjeta()
M = TarjetaMedioBoleto()


def test_reload():
	T.reload(196)
	assert T.money() == 230
	M.reload(368)
	M.reload(50)
	assert M.money() == 510
	

def test_viajes_done():

	#Tarjeta normal

	#Primer viaje -> 230 - 5.75 = 224.25
	T.payTicket(C116, datetime.strptime ("01/09/2015 18:20", "%d/%m/%Y %H:%M"))
	#Segundo viaje (transbordo) -> 224.25 - 1.90 = 222.35
	T.payTicket(C112, datetime.strptime ("01/09/2015 18:40", "%d/%m/%Y %H:%M"))
	assert T.money() == 222.35

	#Tarjeta medio boleto

	#Primer viaje -> 510 - 2.9 = 517.10
	M.payTicket(C116, datetime.strptime ("01/09/2015 19:00", "%d/%m/%Y %H:%M"))
	assert M.money() == 517.10
	#Segundo viaje (transbordo) -> 517.10 - 0.96 = 516.14
	M.payTicket(C112, datetime.strptime ("01/09/2015 19:20", "%d/%m/%Y %H:%M"))
	assert M.money() == 516.14
	#Tercer viaje (Normal, no medio) -> 516.14 - 5.75 = 510.39
	M.payTicket(C136, datetime.strptime ("01/09/2015 04:40", "%d/%m/%Y %H:%M"))
	#Cuarto viaje (transbordo normal, no medio) -> 510.39 - 1.9 = 508.49
	M.payTicket(C116, datetime.strptime ("01/09/2015 05:00", "%d/%m/%Y %H:%M"))
	assert M.money() == 508.19
