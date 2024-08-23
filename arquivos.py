import csv

caminho: str = 'arquivo_exemplo.csv'

lista: list = []

with open(file= caminho, mode="r", encoding='UTF-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    for linha in leitor_csv:
        lista.append(linha)

print(lista)