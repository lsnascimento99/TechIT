CREATE database temakitech;

USE temakitech;

/* INSERIDO o AUTO_INCREMENT */
CREATE TABLE Usuarios (
    Id integer primary key AUTO_INCREMENT,
    usuario varchar(30) not null,
    senha varchar(80) not null,
    data_criacao date,
    data_modificacao date
);

CREATE TABLE Clientes (
	id integer,
    nome varchar (50),
    sobrenome varchar(100),
    idade integer,
    endereco varchar(80) not null,
    cidade varchar(40) not null,
    estado char(2) not null,
    FOREIGN KEY(id) REFERENCES usuarios(id)
    
);

/* INSERIDO o AUTO_INCREMENT */
create table Classificacao(
	id integer primary key AUTO_INCREMENT,
    nome varchar(30)
);

/* INSERIDO o AUTO_INCREMENT */
CREATE TABLE Servicos(
	id integer primary key AUTO_INCREMENT,
    id_classificacao integer,
    nome varchar(60),
    detalhe varchar(200),
    preco decimal(15,2),
    FOREIGN KEY(id_classificacao) REFERENCES Classificacao(id)
);

/* INSERIDO o AUTO_INCREMENT */
CREATE TABLE Status_pedido (
    id integer primary key,
    status varchar(30) not null
    );

CREATE TABLE Pedidos (
    Id integer primary key AUTO_INCREMENT,
    id_servico integer,
    id_usuario integer,
    quantidade integer,
    id_status integer,
    valor_total decimal(15,2),
    FOREIGN KEY(id_servico) REFERENCES Servicos(id),
    FOREIGN KEY(id_usuario) REFERENCES Usuarios(id),
    FOREIGN KEY(id_status) REFERENCES Status_pedido(id)
);


