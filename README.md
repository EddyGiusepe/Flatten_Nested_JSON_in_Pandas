# Data Scientist Jr.: Dr.Eddy Giusepe Chirinos Isidro
Este estudo está baseado no seguinte Tutorial do Kaggle: https://www.kaggle.com/jboysen/quick-tutorial-flatten-nested-json-in-pandas/notebook.
Neste link você pode descargar os Dados necessários para rodar o Script.

## Flatten Nested JSON in Pandas
### Contexto (About this DataSet):
A New York Philharmonic fez seu primeiro concerto em 7 de dezembro de 1842.
Desde então, ela se fundiu com a New York Symphony, a New/National Symphony, e teve uma longa
temporada de verão no Lewisohn Stadium em Nova York. O banco de dados do histórico de desempenho
documenta todos os shows conhecidos de todas essas organizações, totalizando mais de 20000 apresentações.

### Conteúdo:
O conjunto de dados é um único <font color="yellow">csv</font> com mais de 800 mil linhas. Os dados
contêm informações sobre temporada, orquestra, local (lugar), data, hora, maestro (conductor), título
da obra, compositor, movimento e solistas.

### Agradecimentos:
Este conjunto de dados foi compilado pela **New York Philharmonic**. Arquivos json originais hospedados
aqui. Os arquivos json originais foram nivelados e unidos no guid para formar um único arquivo csv.
Imagem cortesia de Larisa Birta.

## <font color="red">Parsing Nested JSON with Pandas</font> 
Aqui vamos a parsear (analisar) arquivos JSON aninhados. Então, neste estudo vamos achatar (flatten) e
carregar no ``Pandas``.  Segundo recomendado (neste tutorial Kaggle), seguiremos os seguintes passos:

* Usamos o aninhado <font color="yellow">"raw_nyc_phil.json"</font> para criar um DataFrame Pandas
achatado a partir de um array aninhado.
* Você achata outra array (matriz).
* Descompactamos uma matriz (array) profundamente aninhada.


Thanks God!
