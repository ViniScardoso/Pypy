CREATE USER 'pypyUser'@'localhost' IDENTIFIED BY 'urubu100';
GRANT ALL PRIVILEGES ON pypy.* TO 'pypyUser'@'localhost';

CREATE DATABASE pypy;
USE pypy;

CREATE TABLE usuario(
	idUsuario INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(128),
    username VARCHAR(128),
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

INSERT INTO usuario VALUES (NULL ,'Leo', 'leovasc', 54.0, 421.0, 0.0, '2003-11-02');

SELECT * FROM usuario;

drop table usuario;

