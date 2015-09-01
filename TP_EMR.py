from datetime import datetime, timedelta, time
import time

now = datetime.now()

class Tarjeta:
	def __init__(self):
		self.guita = 0
		self.flag_bondi_ant = False
		self.bondi_ant = 0
		self.time_bondi_ant = 0
		self.aux_donetravels = Viaje()
		# Ehm, la lista deberia tener el bondi, la hora y el costo del pasaje de cada viaje
		self.list_viajes = []


	def payTicket (self,bondiola,horario):
		self.auxpayTicket(bondiola,horario)


	def auxpayTicket (self,bondiola,horario):
		self.horario = horario
		if self.flag_bondi_ant == True and self.bondi_anterior != bondiola.line and self.horario - self.time_bondi_ant < timedelta(minutes=60):
			if self.guita >= 1.9:
				self.guita = self.guita - 1.9
				self.flag_bondi_ant = False
				self.bondi_anterior = 0			# LINEA de bondi anterior
				self.time_bondi_ant = 0
				self.aux_donetravels.set_travel(bondiola,self.horario,1.9)
				self.list_viajes.append(self.aux_donetravels)
				self.aux_donetravels = Viaje()
				return True
		else:

		# else Normal
			if self.guita >= 5.75:
				self.guita = self.guita - 5.75
				if self.flag_bondi_ant == False:
					self.flag_bondi_ant = True
				self.bondi_anterior = bondiola.line
				self.time_bondi_ant = self.horario
				self.aux_donetravels.set_travel(bondiola,self.horario,5.75)
				self.list_viajes.append(self.aux_donetravels)
				self.aux_donetravels = Viaje()
				return True
			else:
				return False


	def reload (self,toload):
		self.toload = toload
		if self.toload == 196:
			self.guita = self.guita + 230
		elif self.toload == 368:
			self.guita = self.guita + 460
		else:
			self.guita = self.guita + self.toload


	def money (self):
		return self.guita


	def doneTravels (self):
		# Return list_viajes
		for travel in self.list_viajes:
			print (str(travel.hora) + ", " + str(travel.costo) + ", " + str(travel.line) + ", " + str(travel.int) + ", " + str(travel.emp))



class TarjetaMedioBoleto (Tarjeta):

# Solo validas de 6 a 24 hs, todos los dias (incluyendo sabados y domingos). 


	def payTicket (self,bondiola,horario):
		self.horario = horario
		if 0 <= self.horario.time().hour <= 6:
			self.auxpayTicket(bondiola,horario)
		else:
			if self.flag_bondi_ant == True and self.bondi_anterior != bondiola.line and self.horario - self.time_bondi_ant < timedelta(minutes=60):
				if self.guita >= 0.96:
					self.guita = self.guita - 0.96
					self.flag_bondi_ant = False
					self.bondi_anterior = 0			# LINEA de bondi anterior
					self.time_bondi_ant = 0
					self.aux_donetravels.set_travel(bondiola,self.horario,0.96)
					self.list_viajes.append(self.aux_donetravels)
					self.aux_donetravels = Viaje()
					return True
			else:
		# else Normal
				if self.guita >= 2.9:
					self.guita = self.guita - 2.9
					if self.flag_bondi_ant == False:
						self.flag_bondi_ant = True
					self.bondi_anterior = bondiola.line
					self.time_bondi_ant = self.horario
					self.aux_donetravels.set_travel(bondiola,self.horario,2.9)
					self.list_viajes.append(self.aux_donetravels)
					self.aux_donetravels = Viaje()
					return True




class Bondis:
	def __init__ (self, empresa, linea, interno):
		self.emp = empresa
		self.line = linea
		self.int = interno



class Viaje:
	def __init__ (self):
		#self.cant_viajes = 0
		self.costo = 0
		self.hora = 0
		# De objeto de la clase Bondi
		self.emp = ""
		self.line = 0
		self.int = 0


	def set_travel(self,bondiola,hora,costo):
		self.hora = hora
		self.costo = costo
		self.emp = bondiola.emp
		self.line = bondiola.line
		self.int = bondiola.int










C112 = Bondis("Azul",112,1)
C116 = Bondis("Amarillo",116,5)
C136 = Bondis("Naranja",136,124)



# Funciones a probar: pagar, recarga, consulta viajes, saldo disponible


T = Tarjeta()


# Recarga

T.reload(196)
T.reload(50)


print ("Tarjeta normal \n")

print ("Dinero fase 1: " + str(T.money()) )

time.sleep(1)


#Primer viaje

T.payTicket(C116, datetime.now())

print ("Dinero fase 2 (primer viaje): " + str(T.money()) )

time.sleep(1)



#Segundo viaje (Transbordo)

T.payTicket(C112, datetime.now())

print ("Dinero fase 3 (segundo viaje; transbordo): " + str(T.money()))

time.sleep(1)




#Tercer viaje 

T.payTicket(C116, datetime.now())

print ("Dinero fase 4 (tercer viaje): " + str(T.money()) )

time.sleep(1)




#Cuarto viaje (no transbordo ya que pasa mas de una hora)

T.payTicket(C136, (timedelta(hours=7) + datetime.now()))

print ("Dinero fase 5 (cuarto viaje; 7 horas despues): " + str(T.money()) )

time.sleep(1.5)






# Viajes realizados

print ("\n \nViajes realizados con la tarjeta normal: \n" )

time.sleep(1)


T.doneTravels()


time.sleep(1)



print ("\nDinero disponible (tarjeta normal): " + str(T.money()) )



time.sleep(1.5)





print ("\n \n ---------------------------------------- \n \n \n" )


time.sleep(1)



# Tarjeta medio boleto

D = TarjetaMedioBoleto()




D.reload(368)
D.reload(196)



print ("Tarjeta con medio boleto \n \n")

print ("Dinero fase 1: " + str(D.money()) )

time.sleep(1)



#Primer viaje

D.payTicket(C116, datetime.now())

print ("Dinero fase 2 (primer viaje): " + str(D.money()) )

time.sleep(1)





#Segundo viaje (transbordo)

D.payTicket(C112, datetime.now())

print ("Dinero fase 3 (segundo viaje; transbordo): " + str(D.money()) )

time.sleep(1)






#Tercer viaje

#Este testeo fue hecho a las 12:48. Para comprobar la precision de los viajes medio boleto en la franja horaria entre las 0 y las 6
#basta con solo cambiar el timedelta


D.payTicket(C116, timedelta(hours=14)+datetime.now())

print ("Dinero fase 4 (tercer viaje, 14 horas despues; viaje normal): " + str(D.money()) )

time.sleep(1)




#print ("\n \n Datos de la tarjeta despues del tercer viaje: \n \n ")

#print(str(D.time_bondi_ant))


#Cuarto viaje (DEBERIA ser TRANSBORDO NORMAL)

D.payTicket(C136, timedelta(hours=14)+datetime.now())


#print ("\n \n Datos de la tarjeta despues del Cuarto viaje: \n \n ")

#print(str(D.time_bondi_ant))



print ("Dinero fase 5 (cuarto viaje; transbordo normal): " + str(D.money()) )


time.sleep(1.5)





print ("\n \nViajes realizados con la tarjeta medio boleto: \n" )

time.sleep(1)


D.doneTravels()

time.sleep(1)

print ("\nDinero disponible (tarjeta medio boleto): " + str(T.money()) )



time.sleep(1.5)
