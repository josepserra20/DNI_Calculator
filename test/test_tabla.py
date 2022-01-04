import sys
sys.path.append(".")
from src.TablaAsignacion import TablaAsignacion
tabla = TablaAsignacion()

def test_tabla():
    assert 'C' == tabla.calcularLetra(45699019)
    assert 'L' == tabla.calcularLetra(26450640)
    assert 'S' == tabla.calcularLetra(18032682)