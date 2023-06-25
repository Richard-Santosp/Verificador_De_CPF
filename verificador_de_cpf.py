import string
import os
os.system('cls')

cpf = '111.111.111.12'
cpf = cpf.translate(str.maketrans('','', string.punctuation))

if len(cpf) < 11 or len(cpf) > 11:
    print('Quantidade de digitos esta incorreta')
    exit()

#digito um
numeros_cpf_multiplicados = []
contagem_regressiva = 10
for i in cpf[:9]:
    try:
        numero_multiplicado = (int(i)*contagem_regressiva)
    except ValueError:
        print('Valor do CPF é invalido')
        exit()
    numeros_cpf_multiplicados.append(numero_multiplicado)
    contagem_regressiva -= 1

primeiro_digito = 0 if (sum(numeros_cpf_multiplicados) * 10) % 11 > 9 else (sum(numeros_cpf_multiplicados) * 10) % 11
print(f'O primeiro digito é: {primeiro_digito}')

#digito dois
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

#Verificação de CPF
if primeiro_digito == int(cpf[9]) and segundo_digito == int(cpf[10]):
    print('CPF correto')
else:
    print('CPF incorreto')

