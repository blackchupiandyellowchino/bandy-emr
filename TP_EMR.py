#from datetime import datetime, timedelta, time
import time
from datetime import datetime, timedelta
import math
#now = datetime.now()

#datetime.strptime ("01/09/2015 18:20", "%d/%m/%Y %H:%M")

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
			if self.guita >= 1.90:
				self.guita = round(self.guita - 1.90,2)
				self.flag_bondi_ant = False
				self.bondi_anterior = 0			# LINEA de bondi anterior
				self.time_bondi_ant = 0
				self.aux_donetravels.set_travel(bondiola,self.horario,1.90)
				self.list_viajes.append(self.aux_donetravels)
				self.aux_donetravels = Viaje()
				return True
		else:

		# else Normal
			if self.guita >= 5.75:
				self.guita = round(self.guita - 5.75,2)
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
		if self.toload >= 0:
			if self.toload == 196:
				self.guita = self.guita + 230
			elif self.toload == 368:
				self.guita = self.guita + 460
			else:
				self.guita = self.guita + self.toload
		else:
			print ("Error. No se puede cargar saldo negativo o nulo")


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
					self.guita = round(self.guita - 0.96,2)
					self.flag_bondi_ant = False
					self.bondi_anterior = 0			# LINEA de bondi anterior
					self.time_bondi_ant = 0
					self.aux_donetravels.set_travel(bondiola,self.horario,0.96)
					self.list_viajes.append(self.aux_donetravels)
					self.aux_donetravels = Viaje()
					return True
			else:
		# else Normal
				if self.guita >= 2.90:
					self.guita = round(self.guita - 2.90,2)
					if self.flag_bondi_ant == False:
						self.flag_bondi_ant = True
					self.bondi_anterior = bondiola.line
					self.time_bondi_ant = self.horario
					self.aux_donetravels.set_travel(bondiola,self.horario,2.90)
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


T = Tarjeta()
T.reload("asd")