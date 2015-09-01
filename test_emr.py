from TP_EMR import *

def test_reload():
	T = Tarjeta()
	assert T.reload(196) == 230
