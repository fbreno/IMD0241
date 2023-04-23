from suds.client import Client

client = Client('http://localhost:8000/?wsdl')

while True:
    temperatura = input('Digite a temperatura: ')
    try:
        temperatura = int(temperatura)
        break
    except ValueError:
        print('Temperatura inválida')

while True:
    unidade_origem = input('Digite a unidade de origem(F ou C ou K): ')
    if unidade_origem in ["C", "F", "K"]:
        break
    else:
        print('Unidade inválida')
        
while True:
    unidade_destino = input('Digite a unidade de destino(F ou C ou K): ')
    if unidade_destino in ["C", "F", "K"]:
        break
    else:
        print('Unidade inválida')


response = client.service.converter_temperatura(temperatura, unidade_origem, unidade_destino)

print(response)