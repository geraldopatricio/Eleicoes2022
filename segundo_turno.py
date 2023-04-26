import requests
import json
import pandas as pd

data = requests.get(
    'https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json')

json_data = json.loads(data.content)

candidato = []
partido = []
votos = []
porcentagem = []

for informacoes in json_data['cand']:
    
    if int(informacoes['seq']) in range(1,12):
        candidato.append(informacoes['nm'])
        votos.append(informacoes['vap'])
        porcentagem.append(informacoes['pvap'])
        
df_eleicao = pd.DataFrame(list(zip(candidato, votos, porcentagem)), columns = [
    'Candidato', 'Nº de Votos', 'Porcentagem'
])

print(df_eleicao)
print(" ")
print("Porcentagem das Urnas Apuradas: " + json_data['pst'] + "%")