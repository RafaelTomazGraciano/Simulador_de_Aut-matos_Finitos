import json
import csv
import time
import sys


def delta(q, a, transicoes):
    for transicao in  transicoes:
        if transicao['from'] == q and transicao['read'] == a:
            return transicao['to']
    return -1;
    

#inicia contar o tempo
inicio_tempo = time.perf_counter()

# Lendo JSON
arquivo_json = open("arquivo_do_automato.aut")#sys.argv[1]
 
# retorna o JSON 
dadosJson = json.load(arquivo_json)
#salvando dados
estadoInicial = dadosJson['initial']
estadoFinal = dadosJson['final']
transicoes = dadosJson['transitions']

 


with open('arquivo_de_saida.out', 'w') as arquivo_out: #criando arquivo out
    with open('arquivo_de_testes.in', 'r') as arquivo_in: #lendo arquivo in
        leitor = csv.reader(arquivo_in, delimiter = ';')
        for linha in leitor:
            estadoAtual = estadoInicial
            palavra = linha[0]
            caracteres = list(palavra)
            print(caracteres)
            for caractere in caracteres:
                estadoAtual = delta(estadoAtual, caractere, transicoes)
                print('q' + str(estadoAtual) + ' - ' + caractere)
                if estadoAtual == -1:
                    break
            print(estadoAtual)    
            if estadoAtual == estadoFinal:
                resultado_obtido = 1
            else:
                resultado_obtido = 0
            #Escrevendo arquivo out
            escritor = csv.writer(arquivo_out, delimiter = ';')
            fim_tempo = time.perf_counter()
            tempo = fim_tempo - inicio_tempo
            escritor.writerow([linha[0], linha[1], resultado_obtido, tempo])     
    
