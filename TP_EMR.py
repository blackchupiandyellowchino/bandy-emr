import time
import sys


class Tarjeta:
	def __init__(self):
		self.guita = 0
		self.flag_bondi_ant = False
		self.bondi_ant = 0
		aux_doneTravels = Viaje()
		# Ehm, la lista deberia tener el bondi, la hora y el costo del pasaje de cada viaje
		list_viajes = []


	def payTicket (self,bondiola,horario):

		# guita - costo
		# Then copiar datos a aux_doneTravels y de ahi a list_viajes[]

		# if tome bondi antes and self.bondi_anterior != Bondi_actual -> Transbordo

			if self.flag_bondi_ant == True and self.bondi_anterior != bondiola.linea:
				if self.guita >= 1.9:
					self.guita = self.guita - 1.9
					self.flag_bondi_ant = False
					self.bondi_anterior = 0
					return True
				else:
					return False

		# else Normal

			else:
				if self.guita >= 5.75:
					self.guita = self.guita - 5.75
					self.flag_bondi_ant = True
					self.bondi_anterior = bondiola.linea
					return True
				else:
					return False




	def reload (self,toload):
		if self.toload == 196:
			self.guita = self.guita + 230
		elif self.toload == 368:
			self.guita = self.guita + 460
		else
			self.guita = self.guita + self.toload


	def money (self):
		return self.guita


	def doneTravels (self):
		# Don't know como representar los bondis



class TarjetaComun (Tarjeta):
	def __init__ (self):


class TarjetaMedioBoleto (Tarjeta):
	def __init__ (self):

# Sólo válidas de 6 a 24 hs, todos los días (incluyendo sábados y domingos). 
# Meter un if en money()



class Bondis:
	def __init__ (self, empresa, linea, interno):
		self.emp = empresa
		self.line = linea
		self.int = interno



class Viaje:
	def __init__ (self):
		self.cant_viajes = 0
		self.emp = ""
		self.line = 0
		self.int = 0
		self.costo = 0


# bondi, horario, monto del pasaje