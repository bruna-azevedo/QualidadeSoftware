from main import *

def test_e_pangrama():
    assert e_pangrama("The quick brown fox jumps over the lazy dog") == True
    assert e_pangrama("Pack my box with five dozen liquor jugs") == True
    assert e_pangrama("Hello world") == False


def test_formatar_numero_telefone():
    assert formatar_numero_telefone("1234567890") == "(123) 456-7890"
    assert formatar_numero_telefone("9876543210") == "(987) 654-3210"
    assert formatar_numero_telefone("555-123-4567") == "(555) 123-4567"


def test_e_ano_bissexto():
    assert e_ano_bissexto(2020) == True
    assert e_ano_bissexto(2024) == True
    assert e_ano_bissexto(2021) == False
    assert e_ano_bissexto(1900) == False
    assert e_ano_bissexto(2000) == True

from datetime import date

def test_calcular_idade():
    data_nasc1 = date(2000, 5, 15)
    data_nasc2 = date(1995, 10, 1)
    data_nasc3 = date(1988, 3, 25)
    
    assert calcular_idade(data_nasc1) == 24
    assert calcular_idade(data_nasc2) == 28
    assert calcular_idade(data_nasc3) == 36

def test_area_circulo():
    assert area_circulo(6) == 113