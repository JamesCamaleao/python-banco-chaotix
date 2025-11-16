#Plano
def recomendar_plano (consumo):
    if consumo <= 10:
        return "O plano recomendado para você é o Plano Essencial Fibra - 50Mbps"
    elif consumo <= 20:
        return "O plano recomendado para você é o Plano Prata Fibra - 100Mbps" 
    else:
        return "O plano recomendado para você é o Plano Premium Fibra - 300Mbps"
    
consumo = float(input("""Seja bem-vindo, para podermos recomendar
o melhor plano para você diga, 
qual seu consumo medio mensal em GB?"""))

print(recomendar_plano(consumo))

#Equipamentos 

itens = []

for iten in range(3):
    equipamento = input()
    itens.append(equipamento)

print("Lista de Equipamentos:")  
for item in itens:
    print(f"- {item}")

#Telefones

import re
pattern = r'^\(\d{2}\)\s9\d{4}-\d{4}$'

def validate_numero_telefone(phone_number):

    if re.match(pattern, phone_number):  
        return "Número de telefone válido."
    else:
        return "Número de telefone inválido."
phone_number = input() 

result = validate_numero_telefone(phone_number)
print(result)