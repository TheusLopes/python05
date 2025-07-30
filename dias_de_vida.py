from datetime import datetime

data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")

data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")

data_atual = datetime.now()

dias_vivo = (data_atual - data_nascimento).days

print(f"Você está vivo há {dias_vivo} dias.")