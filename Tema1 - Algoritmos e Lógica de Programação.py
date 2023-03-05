print('Ana Maria recebeu seu salário e precisa pagar 2 contas que já venceram. '
      'Como as contas estão atrasadas, Ana Maria terá que pagar multa de 3% sobre cada conta.')
print('Informe o valor do salário')
salario = float(input())
print('Agora digite o valor da primeira conta')
conta1 = float(input())
print('Agora digite o valor da segunda conta')
conta2 = float(input())
total1= conta1 * 3 / 100 + conta1
print('total da primeira conta com os juros de 3%, R$',total1)
total2= conta2 * 3 / 100 + conta2
print('total da segunda conta com os juros de 3%, R$',total2)
totaldascontas= total1+total2
print('O valor total das contas de Ana Maria, com os 3% de multa, será de, R$',totaldascontas)
restodosalario= salario - totaldascontas
print('O valor que sobrará do seu salário após pagar suas contas será de, R$',restodosalario)