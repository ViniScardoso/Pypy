CREATE USER 'pypyUser'@'localhost' IDENTIFIED BY 'urubu100';
GRANT ALL PRIVILEGES ON pypy.* TO 'pypyUser'@'localhost';

CREATE DATABASE pypy;
USE pypy;

CREATE TABLE usuario(
	idUsuario INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(128),
    username VARCHAR(128) UNIQUE,
	senha VARCHAR(45),
    datanasc DATE
);

CREATE TABLE registro(
	idRegistro INT PRIMARY KEY AUTO_INCREMENT,
    peso DECIMAL(6,3),
    altura DECIMAL(3,2),
    imc DOUBLE,
    dataHoraReg DATETIME,
    fkUsuario int,
    foreign key(fkUsuario) references usuario(idUsuario)
);


SELECT * FROM usuario;
SELECT * FROM registro;

DROP TABLE usuario;
DROP TABLE registro;

-- Consulta o registro mais recente de cada usuário
SELECT * FROM registro INNER JOIN (SELECT MAX(dataHoraReg), fkUsuario FROM registro GROUP BY fkUsuario) AS dataSet GROUP BY registro.fkUsuario;

SELECT AVG(dataset.imc) FROM (SELECT peso, altura, imc, TIMESTAMPDIFF(YEAR,datanasc,MAX(dataHoraReg)) AS idade FROM registro JOIN usuario ON fkUsuario = 
idUsuario GROUP BY fkUsuario) AS dataset WHERE idade > 5; 

SELECT AVG(dataset.imc) FROM (SELECT peso, altura, imc, TIMESTAMPDIFF(YEAR,datanasc,MAX(dataHoraReg)) AS idade 
FROM registro JOIN usuario ON fkUsuario = idUsuario GROUP BY fkUsuario) AS dataset WHERE altura >= 1.6 AND altura < 1.7;

INSERT INTO usuario VALUES (NULL, 'vinicius', 'vini', MD5('123'), '2004-11-07');
