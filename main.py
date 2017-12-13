from datetime import datetime

agora = datetime.now()

dia = agora.day
mes = agora.month
ano = agora.year
hora = agora.hour
minuto = agora.minute
segundo = agora.second

diaNascimento = int(input("Informe o seu dia de nascimento: "))
mesNascimento = int(input("Informe o seu mês de nascimento: "))
anoNascimento = int(input("Informe o seu ano de nascimento: "))
dataNascimento = datetime(anoNascimento, mesNascimento, diaNascimento)

print(dataNascimento)

# print("{:02d}/{:02d}/{:04d} - {}:{}'{}\"".format(dia, mes, ano, hora, minuto, segundo))
