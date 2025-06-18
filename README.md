# CRUD com Python e SQLite3
Criação de tabela com SQLite3 e aplicação CRUD em Python, aqui você pode entender como fiz:

Contexto: Regra de Negócio, demandas e clientes.

Baixei o SQLite para utilizar no meu PC Windows.
Criei um diretório DTI_case na minha máquina, descompactei a pasta com os arquivos do SQLite e transferi para o diretório criado.
No meu IDE pessoal, abri o diretório e criei um banco de dados produtos.db, após isso, entrei no banco de dados e comecei a escrever meu script SQL utilizando o acesso ao “terminal” do banco de dados.
Criei uma tabela clientes e configurei suas colunas, campos obrigatórios, campos opcionais e tipos de dados sendo: id Primary Key, Empresa Text Not Null, Demanda Text Not Null, Vencimento Text.
As empresas que utilizei foram: Banco Inter, Gerdau e MRV; com suas respectivas demandas em ordem: atualização e integração de sistemas legados, página web e aplicação mobile. Como havia dito anteriormente, são demandas fictícias, apenas representando o contexto de atuação.
Criando e testando cada item da tabela clientes via terminal, um a um de forma individual.
Após criar a tabela clientes e inserir seus demais dados e informações, instalei a extensão disponível no VScode(extensão utilizada), chamada SQLite para uma experiência mais “amigável”. Utilizo a Paleta de Comandos e uma nova Query para visualizar a tabela criada, literalmente em uma tabela.
Feito isso, crio um arquivo Python e o nomeio de produtos_connect.py inicialmente começo meu código utilizando o terminal, verifico a versão do Python, e importo a biblioteca SQLite, já nativa da linguagem. Realizo um teste de ambiente com o comando print.
Crio um Ambiente Virtual utilizando o python -m venv, para que não corra o risco da aplicação se misturar com outras aplicações já criadas por mim anteriormente. Em seguida entro dentro do Arquivo produtos_connect.py.
Importo a biblioteca para o início do código, para que não haja a necessidade de iniciar pelo terminal novamente, sempre que for fechada a aplicação. Em seguida crio uma variável e atribuiu a ela a conexão ao banco de dados; crio um cursor para executar comandos SQL na tabela. Em seguida, o CRUD.

Observação: Para melhor entendimento e proveito, recomendo seguir os passos conforme relatados. Para que assim, a aplicação funcione 100%. Para isso, recomendo utilizar:

Criar Diretório
Baixar arquivos SQLite
Usar o VScode 
Python 3.12.4 
Instalar a extensão SQLite
Instalar o SQLite 3.47.2

Desenvolvimento:

Inicialmente criei um diretório na minha máquina, e o nomeei de “DTI_case”. Após isso, instalei na minha máquina o banco de dados SQLite3, através da página downloads, no site oficial: https://www.sqlite.org/download.html
Procurei pela versão feita para o windows, pois a máquina que utilizei no momento em que estava desenvolvendo a aplicação possui SO Windows. Em seguida fiz a instalação do arquivo:  sqlite-tools-win-x64-3470200.zip 
Após concluir o download, o encaminho para o diretório criado anteriormente “DTI_case”. Extraio os arquivos, pois estão compactados como: sqlite-tools-win-x64-3470200.zip.
Seguindo, é necessário possuir um IDE, um ambiente de Desenvolvimento Integrado. No meu caso utilizei o VScode. Após isso abro o diretório “DTI_case” na aba “File” dentro do IDE na opção New Folder. Dentro do VScode acesso o PowerShell e executei o comando .\sqlite3 produtos.db (utilizei o “.\” para realizar um by-pass para permissões), e o comando entra no terminal do banco de dados, que está dentro do diretório e então começa meu script SQL. Veja o terminal:
Script SQL

Observação: Para melhor ilustração dos comandos no terminal, vou utilizar IN para representar input, ou seja, meus comandos. E para as respostas utilizamos OUT, de output, que são as saídas para os comandos do Banco de Dados.

Dentro do diretório “DTI_case>” use o comando .\sqlite3 produtos.db:
IN: DTI_case>.\sqlite3 produtos.db

O terminal responde com a versão do SQLite e entra automaticamente no terminal do banco de dados, onde nos possibilita utilizar comandos CREATE, SELECT, DELETE…
OUT: SQLite version 3.47.2 2024-12-07 20:39:59
Enter ".help" for usage hints.
sqlite> 

Aqui utilizo o comando CREATE + TABLE para criar a tabela clientes e configurar suas colunas:
IN:sqlite> create table clientes (id Integer Primary Key, Empresa Text Not Null, Demanda Text Not Null, Vencimento Text);

Aqui irei inserir os primeiros valores a tabela conforme classifiquei as colunas anteriormente:
IN:sqlite> insert into clientes values(1, 'banco inter', 'autualizacao e integracao de sistemas legados', '2025-12-30');

Nesse trecho utilizo o comando Select + * + From + Tabela. O comando “select” é bem intuitivo ele seleciona algo, junto ao “ * ” que tem a função de orientação a todos os dados. O From informa a qual tabela deve ser feito, então basicamente, falando de forma crua o comando funcione como: “selecione tudo da tabela”. Veja na prática como foi feito: 
IN: sqlite> select * from clientes;

É retornado os valores que atribui anteriormente com o Insert Into:
OUT: 1|banco inter|autualizacao e integracao de sistemas legados|2025-12-30

Assim se repete o processo nas outras duas empresas:

IN:sqlite> insert into clientes values(2,'gerdau', 'pagina web', '2025-04-22'); 
IN: sqlite> select * from clientes;

OUT: 1|banco inter|autualizacao e integracao de sistemas legados|2025-12-30
2|gerdau|pagina web|2025-04-22

IN:sqlite> insert into clientes values(3, 'mrv', 'aplicativo mobile', '2025-11-09');
IN:sqlite> select * from clientes;

OUT:
1|banco inter|autualizacao e integracao de sistemas legados|2025-12-30
2|gerdau|pagina web|2025-04-22
3|mrv|aplicativo mobile|2025-11-09

Agora utilizo o Ctrl + Z para sair do terminal do SQLite3
IN: sqlite> Ctrl + Z + enter 
OUT: retorna para fora do SQLite3

Extensão

Para tornar a experiência mais amigável ao usuário, instale a extensão que está disponível dentro do VScode, chamada SQLite com ícone de uma “pena” com fundo azul do autor alexcvzz. Após a instalação, conseguimos visualizar de forma literal a tabela “clientes” utilizando a extensão em conjunto a paleta de comandos. exemplo:

Utilize o atalho Ctrl + Shift + P. Após o comando, pesquise SQLite: Open Database, será necessário selecionar onde está localizado o banco de dados na pasta atual. Se você tiver nomeado seu banco de dados como “produtos.db” como eu orientei anteriormente basta selecionar ele e estará visível em uma aba SQLITE EXPLORER para expandir o banco de dados e visualizar a tabela clientes. Ao visualizar a tabela, clique no botão que representa um play e será mostrado a tabela “clientes”, com os dados e informações que adicionamos anteriormente.

Há também outra maneira de visualizar a tabela utilizando também a paleta de comandos. Utilize o Ctrl + Shift + P e busque por SQLite: New Query, será aberto um arquivo de texto que possibilita o uso de comandos SQL. Para ver a tabela basta escrever esse script:

1      - - SQLite (essa parte não é necessária ser escrita)
2      Select * From clientes

Em seguida use o atalho Ctrl + Shift + Q para executar a Query. A partir da linha 2, você pode utilizar os comandos SQL. Exemplos de comandos são:

Select - seleciona dados;
Update - adiciona dados;
Delete - exclui dados;
From - direciona onde realizar comandos;

Relembrando:
O “ * ” no comando, é para indicar a seleção para todos os dados dentro da tabela.
O From direciona a qual tabela estamos enviando comandos.

Script com Python

Crio um ambiente virtual em com: python -m venv venv para não entrar em conflito com outros arquivos internos.

Vou a New File no IDE e crio o arquivo produtos_connect.py, abro o terminal, e verifico se o interpretador Python está ativo e qual sua versão. Após isso importo a biblioteca SQLite, veja o trecho retirado do código:

#Importo a biblioteca para não ser necessário iniciar por terminal:
import sqlite3


Crio uma variável com a abreviação de “connect”, e atribuo a ela a função de se conectar ao banco de dados utilizando o “connect”. Confira o trecho retirado do código:

#Crio uma variável e atribuo a ela a função de se conectar ao Banco de Dados:
conn = sqlite3.connect("produtos.db")

Agora, um cursor para executar comandos SQL junto a essa conexão, ele vai funcionar como um guia. Código:

#Criando cursor, que utilizo para realizar comandos SQL junto a variável que se conecta ao Banco de Dados: 
cur = conn.cursor()

Importações e Conexão ao Banco de Dados
Começo importando a biblioteca sqlite3, o que me permite trabalhar diretamente com bancos de dados SQLite no meu código Python, sem precisar abrir o terminal a cada vez. Em seguida, crio uma variável conn que estabelece a conexão direta com o banco de dados produtos.db. Para facilitar a execução de comandos SQL, também crio um cursor cur.

Experiência do Usuário
Para tornar a experiência do usuário mais intuitiva, construí um menu interativo. Usei print para mostrar as opções disponíveis, input para coletar as respostas do usuário, e algumas variáveis para armazenar essas respostas.

No início do código, utilizo um loop while para manter o programa rodando continuamente. Esse loop exibe repetidamente o menu de opções até que o usuário decida sair. Isso permite que o usuário realize várias operações sem precisar reiniciar o programa.

Estrutura de Condicionais
A lógica do programa é controlada por estruturas condicionais if, elif e else:

if: Verifico se uma condição é verdadeira e executo o bloco de código correspondente.
elif: Permito verificar várias condições adicionais se as anteriores não forem verdadeiras.
else: Executo um bloco de código se nenhuma das condições anteriores for verdadeira.
Essas condicionais são usadas para diferentes operações:

Ver todos os dados: Consulto e exibo todos os registros da tabela clientes.
Ver um dado específico: Permito ao usuário consultar dados de uma empresa específica.
Atualizar um dado: Permito ao usuário atualizar informações de um cliente específico.
Deletar um dado: Permito ao usuário deletar um registro específico da tabela clientes.
Sair: Encerro o programa.
Encerramento da Conexão
Se o usuário escolher sair do programa, o loop while é interrompido e a conexão com o banco de dados é encerrada. Isso é feito para garantir que todos os recursos sejam liberados corretamente, evitando problemas de conexão e mantendo a integridade dos dados.



