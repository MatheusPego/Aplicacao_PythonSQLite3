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
