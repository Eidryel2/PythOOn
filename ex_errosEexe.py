def calcular_media(valores):
    tamanho = len(valores) 
    soma = 0.0
    for valor in valores:
        soma += valor
    media = soma / tamanho
    return media  

valores = []
while True:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor: ')
    if valor.lower() == 'ok':
        break
    valores.append(float(valor))

media = calcular_media(valores)
print('A média calculada para os valores {} foi de {}'.format(valores, media))
