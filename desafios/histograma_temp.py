temperaturas = [] #ARMAZENAMENTO DAS TEMPERATURAS

for i in range(7): #PERCORRE TODOS OS DIAS DA SEMANA
    temperatura = int(input(f"Digite a temperatura do dia {i + 1}: ")) #ENTRADA PARA TEMPERATURA DE CADA DIA
    temperaturas.append(temperatura) #GUARDA A TEMPERATURA DE CADA DIA

for temperatura in temperaturas:
    histograma = '*' * temperatura #cRIA O hISTOGRAMA COM * DE ACORDO COM O NUMERO INFORMADO NA TEMPERATURA
    dia_semana = ['D', 'S', 'T', 'Q', 'Q', 'S', 'S'][temperaturas.index(temperatura)]
    print(f"{dia_semana}: {histograma}")