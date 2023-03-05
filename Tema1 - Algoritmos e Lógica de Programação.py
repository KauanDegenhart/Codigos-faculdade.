print('Ana Maria recebeu seu salário e precisa pagar 2 contas que já venceram. '
      'Como as contas estão atrasadas, Ana Maria terá que pagar multa de 3% sobre cada conta.')
print('Informe o valor do salário')
salario = float(input())
print('Agora digite o valor da primeira conta')
conta1 = float(input())
print('Agora digite o valor da segunda conta')
conta2 = float(input())
x = 3 / 100
total1= x+conta1
total2= x+conta2
totaldascontas= total2+total1
print('O valor total das contas de Ana Maria, com os 3% de multa, será de',totaldascontas)
restodosalario= salario - totaldascontas
print('O valor que sobrará do seu salário após pagar suas contas será de',restodosalario)