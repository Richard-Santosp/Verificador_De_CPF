import string
import os
os.system('cls')

# Entrada do CPF e padronização dos digitos
cpf = input('Digite seu CPF: ')
cpf = cpf.translate(str.maketrans('','', string.punctuation))

# Verificações dos digitos informados 
if len(cpf) < 11 or len(cpf) > 11:
    print('Quantidade de digitos esta incorreta')
    exit()

if len(set(cpf)) == 1:
    print('Um CPF não possui todos os caracteres iguais')
    exit()

# Obtenção do primeiro digito
numeros_cpf_multiplicados = []
contagem_regressiva = 10
for i in cpf[:9]:
    try:
        numero_multiplicado = int(i)*contagem_regressiva
        numeros_cpf_multiplicados.append(numero_multiplicado)
        contagem_regressiva -= 1
    except ValueError:
        print('Valor do CPF é invalido')
        exit()

possivel_digito = sum(numeros_cpf_multiplicados) * 10 % 11

primeiro_digito = 0 if possivel_digito > 9 else possivel_digito
print(f'O primeiro digito é: {primeiro_digito}')

# obtenção do segundo digito
numeros_cpf_multiplicados2 = []
contagem_regressiva2 = 11
for n in cpf[:10]:
    try:
        numero_multiplicado = int(n)*contagem_regressiva2
    except ValueError:
        print('Valor do CPF é invalido')
        exit()
    numeros_cpf_multiplicados2.append(numero_multiplicado)
    contagem_regressiva2 -= 1

segundo_digito = 0 if (sum(numeros_cpf_multiplicados2) * 10) % 11 > 9 else (sum(numeros_cpf_multiplicados2) * 10) % 11
print(f'O segundo digito é {segundo_digito}')

#Verificando se o CPF é valido 
if primeiro_digito == int(cpf[9]) and segundo_digito == int(cpf[10]):
    print('CPF correto')
else:
    print('CPF incorreto')

