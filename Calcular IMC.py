print ("Bem vindo a Calculadora de IMC")

def calcular_imc(peso, altura):
    # Fórmula do IMC: IMC = peso / (altura^2)
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade Inicial"
    elif 35 <= imc < 39.9:
        return "Obesidade Avançada"
    else:
        return "Obesidade Mórbida"

while True:
    nome = input("Digite seu nome: ")
    idade = int(input("Idade: "))
    peso = float(input("Peso (em KG): "))
    altura = float(input("Altura (em metros e use ponto): "))
    print("Calculando seu IMC")

    # Calcular o IMC
    imc = calcular_imc(peso, altura)

    # Classificar o IMC
    classificacao = classificar_imc(imc)

    # Resultado
    print(f"Olá, {nome}! Seu IMC é {imc:.2f} e você está classificado como '{classificacao}'.")

    repetir = input("Deseja calcular o IMC novamente? (Sim/Nao): ")
    if repetir.lower() != 'Sim':
        break
