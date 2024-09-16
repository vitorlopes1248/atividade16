# Crie um programa que receba o peso e a altura de uma pessoa e calcule o Índice de Massa Corporal (IMC). O programa deve classificar o IMC da pessoa de acordo com a tabela a seguir:
# Abaixo do peso: IMC < 18.5
# Peso normal: 18.5 ≤ IMC < 25
# Sobrepeso: 25 ≤ IMC < 30
# Obesidade: IMC ≥ 30

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)

# Abaixo do peso: IMC < 18.5
if (imc < 18.5):
    print("Abaixo do Peso")

# Peso normal: 18.5 ≤ IMC < 25
elif (18.5 <= imc < 25):
    print("Peso Normal")  

# Sobrepeso: 25 ≤ IMC < 30
elif (25 <= imc < 30):
    print("Você está com sobrepeso")

# Obesidade: IMC ≥ 30
elif (imc >= 30):
    print("Obesidade")
