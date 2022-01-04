import sys
sys.path.append(".")
from src.dni import dni

def test_dni():

    # Verificar DNI
    assert True == dni('45699019C').verifyDni()
    assert False == dni('45699019A').verifyDni()
    assert True == dni('43469656R').verifyDni()

    # DNI sano
    assert False == dni('asdcxzcvds').DNISano()
    assert False == dni('1234567C').DNISano() 

