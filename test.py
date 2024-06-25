from main import *

#TESTA SE A FRASE POSSUI TODAS AS LETRAS DO ALFABETO
def test_is_pangram():
    assert is_pangram("Gazeta publica hoje crítica de filme que venceu o Oscar.") == True
    assert is_pangram("Jovem exibe foto de balão azul que caiu em uma praça vazia.") == True
    assert is_pangram("OLa Mundo") == False

#FORMATA A STRING PARA O FORMATO DE TELEFONE AMERICANO
def test_format_phone_number():
    assert format_phone_number("1234567890") == "(123) 456-7890"
    assert format_phone_number("9876543210") == "(987) 654-3210"
    assert format_phone_number("555-123-4567") == "(555) 123-4567"

#VERIFICA SE O ANO É BISSEXTO
def test_is_leap_year():
    assert is_leap_year(2020) == True
    assert is_leap_year(2024) == True
    assert is_leap_year(2021) == False
    assert is_leap_year(1900) == False
    assert is_leap_year(2000) == True

from datetime import date
#CALCULA A IDADE RECEBENDO A DATA DE NASCIMENTO
def test_calculate_age():
    birth_date1 = date(2000, 5, 15)
    birth_date2 = date(1995, 10, 1)
    birth_date3 = date(1988, 3, 25)
    
    assert calculate_age(birth_date1) == 24
    assert calculate_age(birth_date2) == 28
    assert calculate_age(birth_date3) == 36
    
#CALCULA A AREA DE UM CIRCULO
def test_area_circle():
    assert area_circulo(6) == 113
    assert area_circulo(13) == 530
    assert area_circulo(17) == 113