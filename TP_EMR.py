from datetime import datetime, timedelta, time

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
				self.time_bondi_ant = now
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
			print str(travel.hora) + ", " + str(travel.costo) + ", " + str(travel.line) + ", " + str(travel.int) + ", " + str(travel.emp)



class TarjetaMedioBoleto (Tarjeta):

# Solo validas de 6 a 24 hs, todos los dias (incluyendo sabados y domingos). 


	def payTicket (self,bondiola,horario):
		self.horario = horario
		print self.horario.time()
		if time(00,00,00) >= self.horario.time() >= time(06,00,00):
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
					self.time_bondi_ant = now
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


print "Tarjeta normal \n"

print "Dinero fase 1: " + str(T.money())



#Primer viaje

T.payTicket(C116, datetime.now())

print "Dinero fase 2: " + str(T.money())


#Segundo viaje (Transbordo)

T.payTicket(C112, datetime.now())

print "Dinero fase 3: " + str(T.money())


#Tercer viaje 

T.payTicket(C116, datetime.now())

print "Dinero fase 4: " + str(T.money())


#Cuarto viaje (no transbordo ya que pasa mas de una hora)

T.payTicket(C136, (timedelta(hours=7) + datetime.now()))

print "Dinero fase 5: " + str(T.money())



# Viajes realizados

print "\n Viajes realizados con la tarjeta normal: \n"

T.doneTravels()

print "\nDinero disponible (tarjeta normal): " + str(T.money())





print "\n \n ---------------------------------------- \n \n \n"





# Tarjeta medio boleto

D = TarjetaMedioBoleto()




D.reload(368)
D.reload(196)


print "Tarjeta con medio boleto \n \n"

print "Dinero fase 1: " + str(D.money())


#Primer viaje

D.payTicket(C116, datetime.now())

print "Dinero fase 2: " + str(D.money())


#Segundo viaje (transbordo)

D.payTicket(C112, datetime.now())

print "Dinero fase 3: " + str(D.money())


#Tercer viaje

D.payTicket(C116, datetime.now())

print "Dinero fase 4: " + str(D.money())


#Cuarto viaje (transbordo NORMAL)

D.payTicket(C136, timedelta(hours=5)+datetime.now())

print "Dinero fase 5: " + str(D.money())


print "\nViajes realizados con la tarjeta medio boleto: \n"

D.doneTravels()