from TP_EMR import *

def test_reload():
	T = Tarjeta()
	T.reload(196)
	assert T.money() == 230
