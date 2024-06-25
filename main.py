import string

#TESTA SE A FRASE POSSUI TODAS AS LETRAS DO ALFABETO
def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    return set(sentence.lower()) >= alphabet

#FORMATA A STRING PARA O FORMATO DE TELEFONE
def formatar_numero_telefone(number):
    formatado = ''.join([c for c in number if c.isdigit()])
    return f'({formatado[:3]}) {formatado[3:6]}-{formatado[6:]}'


#VERIFICA SE O ANO É BISSEXTO
def e_ano_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

from datetime import date

#CALCULA A IDADE RECEBENDO A DATA DE NASCIMENTO
def calcular_idade(data_nasc):
    today = date.today()
    idade = today.year - data_nasc.year - ((today.month, today.day) < (data_nasc.month, data_nasc.day))
    return idade

#CALCULA A AREA DE UM CIRCULO
def area_circulo(raio):
    area = 3.1415 * raio ** 2 
    return round(area)