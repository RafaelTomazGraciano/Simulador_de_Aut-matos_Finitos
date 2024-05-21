import json
import csv
import time
import sys

if len(sys.argv) != 4:
    print("Use: python main.py arquivo_do_automato.aut arquivo_de_testes.in arquivo_de_saida.out")
    sys.exit(1)

def delta(q, a, transicoes):
    resultados = []
    for transicao in  transicoes:
        if transicao['from'] == q and transicao['read'] == a:
            resultados.append(transicao['to'])
    return resultados
    

#inicia contar o tempo
inicio_tempo = time.perf_counter()

# Lendo JSON
arquivo_json = open(sys.argv[1])
 
# retorna o JSON 
dadosJson = json.load(arquivo_json)
#salvando dados
estadoInicial = dadosJson['initial']
estadoFinal = dadosJson['final']
transicoes = dadosJson['transitions']



with open(sys.argv[3], 'w', newline='') as arquivo_out: #criando arquivo out
    with open(sys.argv[2], 'r') as arquivo_in: #lendo arquivo in
        leitor = csv.reader(arquivo_in, delimiter = ';')
        for linha in leitor:
            estadosAtuais = [estadoInicial]
            palavra = linha[0]
            caracteres = list(palavra)
            print(caracteres)
            estados = []
            for caractere in caracteres:
                novos_estados = []
                for estado_atual in estadosAtuais:
                    novos_estados.extend(delta(estado_atual, caractere, transicoes))
                estadosAtuais = novos_estados
                estados.append(estadosAtuais)
                print(estados)
                print('q' + str(estadosAtuais) + ' - ' + caractere)
                if estadosAtuais == -1:
                    break
            print(estadosAtuais)
            for estado in estados:    
                if estadoFinal in estado:
                    resultado_obtido = 1
                    break
                else:
                    resultado_obtido = 0
            #Escrevendo arquivo out
            escritor = csv.writer(arquivo_out, delimiter = ';')
            fim_tempo = time.perf_counter()
            tempo = fim_tempo - inicio_tempo
            escritor.writerow([linha[0], linha[1], resultado_obtido, tempo])     
    
