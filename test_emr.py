from TP_EMR import *

T = Tarjeta()

def test_reload():
	assert T.reload(196) == 230
