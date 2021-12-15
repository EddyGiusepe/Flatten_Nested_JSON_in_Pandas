'''
Data Scientist Jr.: Dr.Eddy Giusepe Chirinos Isidro
Este Script está baseado no link: https://www.kaggle.com/jboysen/quick-tutorial-flatten-nested-json-in-pandas/notebook
'''
# Importar nossas bibliotecas:
import json # JSON significa JavaScript Object Notation (Notação de Objecto JavaScript)
import pandas as pd
from pandas.io.json import json_normalize #pacote para achatar json em pandas df
# carregar objeto json
with open('raw_nyc_phil.json', 'r') as f:
    json_datos = json.load(f)
# Vamos colocar os dados em um pandas df
# Clique em raw_nyc_phil.json em "Arquivos de entrada"
# Nos diz que o nó pai é 'programs'
nycphil = json_normalize(json_datos['programs'])
print(nycphil.head(3))

# Também podemos fazer:
df_nycphil = pd.DataFrame(json_datos)
print(df_nycphil.head(5))
print(df_nycphil.shape)

'''
Vemos (pelo menos) duas colunas aninhadas, concerts e works. A documentação do Json_normalize nos dá algumas 
dicas de como nivelar ainda mais os dados semiestruturados. Vamos desempacotar a coluna works em um dataframe
independente. Também pegaremos as colunas planas para que possamos fazer análises. Os parâmetros aqui são um
pouco heterodoxos, veja se você consegue entender o que está acontecendo.

'''
works_data = json_normalize(data=json_datos['programs'], record_path='works',
                            meta=['id', 'orchestra','programID', 'season'])
print(works_data.head(3))
print(works_data.shape)

'''
Excelente!

* passou o caminho de dados do objeto json d[programs]
* passou o caminho do record dentro do objeto que queríamos parsear funciona
* passou os metadados pai que queríamos anexar

Sua vez: você pode descompactar os dados dos concerts?
'''

'''
Dados profundamente aninhados

E daí se você encontrar uma matriz aninhada dentro da sua matriz aninhada? Se você voltar e olhar para works_data achatados,
você pode ver uma segunda coluna aninhada, "soloists". Felizmente, os documentos json_normalize mostram que você pode passar
uma lista de colunas, em vez de uma única coluna, para o caminho do record para unflatten json profundamente aninhado.

Vamos flatten (achatar) os dados de 'soloists' aqui, passando uma lista. Uma vez que os soloists estão aninhados em works, podemos passar isso como:
'''

soloist_data = json_normalize(data=json_datos['programs'], record_path=['works', 'soloists'],
                              meta=['id'])
print(soloist_data.head(3))

























