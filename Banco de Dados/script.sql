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
    altura DECIMAL(3,2),
    imc DOUBLE,
    dataHoraReg DATETIME,
    fkUsuario int,
    foreign key(fkUsuario) references usuario(idUsuario)
);


SELECT * FROM usuario;
SELECT * FROM registro;

drop table usuario;
drop table registro;

