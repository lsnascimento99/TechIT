CREATE TABLE `aux_produto` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_pedido` int DEFAULT NULL,
  `id_produto` int NOT NULL,
  `quantidade` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_produto` (`id_produto`),
  KEY `id_pedido` (`id_pedido`),
  CONSTRAINT `aux_produto_ibfk_1` FOREIGN KEY (`id_produto`) REFERENCES `produto` (`id`),
  CONSTRAINT `aux_produto_ibfk_2` FOREIGN KEY (`id_pedido`) REFERENCES `pedido` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `categoria` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `pedido` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `id_auxproduto` int DEFAULT NULL,
  `id_usuario` int DEFAULT NULL,
  `quantidade` int DEFAULT NULL,
  `id_status` int DEFAULT NULL,
  `valor_total` decimal(15,2) DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `id_usuario` (`id_usuario`),
  KEY `id_status` (`id_status`),
  CONSTRAINT `pedido_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`Id`),
  CONSTRAINT `pedido_ibfk_2` FOREIGN KEY (`id_status`) REFERENCES `status_pedido` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `produto` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_categoria` int DEFAULT NULL,
  `nome` varchar(60) DEFAULT NULL,
  `detalhe` varchar(200) DEFAULT NULL,
  `preco` decimal(15,2) DEFAULT NULL,
  `img` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_categoria` (`id_categoria`),
  CONSTRAINT `produto_ibfk_1` FOREIGN KEY (`id_categoria`) REFERENCES `categoria` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `status_pedido` (
  `id` int NOT NULL,
  `status` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `usuario` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `usuario` varchar(30) NOT NULL,
  `email` varchar(200) NOT NULL,
  `senha` varchar(80) NOT NULL,
  `nome` varchar(50) DEFAULT NULL,
  `sobrenome` varchar(100) DEFAULT NULL,
  `data_nascimento` date DEFAULT NULL,
  `endereco` varchar(80) DEFAULT NULL,
  `cidade` varchar(40) DEFAULT NULL,
  `estado` char(2) DEFAULT NULL,
  `data_criacao` date DEFAULT NULL,
  `data_modificacao` date DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
