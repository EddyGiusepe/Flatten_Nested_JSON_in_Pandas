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
