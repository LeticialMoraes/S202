CREATE TABLE estoque(
	id BIGINT,
	nome TEXT,
	carro TEXT,
	estante INT,
	nivel INT,
	quantidade BIGINT,
	PRIMARY KEY((id, estante, nivel),carro,nome)
);

INSERT INTO estoque(id,nome,carro,estante,nivel,quantidade) VALUES(5,'Pistao','Mustang',4,1,167);
INSERT INTO estoque(id,nome,carro,estante,nivel,quantidade) VALUES(4,'Suspencao',Argo,1,1,3500);

SELECT id,carro,estante,nivel,quantidade FROM estoque WHERE nome = 'Pistao';

-- Calcula a média aritmética da quantidade de todas as colunas armazenadas na tabela
SELECT AVG(quantidade) AS media_quantidade FROM estoque;

-- Retorna a quantidade de colunas armazenadas na tabela
SELECT COUNT(*) AS total_colunas FROM estoque;

-- Retorna a maior e a menor quantidade de peças
SELECT MAX(quantidade) AS "maior quantidade", MIN(quantidade) AS "menor quantidade" FROM estoque;

-- Retorna os atributos nome, carro e quantidade onde a estante é igual a 3
SELECT nome, carro, quantidade FROM estoque WHERE estante = 3;

-- Retorna a média aritmética da quantidade onde o nível é igual a 1
SELECT AVG(quantidade) AS media_quantidade_nivel_1 FROM estoque WHERE nível = 1;

-- Retorna todos os atributos onde a estante é menor que 3 e o nível é maior que 4
SELECT * FROM estoque WHERE estante < 3 AND nível > 4;
