CREATE TABLE cliente (
  idlocacao INTEGER PRIMARY KEY AUTOINCREMENT,
  idcliente INT NOT NULL,
  nomeCliente VARCHAR(100) NOT NULL,
  cidadeCliente VARCHAR(100) NOT NULL,
  estadoCliente VARCHAR(50) NOT NULL,
  paisCliente VARCHAR(50) NOT NULL
);

INSERT INTO cliente (idcliente,nomecliente,cidadecliente,estadocliente,paiscliente)
SELECT DISTINCT idcliente,nomecliente,cidadecliente,estadocliente,paiscliente
FROM tb_locacao;

SELECT *
from cliente 




CREATE TABLE carro (
  idlocacao INTEGER PRIMARY KEY AUTOINCREMENT,
  idcarro INT NOT NULL,
  kmCarro VARCHAR(50),
  classiCarro VARCHAR(50),
  marcaCarro VARCHAR(100),
  modeloCarro VARCHAR(100),
  anoCarro INT,
  idcliente INT,
  FOREIGN KEY (idcliente) REFERENCES cliente(idcliente)
);


INSERT INTO carro (idcarro,kmcarro,classicarro,marcacarro,modelocarro,anocarro,idcliente)
SELECT DISTINCT  idcarro,kmcarro,classicarro,marcacarro,modelocarro,anocarro,idcliente
FROM tb_locacao;

SELECT *
from carro



CREATE TABLE combustivel (
  idcombustivel INTEGER PRIMARY KEY AUTOINCREMENT,
  tipoCombustivel VARCHAR(30) NOT NULL
);

INSERT INTO combustivel (idcombustivel,tipocombustivel)
SELECT DISTINCT idcombustivel, tipocombustivel
FROM tb_locacao;

SELECT *
from combustivel 



CREATE TABLE locacao (
  idlocacao INTeger PRIMARY KEY AUTOINCREMENT,
  idcarro INT,
  idcombustivel INT,
  dataLocacao DATE,
  horaLocacao TIME,
  FOREIGN KEY (idcarro) REFERENCES carro(idcarro),
  FOREIGN KEY (idcombustivel) REFERENCES combustivel(idcombustivel)
);

INSERT INTO locacao (idlocacao,idcarro,idcombustivel,datalocacao,horalocacao)
SELECT DISTINCT idlocacao,idcarro,idcombustivel,datalocacao,horalocacao
FROM tb_locacao;

SELECT *
from locacao


CREATE TABLE diaria (
  idlocacao INTeger PRIMARY KEY AUTOINCREMENT,
  idcarro INT,
  qtddiaria INT,
  vlrDiaria DECIMAL(10, 2) NOT NULL,
  FOREIGN KEY (idcarro) REFERENCES carro(idcarro)
);

INSERT INTO DIARIA (idcarro,qtddiaria,VlrDiaria)
SELECT DISTINCT idcarro,qtddiaria,vlrDiaria
FROM tb_locacao;

SELECT *
from diaria 


CREATE TABLE entrega (
  idlocacao INTEGER PRIMARY KEY AUTOINCREMENT,
dataEntrega DATE,
  horaEntrega TIME,
  FOREIGN KEY (idlocacao) REFERENCES locacao(idlocacao)
);

INSERT INTO entrega (dataentrega,horaentrega)
SELECT DISTINCT dataentrega,horaentrega
FROM tb_locacao;

SELECT *
from entrega




CREATE TABLE vendedor (
  idlocacao INTEGER PRIMARY KEY AUTOINCREMENT,
  idcarro INT,
  idvendedor INT,
  nomeVendedor VARCHAR(100) NOT NULL,
  sexoVendedor VARCHAR(100) NOT NULL,
  estadoVendedor VARCHAR(100) NOT NULL,
  FOREIGN KEY (idcarro) REFERENCES carro(idcarro)
);


INSERT INTO vendedor (idcarro,idvendedor,nomevendedor,sexovendedor,estadovendedor)
SELECT DISTINCT idcarro,idvendedor,nomevendedor,sexovendedor,estadovendedor
FROM tb_locacao;

SELECT *
from vendedor 


