import string

#TESTA SE A FRASE POSSUI TODAS AS LETRAS DO ALFABETO
def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    return set(sentence.lower()) >= alphabet

#FORMATA A STRING PARA O FORMATO DE TELEFONE
def format_phone_number(number):
    cleaned = ''.join([c for c in number if c.isdigit()])
    return f'({cleaned[:3]}) {cleaned[3:6]}-{cleaned[6:]}'


#VERIFICA SE O ANO É BISSEXTO
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

from datetime import date

#CALCULA A IDADE RECEBENDO A DATA DE NASCIMENTO
def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

#CALCULA A AREA DE UM CIRCULO
def area_circulo(raio):
    area = 3.1415 * raio ** 2 
    return round(area)