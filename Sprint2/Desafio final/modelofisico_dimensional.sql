
CREATE VIEW dim_cliente AS
SELECT idlocacao,idcliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM cliente

CREATE VIEW dim_carro AS
SELECT idlocacao,idcarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro
FROM carro


CREATE VIEW dim_tempo AS
SELECT idlocacao, dataLocacao, horaLocacao, dataEntrega, horaEntrega
FROM tb_locacao,


CREATE VIEW fato_vendas AS
SELECT locacao.idlocacao AS idlocacao,
       carro.idcarro AS idcarro,
       locacao.idcombustivel AS idcombustivel,
       diaria.qtddiaria AS qtddiaria,
       diaria.vlrDiaria AS vlrDiaria
FROM locacao
LEFT JOIN diaria ON locacao.idlocacao = diaria.idlocacao
LEFT JOIN carro ON locacao.idcarro = carro.idcarro


select *
from dim_carro 

select *
from dim_cliente 

select *
from dim_tempo 

select *
from fato_vendas












