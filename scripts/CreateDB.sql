CREATE database temakitech;

USE temakitech;

/* INSERIDO o AUTO_INCREMENT */
CREATE TABLE Usuario (
    Id integer primary key AUTO_INCREMENT,
    usuario varchar(30) not null,
    senha varchar(80) not null,
    nome varchar (50),
    sobrenome varchar(100),
    data_nascimento date,
    endereco varchar(80),
    cidade varchar(40),
    estado char(2),
    data_criacao date,
    data_modificacao date
);

/* INSERIDO o AUTO_INCREMENT */
create table Categoria(
	id integer primary key AUTO_INCREMENT,
    nome varchar(30)
);

/* INSERIDO o AUTO_INCREMENT */
CREATE TABLE Produto(
	id integer primary key AUTO_INCREMENT,
    id_categoria integer,
    nome varchar(60),
    detalhe varchar(200),
    preco decimal(15,2),
    FOREIGN KEY(id_categoria) REFERENCES Categoria(id)
);

/* INSERIDO o AUTO_INCREMENT */
CREATE TABLE Status_pedido (
    id integer primary key,
    status varchar(30) not null
    );

CREATE TABLE Pedido (
    Id integer primary key AUTO_INCREMENT,
    id_auxproduto integer,
    id_usuario integer,
    quantidade integer,
    id_status integer,
    valor_total decimal(15,2),
    FOREIGN KEY(id_usuario) REFERENCES Usuario(id),
    FOREIGN KEY(id_status) REFERENCES Status_pedido(id)
);

CREATE TABLE Aux_produto(
	id        integer primary key auto_increment,
	id_pedido integer ,
	id_produto integer not null,
    quantidade int,
    FOREIGN KEY(id_produto) REFERENCES Produto(id),
    FOREIGN KEY(id_pedido) REFERENCES Pedido(id)
    );

/* Tabela nova*/

